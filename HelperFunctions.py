import re

from API.helldivers_2_client.models import Assignment2
from API.helldivers_2_client.models import Reward2
from API.helldivers_2_client.models import Task2
from API.helldivers_2_client.models import Dispatch
from API.helldivers_2_client.models import SteamNews

# Regex to remove markup tags
CLEANR = re.compile('<.*?>')

def format_major_order(MO: Assignment2) -> str:
    briefing = clean_markups(MO.briefing)
    expiration = format_time(MO.expiration)
    rewards = parse_rewards(MO.reward)

    order = f'# MAJOR ORDER\n**Brief**: {briefing}\n**Description**: {MO.description}\n**Rewards**: {rewards}\n**Expiration**: {expiration}\n**Progress**: {MO.progress}'

    return order

def format_dispatch(dispatch: Dispatch) -> str:
    message = clean_markups(dispatch.message)
    return f'## DISPATCH\n**Published**: {format_time(dispatch.published)}\n**Message**:\n{message}'

# TODO news.content has errors when writing to discord, probably because of Steams markup language. Not sure if I even want to add the content
def format_news(news:SteamNews):
    return f'# Steam News\n**{news.title}**\n{news.url}\n'

def format_time(time) -> str:
    return time.strftime("%H:%M:%S %d-%b-%Y")

def clean_markups(string: str) -> str:
    return re.sub(CLEANR, '', string)

def parse_rewards(reward: Reward2) -> str:
    # Not sure whta all these values will be, assign the raw value
    type = reward.type
    if type == 1:
        type = 'Medals'

    return f'{reward.amount} {type}'