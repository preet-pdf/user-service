#!/bin/bash
python -m grpc_tools.protoc -I=. --python_out=../app/grpc --grpc_python_out=../app/grpc update_rule.proto
