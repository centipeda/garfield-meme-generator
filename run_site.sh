#!/bin/sh
cd ~/apps/garfield-meme-generator
python3 -m waitress --port=4567 --call app:create_app
