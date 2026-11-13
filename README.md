# The Witch's Appendix

Blog technique de cybersécurité, construit avec [Pelican](https://getpelican.com),
thème rétro « madchat » (ASCII art, CRT vert phosphore), déployé
automatiquement sur GitHub Pages via GitHub Actions.

## Écrire un article

1. Créer un fichier Markdown dans `content/articles/` :

   ```markdown
   Title: Titre de l'article
   Date: 2026-11-01 10:00
   Category: web
   Tags: xss, méthode
   Summary: Une phrase de résumé affichée sur la page d'accueil.

   Le corps de l'article en Markdown…
   ```

2. Pour les images : les déposer dans `content/images/` puis les référencer
   avec `![légende]({static}/images/mon-image.png)`.

3. Commit + push sur `main` → le site est reconstruit et publié tout seul.

## Aperçu local

```bash
python3 -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt
pelican --autoreload --listen   # http://localhost:8000
```

## Déploiement

Le workflow `.github/workflows/deploy.yml` construit le site et le publie sur
GitHub Pages à chaque push sur `main`.

### Mise en place (une seule fois)

1. Créer le dépôt sur GitHub et pousser ce projet :

   ```bash
   git init -b main
   git add .
   git commit -m "Première version du blog"
   git remote add origin git@github.com:<ton-user>/<repo>.git
   git push -u origin main
   ```

2. Dans les réglages du dépôt : **Settings → Pages → Build and deployment →
   Source : GitHub Actions**.

3. Si le dépôt ne s'appelle pas `<ton-user>.github.io`, le site est servi dans
   un sous-chemin — ajuster `SITEURL` dans `publishconf.py` (ex. `/blog-cyber`)
   ou via la variable d'environnement `SITEURL`.

## Structure

```
content/articles/   articles (Markdown)
content/pages/      pages statiques (à propos…)
content/images/     images des articles
themes/madchat/     thème rétro custom (templates Jinja2 + CSS)
output/             site généré (ne pas commiter)
```

## Avertissement

Ne publier des résultats de recherche (bug bounty, pentest) qu'en accord avec
la politique de divulgation du programme concerné.
