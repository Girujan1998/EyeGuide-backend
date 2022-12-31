# Setting Up Backend

This README should assist in setting up the backend instance on your local environment, from getting Django, Postgres and other applications working.

## Before working with backend architecture 

Before you work with backend code and when running the backend to get the server running, this should always be done in a virtual environment. This is done to prevent the OS intefering with the backend setup and packages, while also isolating our environment so we all work with the same type of environment. 

# Setting Up Environment

This README should assist in setting up your local machine for local Postgres database, Django backend server, NGORK tunnel, and React Native frontend.

## Software Download / Installation

Before we can run any local instances and have your environment up and running, you will need to download and install the following softwares:

### Postgres SQL

Postgres SQL is the database we are using to store our GPS data and will be what the Django server makes SQL queries to. We will be using Postgres SQL to create a local database instance running on our machine that will eventually connect to our Django server. Try to download v15 from https://www.postgresql.org/download/.

### pgAdmin4 

pgAdmin 4 is a software that allows us to interact with our local instance of Postgres SQL database using a UI instead of API calls or a terminal. This would allow us to imporve overall efficency, development, and testing as we can quickly query the database and make quick modifications to the data. Additionally, we could upload data in CSV files and export data more quickly compared to writing SQL queries and using API calls. You can download pgAdmin 4 from https://www.pgadmin.org/download/.

### Postman

Postman is a software that allows us to interact with our Django server using API calls and view the response with a better intergrated UI instead of using log / print messages and code to verify your API requests. You can download Postman from https://www.postman.com/downloads/.

### NGROK

NGROK is a software that creates a tunnel that allow you to access you localhost with a public URL that others can use. An example of this commonly seen is when you want someone remotley to view or test your changes that currently are running on your local machines. We are not able to share our localhost URL but we can use NGROK to create a tunnel to a public NGROK url that we can send to the person that will forward the user to your localhost. Additionally, we are using NGROK to avoid a network error when trying to do API calls with our localhost API URL and we can potentially use NGROK to temporarily get around deploying our project and use a local db and server instance running connected to a NGROK tunnel. You can download NGROK and how to set it up from here https://ngrok.com/download.

## Setting Up and Running Your Environemnt

To setup your environment and getting it up and running, ensure you have both the `Capstone` and `capstone-backend` repos cloned. 

1) Open Postgres SQL software and start the server

<img width="598" alt="Screen Shot 2022-12-31 at 2 51 28 AM" src="https://user-images.githubusercontent.com/24899889/210129679-6546ff93-d062-41d8-a869-f4ff7183aaee.png">

2) Open pgAdmin 4
3) Login with the main password (if you have not created one, make one and login)
4) Register a Postgres server with the following details

`General -> Name = PostgreSQL 15`
`Connection -> Host name/address = localhost`
`Connection -> Post = 5432`
`Connection -> Username = postgres`

5) Connect to your newly registered database
6) Open VS Code in your local `capstone-backend` repo and open a terminal in VS Code
7) Run the following `ngrok http 8000` and copy the `https` ngrok URL and replace the URL in both .env files (ensure you don't add the https part for certain variables and add it for the other ones)
8) Open another terminal in VS Code and run `source capstone-env/bin/activate` to start up a virtual env terminal (when running code for the Django backend, ensure you are running in a virtual machine to avoid issues due to your own machine. 
9) Run `npm install -r requirements.txt`
10) Run `python manage.py runserver` to start up the Django server on your local machine
11) 


5) 
