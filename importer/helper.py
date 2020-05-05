import random
from typing import List
import networkx as nx
import matplotlib.pyplot as plt


from rasa.core.events import UserUttered, ActionExecuted, SlotSet


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


def get_graph(domain, story_steps):
    graph = create_matrix_structur(domain, 0)
    for story_step in story_steps:
        for x in range(len(story_step.events)):
            # if current event is not last of story
            if x + 1 < len(story_step.events):
                x_name = get_event_name(story_step.events[x])
                y_name = get_event_name(story_step.events[x + 1])
                graph[x_name][y_name] = 1
    return graph

def get_event_name(event):
    datatype = type(event)
    if datatype == UserUttered:
        return event.intent['name']
    elif datatype == ActionExecuted:
        return event.action_name
    elif datatype == SlotSet:
        return event.key
    else:
        print('ERROR')
        return None


def draw_graph(story_steps, file_name):
    edges = get_edges(story_steps)
    G = nx.DiGraph()
    G.add_edges_from(edges)
    plt.figure(figsize=(50,50))
    nx.draw_circular(G, with_label=True, font_size=9 ,color=[76], cmap=plt.cm.Blues)
    plt.savefig(file_name + '.png')
    nx.write_graphml(G, file_name + '.graphml')


def get_edges(story_steps):
    edges = []
    for story_step in story_steps:
        for x in range(len(story_step.events)):
            # if current event is not last of story
            if x + 1 < len(story_step.events):
                edges.append((get_event_name(story_step.events[x]), get_event_name(story_step.events[x + 1])))
    return edges


def get_all_interactions(domain):
    # all Actions and intents as Array
    interactions = []
    for action in domain.action_names:
        interactions.append(action)
    for intent in domain.intents:
        interactions.append(intent)
    for slot in domain.slots:
        interactions.append(slot.name)
    return interactions

def create_matrix_structur(domain, initial_value):
    interactions = get_all_interactions(domain)
    # Initialize Struktur
    matrix = {}
    for x_interaction in interactions:
        matrix[x_interaction] = {}
        for y_interaction in interactions:
            matrix[x_interaction][y_interaction] = initial_value
    return matrix

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
