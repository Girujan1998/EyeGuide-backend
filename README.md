# About Eye Guide Backend

This repo contains the backend code for the Eye Project to interact with the Postgres SQL database and modify data before passing it to the frontend. The frontend of this repo can be found here - https://github.com/Girujan1998/EyeGuide

## Software's Used

Before we can run any local instances and have your environment up and running, you will need to download and install the following softwares:

### Postgres SQL

Postgres SQL is the database we are using to store our GPS data and will be what the Django server makes SQL queries to. We will be using Postgres SQL to create a local database instance running on our machine that will eventually connect to our Django server. Try to download v15 from https://www.postgresql.org/download/.

### pgAdmin4 

pgAdmin 4 is a software that allows us to interact with our local instance of Postgres SQL database using a UI instead of API calls or a terminal. This would allow us to imporve overall efficency, development, and testing as we can quickly query the database and make quick modifications to the data. Additionally, we could upload data in CSV files and export data more quickly compared to writing SQL queries and using API calls. You can download pgAdmin 4 from https://www.pgadmin.org/download/.

### Postman

Postman is a software that allows us to interact with our Django server using API calls and view the response with a better intergrated UI instead of using log / print messages and code to verify your API requests. You can download Postman from https://www.postman.com/downloads/.

### NGROK

NGROK is a software that creates a tunnel that allow you to access you localhost with a public URL that others can use. An example of this commonly seen is when you want someone remotley to view or test your changes that currently are running on your local machines. We are not able to share our localhost URL but we can use NGROK to create a tunnel to a public NGROK url that we can send to the person that will forward the user to your localhost. Additionally, we are using NGROK to avoid a network error when trying to do API calls with our localhost API URL and we can potentially use NGROK to temporarily get around deploying our project and use a local db and server instance running connected to a NGROK tunnel. You can download NGROK and how to set it up from here https://ngrok.com/download.
