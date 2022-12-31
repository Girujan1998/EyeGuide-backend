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
