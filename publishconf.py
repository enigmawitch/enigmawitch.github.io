# -*- coding: utf-8 -*- #
# Configuration utilisée uniquement pour le build de production (GitHub Actions).
import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from pelicanconf import *  # noqa: E402,F401,F403

# URL publique du site — à adapter si le dépôt ne s'appelle pas <user>.github.io
# ex. https://alice.github.io/blog-cyber/  →  SITEURL = "/blog-cyber"
SITEURL = os.environ.get("SITEURL", "")
RELATIVE_URLS = False

DELETE_OUTPUT_DIRECTORY = True
