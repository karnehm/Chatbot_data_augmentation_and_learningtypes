import logging
import pickle
import sys, getopt
from typing import Text, Optional

import yaml
import asyncio
from rasa.cli.utils import print_error
from rasa.constants import DEFAULT_RESULTS_PATH, DEFAULT_MODELS_PATH
import rasa.core.test
import rasa.core.utils as core_utils
import rasa.cli.utils as cli_utils
from rasa.core.agent import Agent
from rasa.core.interpreter import RegexInterpreter
from rasa.exceptions import ModelNotFound
from rasa.model import get_model, get_model_subdirectories
from rasa.utils.common import set_log_level

logger = logging.getLogger(__name__)


def main(argv):
    set_log_level(None)
    model, train_data, test_data, config, run_name, original_config = initialize_values(argv)
    result_of_run = {}
    result_of_run['name'] = run_name
    result_of_run['importer'] = get_importer(original_config)
    result_of_run['policy'] = get_policies(config)
    loop = asyncio.get_event_loop()
    result_of_run['test'] = loop.run_until_complete(
        test_core(model=model, stories=test_data)
    )
    result_of_run['train'] = loop.run_until_complete(
        test_core(model=model, stories=train_data)
    )
    with open(model + '/test_run.pkl', 'fb') as f:
        pickle.dump(result_of_run, f)


def initialize_values(argv):
    train_data = ''
    test_data = ''
    config = ''
    model = ''
    original_config = ''
    run_name = ''
    try:
        opts, args = getopt.getopt(argv, "m:h:t:e:c:n:o:")
    except getopt.GetoptError:
        print('test.py -m <path/to/model/dir> -t <train/data> -e <test/data> -c <config.yml> -n <name-of-run>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-m':
            model = arg
        elif opt == '-h':
            print('test.py -t <test/data> -e <train/data> -c <config.yml> -n <name-of-run>')
            sys.exit()
        elif opt == "-t":
            train_data = arg
        elif opt in ("-e",):
            test_data = arg
        elif opt in ("-c"):
            config = arg
        elif opt == '-o':
            original_config = arg
        elif opt in ("-n"):
            run_name = arg
    return model, train_data, test_data, config, run_name, original_config


def get_importer(config):
    importer = {}
    print(config)
    with open(config, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    try:
        for attr in data_loaded['importers'][0]:
            if not attr == 'name':
              importer[attr] = data_loaded['importers'][0][attr]
    except:
        print('Only found')
    return importer

def get_policies(config):
    with open(config, 'r') as stream:
        data_loaded = yaml.safe_load(stream)
    return data_loaded['policies']

async def test_core(
        model: Text,
        stories: Text,
        endpoints: Optional[Text] = None,
        output: Text = DEFAULT_RESULTS_PATH ):
    _endpoints = core_utils.AvailableEndpoints.read_endpoints(endpoints)
    model = cli_utils.get_validated_path(model, "model", DEFAULT_MODELS_PATH)
    try:
        unpacked_model = get_model(model)
    except ModelNotFound:
        print_error(
            "Unable to test: could not find a model. Use 'rasa train' to train a "
            "Rasa model and provide it via the '--model' argument."
        )
        return

    core_path, nlu_path = get_model_subdirectories(unpacked_model)

    if not core_path:
        print_error(
            "Unable to test: could not find a Core model. Use 'rasa train' to train a "
            "Rasa model and provide it via the '--model' argument."
        )

    _interpreter = RegexInterpreter()

    _agent = Agent.load(unpacked_model, interpreter=_interpreter)

    return await rasa.core.test(stories, _agent, out_directory=output)


if __name__ == "__main__":
   main(sys.argv[1:])