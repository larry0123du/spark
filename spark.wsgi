#!/usr/bin/python
import sys
import logging
logging.basicConfig(stream=sys.stderr)
sys.path.insert(0,"/var/www/spark/")

from spark import app as application
application.secret_key = 'your secret key. If you share your website, do NOT share it with this key.'