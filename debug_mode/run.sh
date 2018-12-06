#!/bin/sh

set -x
echo "debug:"
python main.py

echo "basic optimization:"
python -O main.py

echo "optimization(discard docstring):"
python -OO main.py
