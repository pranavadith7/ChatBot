# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

# from typing import Any, Text, Dict, List
#
# from rasa_sdk import Action, Tracker
# from rasa_sdk.executor import CollectingDispatcher
#
#
# class ActionHelloWorld(Action):
#
#     def name(self) -> Text:
#         return "action_hello_world"
#
#     def run(self, dispatcher: CollectingDispatcher,
#             tracker: Tracker,
#             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
#
#         dispatcher.utter_message(text="Hello World!")
#
#         return []
from typing import Any, Text, Dict,List
from database import DataUpdate
from rasa_sdk import Action,Tracker
from rasa_sdk.events import SlotSet, EventType
from rasa_sdk.executor import CollectingDispatcher
from database import DataDelete
import webbrowser


# print("Im in !!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!s")

class ActionVideo(Action):
    def name(self) -> Text:
        return "action_video"
    
    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        t=tracker.latest_message["text"]
        # print(t)
        web_url="https://rasa.com/docs/rasa/forms/"
        dispatcher.utter_message("wait... opening your link")
        webbrowser.open(web_url)
        return []

class EditDetails(Action):
    def name(self) -> Text:
        return "edit_details"
    
    async def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        t=tracker.latest_message["text"]
        # print(t)
        t=t.lower()
        if t=='name':
            return [SlotSet("name",None)]
        elif t=='location':
            return [SlotSet("location",None)]
        elif t=='destination':
            return [SlotSet("destination",None)]
        elif t=='car type':
            return [SlotSet("car_type",None)]
        elif t=='total people':
            return [SlotSet("total_people",None)]
        elif t=='date':
            return [SlotSet("date",None)]
        elif t=='time':
            return [SlotSet("time",None)]
        return []

class CancelBooking(Action):
    def name(self) -> Text:
        return "cancel_booking"
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain:Dict
    ) -> List[EventType]:
        required_slots =["name","location","destination","car_type","total_people","date","time"]
        
        for slot_name in required_slots:
            SlotSet(slot_name,None)
            
        DataDelete(name=tracker.get_slot("name"))
        
        #once all slots are filled
        return [SlotSet("requested_slot",None)]

class ValidateDetailsForm(Action):
    def name(self) -> Text:
        return "user_details_form"
        
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain:Dict
    ) -> List[EventType]:
        required_slots =["name","location","destination","car_type","total_people","date","time"]
        
        for slot_name in required_slots:
            if tracker.slots.get(slot_name) is None:
                return [SlotSet("requested_slot",slot_name)]
            
        #once all slots are filled
        return [SlotSet("requested_slot",None)]
    
    
class ActionSubmit(Action):
    def name(self) -> Text :
        # print(Text)
        return "action_submit"
    
    def run(
        self,
        dispatcher,
        tracker: Tracker,
        domain: "DomainDict",
    ) -> List[Dict[Text,Any]]:
        # print(tracker.get_slot("name"))
        DataUpdate(name=tracker.get_slot("name"), location=tracker.get_slot("location"), destination=tracker.get_slot("destination"), car_type=tracker.get_slot("car_type"), total_people=tracker.get_slot("total_people"), date=tracker.get_slot("date"), time=tracker.get_slot("time"))
        dispatcher.utter_message(template="utter_details_thanks", Name=tracker.get_slot("name"),Location=tracker.get_slot("location"),Destination=tracker.get_slot("destination"),Car_type=tracker.get_slot("car_type"),Total_people=tracker.get_slot("total_people"),Date=tracker.get_slot("date"),Time=tracker.get_slot("time")) 