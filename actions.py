# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa.core.events import SlotSet
from rasa.core.actions import Action


class ActionSearchRestaurant(Action):

    def name(self):
        return "action_search_restaurant"

    def run(self, dispatcher, tracker, domain):

        return [SlotSet('restaurant', 'restaurant')]


class ActionSearchHotel(Action):

    def name(self):
        return "action_search_hotel"

    def run(self, dispatcher, tracker, domain):

        return [SlotSet('hotel', 'hotel')]
