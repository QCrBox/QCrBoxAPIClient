"""Invoking an interactive olex2 session.

This is an example script of creating a dataset and passing the data file within
the dataset to the API to invoke an Olex2 session accessible at:

    http://127.0.0.1:12004/vnc.html?path=vnc&autoconnect=true&resize=remote&reconnect=true&show_dot=true

NB: you will need to remove the calls to `close_interactive_session` and
`delete_dataset_by_id` to actually interact with the interactive session.
"""

import io
import pathlib
import time

from qcrboxapiclient.api.datasets import create_dataset, delete_dataset_by_id
from qcrboxapiclient.api.interactive_sessions import (
    close_interactive_session,
    create_interactive_session_with_arguments,
)
from qcrboxapiclient.client import Client
from qcrboxapiclient.models import (
    CreateDatasetBody,
    CreateInteractiveSessionParameters,
    CreateInteractiveSessionParametersArguments,
    QCrBoxErrorResponse,
)
from qcrboxapiclient.types import File

# Create a synchronous client, which is passed to each `sync()` for an API endpoint
# via keyword
client = Client(base_url="http://127.0.0.1:11000")

# Example file in QCrBox repository, but could substitite with `work.cif` which
# 100% works w/ Olex2 and Crystal Explorer
test_file = pathlib.Path("../robot_tests/test_data/api_client_test_cif.cif").resolve()

# To upload the file to the registry, we need to create a dataset and attach the
# file to it. Files are sent via the API as binary in a CreateDatasetBody payload
with test_file.open("rb") as f:
    file = File(io.BytesIO(f.read()), test_file.name)
upload_payload = CreateDatasetBody(file)

# Uploading the file with this endpoint creates a dataset containing this file.
# Assuming everything went OK, thn we will get a QCrBoxResponse. If an error
# occurred then the response is of type QCrBoxErrorResponse
response = create_dataset.sync(client=client, body=upload_payload)
if isinstance(response, QCrBoxErrorResponse) or response is None:
    raise TypeError("Failed to upload file")
else:
    print("Created dataset:", response)

# The response returns the created object in payload.datasets[0]. Note that this
# doesn't contain any of the file's binary data and instead contains metadata
# about the dataset and data files in the data set.
dataset_id = response.payload.datasets[0].qcrbox_dataset_id
data_file_id = response.payload.datasets[0].data_files[test_file.name].qcrbox_file_id

# To create an interactive olex2 session we call the create_interactive_session_with_arguments
# endpoint with a payload of application we want to start and arguments for the olex2
# command. For olex2, we need an argument named "input_file" which contains a data_file_id.
# Note that the arguments is a dict and we use `CreateInteractiveSessionArguments` to
# marshal out input into Json for the API
arguments = CreateInteractiveSessionParametersArguments.from_dict({"input_file": {"data_file_id": data_file_id}})
create_session = CreateInteractiveSessionParameters("olex2", "1.5-alpha", arguments)
response = create_interactive_session_with_arguments.sync(client=client, body=create_session)
if isinstance(response, QCrBoxErrorResponse) or response is None:
    raise TypeError("Failed to start interactive session")
else:
    print("Created interactive session:", response)

# The response from this endpoint is slightly different as it returns a reference
# to the create object, rather than the object iself. The payload contains the
# interactive_session_id which is also the calcualtion id of the interactive session
session_id = response.payload.interactive_session_id
print("Session ID:", session_id)

# We can close the interactive session now. But we should sleep for a little while
# so things have time to registry in all the databases and the run command can
# execute
time.sleep(3)
response = close_interactive_session.sync(client=client, id=session_id)
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to close interactive session")
else:
    print("Closed interactive session:", response)

# Delete the dataset afterward, because we are just using this for test purposes
response = delete_dataset_by_id.sync(id=dataset_id, client=client)
if isinstance(response, QCrBoxErrorResponse):
    raise TypeError("Failed to delete test dataset")
else:
    print("Deleted test dataset")
