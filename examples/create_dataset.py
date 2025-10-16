import io
import pathlib

from qcrboxapiclient.api.datasets import create_dataset
from qcrboxapiclient.client import Client
from qcrboxapiclient.models import (
    CreateDatasetBody,
    QCrBoxErrorResponse,
)
from qcrboxapiclient.types import File

client = Client(base_url="http://127.0.0.1:11000")

test_file = pathlib.Path("../robot_tests/test_data/api_client_test_cif.cif").resolve()

with test_file.open("rb") as f:
    file = File(io.BytesIO(f.read()), test_file.name)
upload_payload = CreateDatasetBody(file)

response = create_dataset.sync(client=client, body=upload_payload)
if isinstance(response, QCrBoxErrorResponse) or response is None:
    raise TypeError("Failed to upload file")
else:
    print("Created dataset:", response)
