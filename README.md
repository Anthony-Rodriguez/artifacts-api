# Artifacts Back-end

Utilize Django's REST framework to create a database or artifacts. This repo is for the [back-end](https://git.heroku.com/dry-stream-85986.git) and speaks with the [front-end](https://github.com/Anthony-Rodriguez/artifacts) that was designed for this.

Checkout the [README](https://github.com/Anthony-Rodriguez/artifacts/blob/main/README.md) for instructions on getting set up with the deployed front-end.

## Set-up

1. Fork and clone this repository.
1. Change into this directory
1. Create and checkout a new branch.
1. Run `pipenv shell` to start up your virtual environment.
1. Run `pipenv install` to install dependencies.
1. Create a database for this api to interact with. (if you're not using artifacts)
  - Type psql to get into interactive shell
  - Run CREATE DATABASE "your_database_name";
  - Exit shell
1. Run `python manage.py makemigrations` when changing or adding models
1. Run `python manage.py migrate` to incorporate those changes
1. Run `atom .` to open the repo


This is set to run with the artifacts database.
## Routes


##### Authentication:
| Action | Method | Path |
| ----------- | ----------- | ----------- |
| Sign-Up | POST | `/sign-up/`
| Sign-In | POST  | `/sign-in/`
| Change-Password |  PATCH | `/change-password/`
| Sign-Out | DELETE | `/delete/`


##### Artifacts: (Authorized)
| Routes | Method | Path |
| ----------- | ----------- | ----------- |
| Create | POST | `/items`
| Index | GET | `/items`
| Show | GET | `/items/<int:pk>/`
| Update | PATCH | `/items/<int:pk>/`
| Delete | DELETE | `/items/<int:pk>/`

## Planning Story

I began with the user routes. Using a Django-template made that part easy. Next came the model for artifacts. I decided to use choice fields and a boolean field for some properties of the model. In our class, we hadn't gone into depth about those so I wanted to give it a shot. The choice field took a long time to figure out how to use correctly, but I was proud of the result. Curl-scripts were part of the testing process. Once I had CREATE completed, the rest was simple.

## Problem Solving Strategy

I was able to read the errors and fix most of the bugs.
I also utilized my cohort by asking them questions when I couldn't solve an issue.

## Technologies Used

- Python
- Django
- pipenv

## Unsolved Problems/Planned Updates

- This build is bug-free! (As far as I can tell)
- Planning to add new models based on the item model when user selects what category to create
- Planning to add option for images for the artifacts


## Entity Relationship Diagram

![ERD](https://i.imgur.com/VVKJO41.png)
