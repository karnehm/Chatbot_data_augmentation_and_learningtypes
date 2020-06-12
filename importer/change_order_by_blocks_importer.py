import random
from typing import Optional, Text, Union, List, Dict
import numpy as np
from rasa.core.interpreter import RegexInterpreter
from rasa.core.training.structures import StoryGraph
from rasa.core.training.dsl import StoryFileReader

from rasa.importers.rasa import RasaFileImporter

from importer.helper import get_possible_indexes, ImportHelper


def get_all_blocks(len_of_story, possible_indexes):
    blocks = np.array([
        possible_indexes[0],  # Start
        possible_indexes[1] - 1  # End
    ])
    for i in range(1, len(possible_indexes) - 1):
        block = np.array([
            possible_indexes[i],  # Start
            possible_indexes[i + 1] - 1  # End
        ])
        blocks = np.vstack((blocks, block))
    block = np.array([[
        possible_indexes[len(possible_indexes) - 1],  # Start
        len_of_story - 1  # End
    ]])

    # If there are only 2 possible indexes, the number of dimensions will
    # be 1 of blocks and for concatenation we need 2 dimensions
    if (len(possible_indexes) == 2):
        return np.concatenate(([blocks], block))
    return np.concatenate((blocks, block))


def shuffle_blocks(story, blocks):
    new_story = []
    np.random.shuffle(blocks)
    for block in blocks:
        new_story.extend(story[block[0]:block[1]])
    return new_story


def combine_blocks(blocks, number_of_blocks, number_of_stories):
    np.random.shuffle(blocks)
    end_blocks = blocks[:number_of_blocks]
    end_blocks.view('i8,i8').sort(order=['f1'], axis=0) #<-- returns None
    end_blocks[0][0] = 0 # First block starts at 0
    for i in range(1, number_of_blocks):
        end_blocks[i][0] = end_blocks[i - 1][1] # Block starts at End of Block before + 1
    end_blocks[number_of_blocks -1][1] = number_of_stories # Last Block ends at last Story
    return end_blocks


class ChangeOrderByBlocksImporter(RasaFileImporter):

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
        copy_story_steps = story_steps.copy()
        number_of_blocks = self.helper.get_param('number_of_blocks', 3)
        number_of_copies = self.helper.get_param('number_of_copies', 1)
        for copy in range(0, number_of_copies):
            for story in story_steps:
                possible_indexes = get_possible_indexes(story)
                blocks = get_all_blocks(len(story.events), possible_indexes)

                blocks = combine_blocks(blocks,
                                        number_of_blocks=
                                            (number_of_blocks if number_of_blocks <= len(blocks) else len(blocks)),
                                        number_of_stories=len(story.events))
                new_story = story.create_copy(True)
                new_story.events = shuffle_blocks(new_story.events, blocks)
                copy_story_steps.append(new_story)
        return StoryGraph(copy_story_steps)
