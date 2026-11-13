Title: Bienvenue sur mon blog — premier article de test
Date: 2026-10-30 12:00
Category: divers
Tags: meta, test
Summary: Un premier article générique pour vérifier que tout fonctionne : Markdown, blocs de code, images et style rétro du thème.

Hello, monde_ ▮
===============

Ceci est un **article d'exemple** écrit en *Markdown*. Il sert uniquement à
valider le rendu du thème et du pipeline de publication. Tu peux le supprimer
dès que tu écris ton premier vrai article.

Un bloc de code, parce que c'est un blog technique
--------------------------------------------------

```python
#!/usr/bin/env python3
import hashlib


def sha256sum(path: str) -> str:
    """Empreinte SHA-256 d'un fichier — l'outil de base pour vérifier une intégrité."""
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(8192), b""):
            h.update(chunk)
    return h.hexdigest()


if __name__ == "__main__":
    print(sha256sum("exemple.bin"))
```

Insérer une image
-----------------

Les images vivent dans `content/images/` et se référencent avec le lien
`{static}` :

![Capture d'écran d'un scan nmap factice (exemple d'image)]({static}/images/exemple-schema.svg)

Une liste, pour la forme
------------------------

- écrire des articles en Markdown dans `content/articles/` ;
- pousser sur la branche `main` ;
- GitHub Actions construit et publie le site tout seul ▮

> « Trust, but verify. » — vérifie toujours, même (surtout) ce que ton propre
> outil te raconte.
