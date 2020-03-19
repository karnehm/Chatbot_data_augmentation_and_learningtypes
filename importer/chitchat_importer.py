import logging
import re
from typing import Dict, List, Optional, Text, Union

from rasa.core.domain import Domain
from rasa.core.events import Event, ActionExecuted, UserUttered
from rasa.core.exceptions import StoryParseError
from rasa.core.interpreter import NaturalLanguageInterpreter, RegexInterpreter
from rasa.core.training.dsl import StoryFileReader
from rasa.core.training.structures import StoryGraph
from rasa.importers import utils
from rasa.importers.rasa import RasaFileImporter
from rasa.nlu.training_data import TrainingData
from rasa.utils.common import raise_warning

logger = logging.getLogger(__name__)


def get_possible_indexes(story) -> List:
    indexes = []
    last_datatype = None
    current_index = 0
    for event in story.events:
        current_datatype = type(event)
        if current_datatype != last_datatype and current_datatype == UserUttered:
            indexes.append(current_index)
        last_datatype = type(event)
        current_index += 1
    return indexes


class ChitchatImporter(RasaFileImporter):
    """Default `TrainingFileImporter` implementation."""

    def __init__(
        self,
        config_file: Optional[Text] = None,
        domain_path: Optional[Text] = None,
        training_data_paths: Optional[Union[List[Text], Text]] = None,
    ):
        print('INIT')
        super().__init__(config_file, domain_path, training_data_paths)

    async def get_config(self) -> Dict:
        print('get_config')
        config = await super().get_config()
        return config

    async def get_stories(
        self,
        interpreter: "NaturalLanguageInterpreter" = RegexInterpreter(),
        template_variables: Optional[Dict] = None,
        use_e2e: bool = False,
        exclusion_percentage: Optional[int] = None,
    ) -> StoryGraph:
        print('get_stories')
        #stories = await super().get_stories(interpreter, template_variables, use_e2e, exclusion_percentage)
        #return stories
        story_steps = await StoryFileReader.read_from_files(
            self._story_files,
            await self.get_domain(),
            interpreter,
            template_variables,
            use_e2e,
            exclusion_percentage,
        )
        reader = StoryFileReader(interpreter, await self.get_domain(), template_variables, use_e2e)
        story_steps_copy = story_steps.copy()
        for story in story_steps:
            indexes = get_possible_indexes(story)
            story = await self.add_chitchat_to_story(story.create_copy(True), await self.get_domain(), [0, 3], interpreter)
            story_steps_copy.append(story)
        return StoryGraph(story_steps_copy)

    async def get_nlu_data(self, language: Optional[Text] = "en") -> TrainingData:
        print('get_nlu_data')
        nlu = await super().get_nlu_data(language)
        path = set()
        path.add('data/chitchat_nlu.md')
        chitchat_nlu = utils.training_data_from_paths(path, language)
        nlu = nlu.merge(chitchat_nlu)
        return nlu

    async def get_domain(self) -> Domain:
        domain = await super().get_domain()
        chitchat_domain = Domain.from_file('data/chitchat_domain.yml')
        domain = domain.merge(chitchat_domain, False)
        return domain

    async def add_chitchat_to_story(self,
                                    story,
                                    domain: Domain,
                                    indexes: List,
                                    interpreter: "NaturalLanguageInterpreter" = RegexInterpreter()):
        # Delete Indexes, if they greater then the length of the story or lower 0
        indexes = sorted(set(indexes))
        regex = re.compile('')
        indexes = [i for i in indexes if i >= 0 and i < len(story.events)]
        for index in indexes:
            # Intent
            intent = 'chitchat'
            parse_data = await interpreter.parse(intent)
            utterance = UserUttered(
                intent, parse_data.get("intent"), parse_data.get("entities"), parse_data
            )
            intent_name = utterance.intent.get("name")
            if domain and intent_name not in domain.intents:
                raise_warning(
                    f"Found unknown intent '{intent_name}'. "
                    "Please, make sure that all intents are "
                    "listed in your domain yaml.",
                    UserWarning,
                )
            # Utter
            # Copyied at dsl.py
            # def add_event(self, event_name, parameters):
            parameters = {}
            event_name = "utter_chitchat"
            # add 'name' only if event is not a SlotSet,
            # because there might be a slot with slot_key='name'
            parameters["name"] = event_name

            parsed_events = Event.from_story_string(
                event_name, parameters, default=ActionExecuted
            )
            if parsed_events is None:
                raise StoryParseError(
                    "Unknown event '{}'. It is Neither an event "
                    "nor an action).".format(event_name)
                )

            # Add to Story
            story.events.insert(index, utterance)
            index += 1
            for parsed_event in parsed_events:
                story.events.insert(index, parsed_event)
                index += 1

        return story
