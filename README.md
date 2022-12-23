EpicEvents - CRM sécurisé pour la gestion d'évenements... EPIC !

---

Epic Events est une société d'organisation d'événements épics. Cette application sert de gestion de relation clients.
Dévelopée avec le framework Django ORM ainsi que Django REST pour la partie de l'API.

Epic Events est divisée en deux applications :

- l'application Epic Events, développée avec Django ORM (donc la partie CRM d'Epic Events).
- l'application Epic Events API, développée avec Django REST (donc la partie back-end qui permet à ses utilisateurs d'accèder à la base de données via des endpoints).


#### Pour utiliser l'API, merci de suivre la [documentation Postman](https://documenter.getpostman.com/view/19936781/2s8Z6u5FHS) dédiée à cette partie.

---

### Prérequis :

    Python 3
    Environnement virtuel
    pipfile

#### Comment installer l'environnement virtuel ?

#### Dans votre terminal :

    pip install pipenv

    pipenv shell

    pipenv install

Pour plus de précisions : https://pypi.org/project/pipenv/

---

## Comment exécuter le serveur de l'application *Epic Events* ?
Dans votre terminal :

_assurez-vous d'être à la racine de votre projet_

> cd .\epiceventsproject\

Faites les migrations !

> py -m manage makemigrations
> py -m manage migrate

Vous pourrez lancer le serveur avec la commande suivante :

> py -m manage runserver

Vous devriez voir dans le terminal : _`Starting development server at http://127.0.0.1:8000/`_

8000 correspond au port de votre serveur local

## Création d'un super utilisateur

Afin de pouvoir accèder au tableau de bord Django d'administration de notre application Epic Events,
nous allons devoir créer un super utilisateur qui fera office de "manager" (ou admin), membre de l'équipe de gestion.

Pour cela, tappez dans votre terminal (toujours à la racine de votre projet) :

> py -m manage createsuperuser

Vous pourrez ensuite suivre les instructions dans votre terminal et n'oubliez pas garder quelque part vos identifiants !

### Connexion Django Epic Events admin

Rendez-vous sur ce lien : http://127.0.0.1:8000/management-admin/

Entrez vos identifiants, ... bravo vous êtes connecté !

### Règles utilisateurs

Seuls les membres de l'équipe de gestion pourront accéder au panneau d'administration.

Pour les autres types d'utilisateurs, les accès seront accessibles via des points de terminaisons.
Merci de suivre les instructions fournies dans la [documentation Postman de l'API](https://documenter.getpostman.com/view/19936781/2s8Z6u5FHS).

---
