#!/usr/bin/python

# For running in virtual environment
# activate_this = '/var/www/flaskapp/venv/bin/activate_this.py'
# execfile(activate_this, dict(__file__=activate_this))

import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/flaskapp/")

from app import app as application
