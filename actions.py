# -*- coding: utf-8 -*-
from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

from rasa_core_sdk import Tracker
from rasa_core_sdk.executor import CollectingDispatcher

from typing import Dict, Text, Any, List

import requests
from rasa_core_sdk import Action
from rasa_core_sdk.events import SlotSet, FollowupAction
from rasa_core_sdk.forms import FormAction




class FindAp(Action):
    """This action class retrieves the ap of the user."""

    def name(self):
        """Unique identifier of the action"""

        return "action_return_apname"

    def run(self, dispatcher, tracker, domain):

        ap_name = tracker.get_slot("ap")
        if ap_name == None:
            out_message = "For ap troubleshooting, check out this link: https://www.mist.com/documentation/troubleshooting-ap-disconnect-issues/"
        else:    
            out_message = "Wait a moment, I am searching log data for ap {} ".format(ap_name)
        
        dispatcher.utter_message(out_message)

        return []



