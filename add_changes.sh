#!/bin/bash

git add .
pytest tests/ && git commit -m $1 || git reset --hard
