from qcrboxapiclient import Client
from qcrboxapiclient.api.default.api_calculations_id_get_calculation_by_id import sync, sync_detailed

client = Client("http://127.0.0.1:11000")
response = sync(id=1, client=client)
response_detailed = sync_detailed(id=1, client=client)
print(response)
