import random
from typing import Text, Optional, Union, List, Dict

from rasa.core import interpreter
from rasa.core.events import Event, ActionExecuted, UserUttered, SlotSet
from rasa.core.exceptions import StoryParseError
from rasa.core.interpreter import RegexInterpreter
from rasa.core.training import StoryGraph
from rasa.core.training.dsl import StoryFileReader
from rasa.core.training.structures import Story, StoryStep
from rasa.importers.rasa import RasaFileImporter

from importer.helper import get_graph, get_all_interactions


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
        self.graph = get_graph(domain, story_steps)
        number_of_storys = len(story_steps) * 3
        probability_of_termination = 0.1

        for story_number in range(number_of_storys):
            events = []
            interactions = get_all_interactions(domain)
            current_interaction = random.choice(interactions)
            while random.random() >= probability_of_termination:
                # create and add current Event
                new_event = None
                if current_interaction in domain.slots:
                    new_event = create_slot(current_interaction)
                elif current_interaction in domain.action_names:
                    new_event = create_action(current_interaction)
                elif current_interaction in domain.user_actions:
                    new_event = await create_intent(current_interaction)
                events.append(new_event)
                current_interaction = random.choice(self.get_next_events(current_interaction))
            story_steps.append(StoryStep(events=events))

    def get_next_events(self, current_event):
        return [key for key, val in self.graph[current_event].items() if val == 1]


def create_slot(slot_name):
    return SlotSet(slot_name)


def create_action(action_name):
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


async def create_intent(intent_name):
    # Intent
    parse_data = await interpreter.parse(intent_name)
    intent = UserUttered(
        intent_name, parse_data.get("intent"), parse_data.get("entities"), parse_data
    )
    return intent