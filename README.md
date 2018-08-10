# [`Apache Superset` Projects](https://superset.incubator.apache.org)   

## [`Superset` Installation and Initialization](https://superset.incubator.apache.org/installation.html#superset-installation-and-initialization)
1. Install superset  
`> pip install superset`

2. Create an admin user (you will be prompted to set username, first and last name before setting a password)  
`> fabmanager create-admin --app superset`

3. Initialize the database
`> superset db upgrade`

4. Load some data to play with
`> superset load_examples`

5. Create default roles and permissions
`> superset init`

6. To start a development web server on port 8088, use -p to bind to another port
`> superset runserver -d`

## [Tutorial](https://superset.incubator.apache.org/tutorial.html)  
* **[Weather Data](https://github.com/dylburger/noaa-ghcn-weather-data)**  
* **[PostgreSQL Sample Data](https://wiki.postgresql.org/wiki/Sample_Databases)**  
* **[SQLAlchemy](http://www.sqlalchemy.org/)**
