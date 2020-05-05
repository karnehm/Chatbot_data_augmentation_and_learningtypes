import random
from typing import Optional, Text, Union, List, Dict

from rasa.core.events import ActionExecuted, Event, UserUttered, SlotSet
from rasa.core.exceptions import StoryParseError
from rasa.core.interpreter import RegexInterpreter
from rasa.core.training.structures import StoryGraph
from rasa.core.training.dsl import StoryFileReader
from rasa.importers.rasa import RasaFileImporter

from importer.helper import get_graph, get_all_interactions, ImportHelper


class CreateNewDialogesByGraphImporter(RasaFileImporter):
    """Default `TrainingFileImporter` implementation."""

    def __init__(
            self,
            config_file: Optional[Text] = None,
            domain_path: Optional[Text] = None,
            training_data_paths: Optional[Union[List[Text], Text]] = None,
    ):
        super().__init__(config_file, domain_path, training_data_paths)
        random.seed(4)
        self.helper = ImportHelper(type(self).__name__, self.config)


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
        story_file_reader = StoryFileReader(interpreter, domain, template_variables, use_e2e)
        self.graph = get_graph(domain, story_steps)
        number_of_storys = len(story_steps) * self.helper.get_param('multiplication', 1)
        probability_of_termination = self.helper.get_param('average_length', 10) ** -1
        for story_number in range(number_of_storys):
            events = []
            interactions = get_all_interactions(domain)
            current_interaction = random.choice(interactions)
            end_of_story = False
            story_steps_lines = ['## Random Story ' + str(int (random.random() * 10000))]
            while random.random() >= probability_of_termination and not end_of_story:
                # create and add current Event
                if current_interaction in domain.action_names:
                    story_steps_lines.append('- ' + current_interaction)
                elif current_interaction in domain.intents:
                    story_steps_lines.append('* ' + current_interaction)

                possible_next_interactions = self.get_next_events(current_interaction)
                if len(possible_next_interactions) > 0 or possible_next_interactions == None:
                    current_interaction = random.choice(possible_next_interactions)
                else:
                    end_of_story = True

            story_step = await story_file_reader.process_lines(story_steps_lines)
            story_steps.extend(story_step)
        return StoryGraph(story_steps)

    def get_next_events(self, current_event):
        return [key for key, val in self.graph[current_event].items() if val == 1]


    def create_slot(self, slot_name):
        return SlotSet(slot_name)


    def create_action(self, action_name):
        # Utter
        # Copyied at dsl.py
        # def add_event(self, event_name, parameters):
        parameters = {}
        # add 'name' only if event is not a SlotSet,
        # because there might be a slot with slot_key='name'
        parameters["name"] = action_name

        parsed_events = Event.from_story_string(
            action_name, parameters, default=ActionExecuted
        )
        if parsed_events is None:
            raise StoryParseError(
                "Unknown event '{}'. It is Neither an event "
                "nor an action).".format(action_name)
            )
        return parsed_events


    async def create_intent(self, intent_name, interpreter):
        # Intent
        parse_data = await interpreter.parse(intent_name)
        intent = UserUttered(
            intent_name, parse_data.get("intent"), parse_data.get("entities"), parse_data
        )
        return intent