# Application de gestion de projet par SoftDesk

SoftDesk est une API RESTful de suivi de problèmes liés à différentes plateformes (Site web, Android, IOS).

L'application permet essentiellement aux utilisateurs de créer divers projets, d'ajouter des utilisateurs à des projets spécifiques, de créer des problèmes au sein des projets et d'attribuer des libellés à ces problèmes en fonction de leurs priorités, de balises, etc.

Pour utiliser cette API, il est conseillé de se référer à sa [documentation](https://documenter.getpostman.com/view/15611753/UUxtFrBC).

## Prérequis

1. Installer [Python 3](https://www.python.org/downloads/).

2. Télécharger le programme via GitHub avec la commande ci-dessous ou en téléchargeant [l'archive](https://github.com/MaeRiz/OC_P10_SoftDesk/archive/refs/heads/master.zip).
```bash
git clone https://github.com/MaeRiz/OC_P10_SoftDesk.git
```

3. Créer un environnement virtuel et l'activer :
```cmd
python3 -m venv env
env\Scripts\activate
```

4. installer les modules :
```cmd
pip install -r requirements.txt
```

5. Faire les migrations:
```cmd
softdesk\manage.py makemigrations
softdesk\manage.py migrate
```
## Utilisation
1. Lancer le serveur [Django](https://www.djangoproject.com/):
```cmd
softdesk\manage.py runserver
```
2. L'API peut être utilisée de différente manière:
- avec l'application [Postman](https://www.postman.com/)
- par interface [curl](https://curl.se/)
- directement sur l'adresse du serveur: [http://localhost:8000/](http://localhost:8000/) (adresse par défaut)