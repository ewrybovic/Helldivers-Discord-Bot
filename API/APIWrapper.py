from .helldivers_2_client import Client

from .helldivers_2_client.models import Assignment2
from .helldivers_2_client.models import Dispatch
from .helldivers_2_client.api.v1 import get_api_v1_assignments_all
from .helldivers_2_client.api.v1 import get_api_v1_dispatches_all

URL = "https://helldivers-2-dotnet.fly.dev/"
HEADERS = {
    'User-Agent': 'Helldivers-Discord-Bot',
    'X-Application-Contact' : 'rybovic.evan@gmail.com'
    }

def GetCurrentMO() -> Assignment2:
    CurrentMO: Assignment2

    with Client(base_url=URL, headers=HEADERS) as client:
        data: Assignment2 = get_api_v1_assignments_all.sync( client=client)

        if data is not None:
            CurrentMO = data[0]

            print(f'Breifing: {CurrentMO.briefing}')
            print(f'Description: {CurrentMO.description}')
            print(f'Expiration: {CurrentMO.expiration}')
            print(f'Progress: {CurrentMO.progress}')

            return CurrentMO
        else:
            return None

def GetCurrentDispatch() -> Dispatch:
    dispatch: Dispatch

    with Client(base_url=URL, headers=HEADERS) as client:
        data = get_api_v1_dispatches_all.sync(client=client)

        if data is not None:
            for dispatch in data:
                print(dispatch)

                if dispatch.message is not None:
                    print("good dispatch")
                    return dispatch
        
        return None

    
if __name__ == '__main__':
    #GetCurrentMO()
    GetCurrentDispatch()