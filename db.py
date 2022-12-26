import mysql.connector
from Gecko import *
from sqlalchemy import types, create_engine

# MySQL Connection
MYSQL_USER 	= 'root'
MYSQL_PASSWORD 	= "Password" 
MYSQL_HOST_IP 	= '127.0.0.1'
MYSQL_PORT	= '3306'
MYSQL_DATABASE	= 'crypto'

engine = create_engine('mysql+mysqlconnector://'+MYSQL_USER+':'+MYSQL_PASSWORD+'@'+MYSQL_HOST_IP+':'+MYSQL_PORT+'/'+MYSQL_DATABASE, echo=False)



def Markets ():
    cf = get_all_market(4)
    cf.drop('roi',1,inplace=True)
    cf.to_sql(con=engine,name='market_ranking',if_exists='append',index=False)
    
def trends ():
    df = trending()
    df.to_sql(con=engine,name='trending',if_exists='append',index=False)



if __name__ == '__main__':
    Markets()
    trends()

    
