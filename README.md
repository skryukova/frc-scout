# FRC Scouting Web App

This project is not yet ready for public usage! 
At the moment the readme is more of running notes, 
and will become something more useful as the project matures

## Prerequisites
This application is using the following technology stacks
* Angular 7 on the front end
* Python and Flask on the backend
  * Download Python 3.7.1 from here https://www.python.org/downloads/release/python-371/
  * Install pip
  * Install flask by running "pip install flask"

You should install those in your environment.

## Running in Debug
This will change as implementation gets containerized

### Running Backend
1) Navigate to the `backend` directory 
2) Set a couple of environment variables:  
`export FLASK_APP=frc_scout`  
`export FLASK_ENV=development`
3) Create subdirectory named `instance`
4) Create file, named `application.cfg`, in the new subdirectory with the following contents:  
`SECRET_KEY='dev'`  
`HOME_TEAM='<home team key>'`  
`AUTH_KEY='<auth key>'`  
where `AUTH_KEY` is the Blue Alliance API key, and `<home team key>` is the Blue Alliance key of the team that will use this app for scouting its needs. 
5) Start the server by running command `flask run`

### Running Front End
1) Navigate to the `frontend` directory 
2) Run `ng serve` command






 

