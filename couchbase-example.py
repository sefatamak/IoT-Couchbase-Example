#-*- coding: utf-8 -*-
from couchbase.cluster import Cluster
from couchbase.cluster import PasswordAuthenticator
from couchbase.bucket import Bucket
from numpy import loadtxt


def connect_bucket():
	cluster = Cluster('couchbase://localhost')
	authenticator = PasswordAuthenticator('admin', 'admin123')
	cluster.authenticate(authenticator)
	bucket = cluster.open_bucket('thirdbucket')
	return bucket

def insert_data(get_data):
	counter = 0
	for data in get_data:
		counter += 1
		data_dict = {
						"object_id": "object1", # changeable
						"value1": {
							"value2": data[0],
							"value3": data[1],
							"value4": data[2],
							"value5": data[3],
							"value6": data[8]
						},
						"value7": data[4],
						"value8": {
							"value9": data[5],
							"value10": data[6]
						},
						"value11": data[7],
						"authorities" : ['user1','user2']
					}
		bucket.upsert('sensordata{}'.format(counter), data_dict)

if __name__ == "__main__":
	bucket = connect_bucket()
	for i in range(1,3):
		get_data = loadtxt('data{}.txt'.format(i), dtype='float', comments='#')
		get_data = list(get_data)
		insert_data(get_data)