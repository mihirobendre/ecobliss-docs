#!/bin/bash

echo "Installing Python libraries..."
pip install earthengine-api geemap
earthengine authenticate --force

