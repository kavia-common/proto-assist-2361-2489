#!/bin/bash
cd /home/kavia/workspace/code-generation/proto-assist-2361-2489/BackendAPI
source venv/bin/activate
flake8 .
LINT_EXIT_CODE=$?
if [ $LINT_EXIT_CODE -ne 0 ]; then
  exit 1
fi

