## Introduction

As I enjoy learning by building projects of my own, I went on with a personnal project that would lead me to explore a variety of tools, such as :

* Airflow
* DBT
* And, AWS.

## Project

Create a dashboard following the trends and ranking history of the top 1000 cryptocurrencies. 
The underlying data, pulled from on API and stored in a MYSQL database, would be updated on a daily basis.


## As of now 

* **Gecko.py** : Pulls data from coingecko.com's API.  
  - Top 7 trending cryptocurrencies, for the given day.
  - Top 1000 cryptocurrencies ranking, for the given day, with associated metrics.

* **db.py** : Calls gecko.py's functions and write down the data into a mysql database.

* **Dag.py** : Orchestrates those scripts on a daily basis, as of now.


## Next
* Use DBT for data transformation and orchestrate it with airflow. 
* Migrate to an Amazon EC2 instance.
* Build the dashboard.


