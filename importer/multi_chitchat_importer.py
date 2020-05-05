import random
from typing import Optional, Text, Union, List, Dict

from rasa.core.domain import Domain
from rasa.core.events import ActionExecuted, Event, UserUttered
from rasa.core.exceptions import StoryParseError
from rasa.core.interpreter import RegexInterpreter
from rasa.core.training.structures import StoryGraph
from rasa.core.training.dsl import StoryFileReader
from rasa.importers import utils
from rasa.importers.rasa import RasaFileImporter
from rasa.nlu.training_data import TrainingData
from rasa.utils.common import raise_warning

from importer.helper import ImportHelper


class MultiChitchatImporter(RasaFileImporter):

    def __init__(
            self,
            config_file: Optional[Text] = None,
            domain_path: Optional[Text] = None,
            training_data_paths: Optional[Union[List[Text], Text]] = None,
    ):
        super().__init__(config_file, domain_path, training_data_paths)
        self.helper = ImportHelper(type(self).__name__, self.config)
        self.chitchat_domain = None
        self.chitchat_nlu = None
        random.seed(4)

    async def get_nlu_data(self, language: Optional[Text] = "en") -> TrainingData:
        nlu = await super().get_nlu_data(language)
        path = set()
        path.add(self.helper.get_param("nlu_data_file","data/chitchat_nlu.md"))
        self.chitchat_nlu = utils.training_data_from_paths(path, language)
        nlu = nlu.merge(self.chitchat_nlu)
        return nlu

    async def get_domain(self) -> Domain:
        domain = await super().get_domain()
        self.chitchat_domain = Domain.from_file(self.helper.get_param("domain_data_file", "data/chitchat_domain.yml"))
        domain = domain.merge(self.chitchat_domain, False)
        return domain

    async def get_stories(
            self,
            interpreter: "NaturalLanguageInterpreter" = RegexInterpreter(),
            template_variables: Optional[Dict] = None,
            use_e2e: bool = False,
            exclusion_percentage: Optional[int] = None,
    ) -> StoryGraph:

        domain = await self.get_domain()
        story_steps = await StoryFileReader.read_from_files(
            self._story_files,
            domain,
            interpreter,
            template_variables,
            use_e2e,
            exclusion_percentage,
        )

        story_steps_copy = []
        if(self.helper.get_param('add_original_storys', False)):
            story_steps_copy = story_steps.copy()


        for copy_nr in range(self.helper.get_param('copys_per_story', 1)):
            indexes = self.helper.get_indexes(story_steps, copy_nr)
            for idx, story in enumerate(story_steps):
                story = await self.add_chitchat_to_story(story.create_copy(True), domain, indexes[idx],
                                                         interpreter)
                story_steps_copy.append(story)
        return StoryGraph(story_steps_copy)

    async def add_chitchat_to_story(self,
                                    story,
                                    domain: Domain,
                                    indexes: List,
                                    interpreter: "NaturalLanguageInterpreter" = RegexInterpreter()):

        # possible Chitchat
        chitchat_intent = self.chitchat_domain.intents
        chitchat_utter = [x for x in self.chitchat_domain.action_names if "utter_" in x]

        # Delete Indexes, if they greater then the length of the story or lower 0
        indexes = sorted(set(indexes))
        to_add = 0
        indexes = [i for i in indexes if i >= 0 and i < len(story.events)]
        for index in indexes:
            index += to_add
            # get last Utter
            last_utter = None
            if index - 1 >= 0:
                last_utter = story.events[index - 1]

            # Intent
            # intent = 'chitchat'

            intent = random.choice(chitchat_intent)
            intent_index = chitchat_intent.index(intent)
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
            event_name = chitchat_utter[intent_index]
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
            to_add += 1
            for parsed_event in parsed_events:
                story.events.insert(index, parsed_event)
                index += 1
                to_add += 1

            if last_utter and self.helper.get_param('consultation', False):
                story.events.insert(index, last_utter)
        return story