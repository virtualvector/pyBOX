#!/usr/bin/env bash
python HelloWorld.py > /dev/null &
nosetests --with-coverage
