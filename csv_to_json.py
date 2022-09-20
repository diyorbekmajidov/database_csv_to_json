import read_data
import json
from tinydb import TinyDB 
db = TinyDB('db.json')
def csv_to_json(data:list)-> None:
    """
    Given csv list turn into tinydb database

    Arguments:
        data(list): paramenter
    Returns:
        None
    """
    mobile=db.table('Mobile')
    for i in data[1:len(data)]:
        mobile.insert(({'model':i[1], 'company':i[2], 'price':i[3]}))
m=read_data.read_csv('specifications.csv')

z=csv_to_json(m)
print(z)