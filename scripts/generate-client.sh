#!/bin/bash

openapi-python-client generate \
	--url http://127.0.0.1:11000/api/openapi-schema \
	--config config.yaml \
	--output-path . \
	--overwrite

