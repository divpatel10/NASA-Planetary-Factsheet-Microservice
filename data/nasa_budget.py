import os
from dotenv import load_dotenv
import requests, json
load_dotenv()

SHEETS_API = os.getenv('SHEETS_API_KEY')
SPREADSHEET_ID = "12frTU01gfT1CXGWFimN3whf4348F_r3XolTqBt02OyM"


def get_link(sheet_name):
    ADD_KEY = f"?key={SHEETS_API}"
    NASA_MISSION_BUDGET = f"https://sheets.googleapis.com/v4/spreadsheets/{SPREADSHEET_ID}/values/"

    return f"{NASA_MISSION_BUDGET}{sheet_name}{ADD_KEY}"

def get_mission():
    try:
        url = requests.get(get_link("Mission Costs"))
    except:
        print("Unhandled Exception")
        return("Unhandled Exception")
    



data = json.loads(get_mission)
print(data)