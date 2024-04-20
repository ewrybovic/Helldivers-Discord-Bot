import re

from API.helldivers_2_client.models import Assignment2
from API.helldivers_2_client.models import Dispatch

# Regex to remove markup tags
CLEANR = re.compile('<.*?>')

def format_major_order(MO: Assignment2) -> str:
    briefing = clean_markups(MO.briefing)
    return f'# MAJOR ORDER\n**Brief**: {briefing}\n**Description**: {MO.description}\n**Expiration**: {format_time(MO.expiration)}\n**Progress**: {MO.progress}'

def format_dispatch(dispatch: Dispatch) -> str:
    message = clean_markups(dispatch.message)
    return f'## DISPATCH\n**Published**: {format_time(dispatch.published)}\n**Message**:\n{message}'

def format_time(time) -> str:
    return time.strftime("%H:%M:%S %d-%b-%Y")

def check_new_order(MO: Assignment2, currentMOID: int) -> bool:
    if currentMOID != MO.id:
        # Wrtie new mo id
        with open('majorOrder.txt', 'w') as f:
            f.write(str(MO.id))
        
        currentMOID = MO.id
        return True
    else:
        return False

def clean_markups(string: str) -> str:
    return re.sub(CLEANR, '', string)