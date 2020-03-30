from random import random
from typing import List

from rasa.core.events import UserUttered


def get_possible_indexes(story) -> List:
    indexes = []
    last_datatype = None
    current_index = 0
    for event in story.events:
        current_datatype = type(event)
        if current_datatype != last_datatype and current_datatype == UserUttered():
            indexes.append(current_index)
        last_datatype = type(event)
        current_index += 1
    return indexes


class ImportHelper:

    def __init__(self, class_name, config):
        self.config = config["importers"]
        self.class_name = class_name
        random.seed(4)

    def get_param(self, param, default=None):
        for c in self.config:
            if self.class_name in c["name"] and param in c:
                return c[param]
        return default

    def get_indexes(self, stories, copy_nr):
        indexes = []

        per_story = self.get_param('per_story')
        each_n = self.get_param('each_n', 1)
        shuffle = self.get_param('shuffle', False)

        for story in stories:
            story_indexes = get_possible_indexes(story)

            story_indexes = [i for idx, i in enumerate(story_indexes)
                             if (idx + 1 + copy_nr) % each_n == 0]

            # Shuffle, if config set True
            if shuffle:
                random.shuffle(story_indexes)
            story_indexes = story_indexes[:per_story]
            indexes.append(story_indexes)
        return indexes
