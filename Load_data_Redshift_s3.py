import psycopg2
import boto3 as boto
conn_string = "dbname='***' port='5439' user='***' password='***' host='mycluster.***.redshift.amazonaws.com'"
client = boto3.client('redshift')
con = psycopg2.connect(conn_string);
s3 = boto.resource('s3')
sql = COPY <table_name> from 's3://bucket/mydata' access_key_id <access_key_id> secreat_access_key '<secreat access_key>'
upload = client.excute(sql)
print("table loaded with the data")
