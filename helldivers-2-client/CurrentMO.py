from helldivers_2_client import Client

client = Client(base_url="https://helldivers-2-dotnet.fly.dev/")

from helldivers_2_client.models import assignment_2
from helldivers_2_client.api.v1 import get_api_v1_assignments_all

with client as client:
    my_data: assignment_2 = get_api_v1_assignments_all.sync( client=client)

    print(my_data)