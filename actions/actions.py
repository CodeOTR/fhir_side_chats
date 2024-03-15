from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.events import SlotSet
from rasa_sdk.executor import CollectingDispatcher

class SubmitSymptomForm(Action):
    def name(self) -> Text:
        return "submit_symptom_form"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        symptom = tracker.get_slot("symptom_name")
        severity = tracker.get_slot("symptom_severity")
        duration = tracker.get_slot("symptom_duration")

        # TODO: Convert to FHIR format and save to server

        dispatcher.utter_message(text="Thanks for sharing your symptoms. I've recorded the following:")
        dispatcher.utter_message(text=f"- Symptom: {symptom}")
        dispatcher.utter_message(text=f"- Severity: {severity}")
        dispatcher.utter_message(text=f"- Duration: {duration}")

        return []