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

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionFetchDiseaseDescription(Action):
    def name(self) -> Text:
        return "action_fetch_disease_description"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        disease = tracker.get_slot("disease")
        
        # Fetch disease description from CSV file
        description = self.fetch_description_from_csv(disease)
        
        dispatcher.utter_message(text=description)

        return []

    def fetch_description_from_csv(self, disease: Text) -> Text:
        # Open the CSV file
        with open(r'C:\Users\DHARAVATH RAMDAS\chatbot111\clean_disease_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            # Find the disease in the CSV file
            for row in reader:
                if row['disease'] == disease:
                    return row['description']

        return "No description found for the disease."

class ActionFetchSymptoms(Action):
    def name(self) -> Text:
        return "action_fetch_symptoms"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease = tracker.get_slot("disease")
        
        # Fetch symptoms from CSV file
        symptoms = self.fetch_symptoms_from_csv(disease)
        
        dispatcher.utter_message(text=symptoms)

        return []

    def fetch_symptoms_from_csv(self, disease: Text) -> Text:
        # Open the CSV file
        with open(r'C:\Users\DHARAVATH RAMDAS\chatbot111\clean_disease_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            # Find the disease in the CSV file
            for row in reader:
                if row['disease'] == disease:
                    return row['symptoms']

        return "No symptoms found for the disease."

class ActionFetchPrevention(Action):
    def name(self) -> Text:
        return "action_fetch_prevention"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        disease = tracker.get_slot("disease")
        
        # Fetch prevention measures from CSV file
        prevention = self.fetch_prevention_from_csv(disease)
        
        dispatcher.utter_message(text=prevention)

        return []

    def fetch_prevention_from_csv(self, disease: Text) -> Text:
        # Open the CSV file
        with open(r'C:\Users\DHARAVATH RAMDAS\chatbot111\clean_disease_data.csv', 'r') as file:
            reader = csv.DictReader(file)
            
            # Find the disease in the CSV file
            for row in reader:
                if row['disease'] == disease:
                    return row['prevention']

        return "No prevention measures found for the disease."
