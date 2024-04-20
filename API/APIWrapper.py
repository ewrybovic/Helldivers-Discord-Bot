from .helldivers_2_client import Client

from .helldivers_2_client.models import Assignment2
from .helldivers_2_client.models import Dispatch
from .helldivers_2_client.api.v1 import get_api_v1_assignments_all
from .helldivers_2_client.api.v1 import get_api_v1_dispatches_all


def GetCurrentMO() -> Assignment2:
    client = Client(base_url="https://helldivers-2-dotnet.fly.dev/")
    CurrentMO: Assignment2

    with client as client:
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

def GetMostRecentDispatchs(previousIndex: int) -> []:
    dispatch: Dispatch

    with Client(base_url="https://helldivers-2-dotnet.fly.dev/") as client:
        data = get_api_v1_dispatches_all.sync(client=client)

        if data is not None:
            print(data)

def GetCurrentDispatch() -> Dispatch:
    dispatch: Dispatch

    with Client(base_url="https://helldivers-2-dotnet.fly.dev/") as client:
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