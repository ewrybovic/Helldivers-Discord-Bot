from .helldivers_2_client import Client

from .helldivers_2_client.models import Assignment2
from .helldivers_2_client.api.v1 import get_api_v1_assignments_all


def GetCurrentMO() -> Assignment2:
    client = Client(base_url="https://helldivers-2-dotnet.fly.dev/")
    CurrentMO: Assignment2

    with client as client:
        CurrentMO: Assignment2 = get_api_v1_assignments_all.sync( client=client)
        return CurrentMO