import random
from typing import Optional, Text, Union, List, Dict


from rasa.core.interpreter import RegexInterpreter
from rasa.core.training.structures import StoryGraph, StoryStep
from rasa.core.training.dsl import StoryFileReader
from rasa.importers.rasa import RasaFileImporter

from importer.helper import get_possible_indexes


class ChangeOrderImporter(RasaFileImporter):
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
        copy_story_steps = story_steps.copy()

        for story in story_steps:
            possible_indexes = get_possible_indexes(story)
            choosed_index = random.choice(possible_indexes)
            new_story = story.create_copy(True)
            new_story.events = new_story.events[choosed_index:] + new_story.events[:choosed_index]
            copy_story_steps.append(new_story)
        return StoryGraph(copy_story_steps)

