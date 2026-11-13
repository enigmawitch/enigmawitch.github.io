# -*- coding: utf-8 -*- #
AUTHOR = "EnigmaWitch"
SITENAME = "The Witch's Appendix"

import datetime
FOOTER_YEAR = datetime.date.today().year
SITEDESCRIPTION = "The Witch's Appendix — carnet de recherche en cybersécurité : méthodologies, PoC et retours d'expérience, par EnigmaWitch."
SITEURL = ""

PATH = "content"
THEME = "themes/madchat"
OUTPUT_PATH = "output"

TIMEZONE = "Europe/Zurich"

DEFAULT_LANG = "fr"
DEFAULT_PAGINATION = 10

# Feed RSS
FEED_ALL_ATOM = "feeds/all.atom.xml"
CATEGORY_FEED_ATOM = "feeds/{slug}.atom.xml"

# URLs propres
ARTICLE_URL = "articles/{slug}/"
ARTICLE_SAVE_AS = "articles/{slug}/index.html"
PAGE_URL = "pages/{slug}/"
PAGE_SAVE_AS = "pages/{slug}/index.html"
ARCHIVES_URL = "archives/"
ARCHIVES_SAVE_AS = "archives/index.html"

# Affichage des catégories en « kebab-case » plutôt qu'avec les accents
CATEGORY_URL = "categorie/{slug}/"
CATEGORY_SAVE_AS = "categorie/{slug}/index.html"

# Pages de menu (fichiers .md à la racine de content/)
MENUITEMS = [
    ("Accueil", "/"),
    ("Archives", "/archives/"),
]
