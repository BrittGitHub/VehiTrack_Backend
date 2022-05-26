## VehiTrack
Trying to find an easy way to track all of your household vehicles' maintenance costs? VehiTrack is the solution to meet your needs! This application allows users to create an account, store their household vehicles, and track the maintenance cost on each vehicle!

## Deployed Application

[Link]() to deployed application

[Link]() to deployed Heroku remote server.

[Link](https://github.com/BrittGitHub/VehiTrack_Client) to Client repository

## User Stories
* As a user, I want to be able to create an account.
* As a user, I want to be able to sign in.
* As a user, I want to be able to sign out of my account.
* As a user, I want to be able to change my password.
* As a user, I want to be able to add a new vehicle.
* As a user, I want to be able to update a vehicle.
* As a user, I want to be able to delete a vehicle.
* As a user, I want to be able to add a maintenance memo/note on a particular vehicle.
* As a user, I want to be able to update a maintenance memo/note that I created on a particular vehicle.
* As a user, I want to be able to delete a maintenance memo/note that I created on a particular vehicle.

## Technologies Used

Utilized the following to build a full-stack application:
* Django
* Python
* React.js/JSX
* Node.js

Other technologies used:
* Bootstrap
* Sass
* Javascript
* Axios
* Heroku for deployment of API

## ERD

To view an ERD of the app, [click here](/VehiTrack_ERD.png).

## API Routes

| HTTP Method   | URL Path        | Action           | CRUD     |
|:--------------|:----------------|:-----------------|----------|
| GET           | /vehicles       | index or list    | `R`ead   |
| GET           | /vehicles/`:id` | show or retrieve | `R`ead   |
| POST          | /vehicles       | create           | `C`reate |
| PATCH         | /vehicles/`:id` | update           | `U`pdate |
| DELETE        | /vehicles/`:id` | delete           | `D`elete |


| HTTP Method   | URL Path                        | Action           | CRUD     |
|:--------------|:--------------------------------|:-----------------|----------|
| POST          | vehicles/:id/maintenances       | create           | `C`reate |
| PATCH         | vehicles/:id/maintenances/`:id` | update           | `U`pdate |
| DELETE        | vehicles/:id/maintenances/`:id` | delete           | `D`elete |

## Planning

* Began by writing out user stories
* From the user stories, I created an ERD to map out the necessary entities
* After the ERD was constructed, I designed a wireframe for which the flow of the application should follow

## Future iterations
* Allow users update maintenance memos created on the vehicles
* Display a totals section to show to total cost of maintenance per vehicle

## Setup and Installation
To build more onto this app on your own, simply `fork` and `clone` this repository to your local environment. Then, start a local instance of the server run  `python manage.py runserver`. Your server is now running at `http://127.0.0.1:8000/`
