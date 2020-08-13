from elasticsearch import Elasticsearch
import os

pwd = os.environ.get('ELASTIC_PWD')
cloud_id = os.environ.get('CLOUDID')

Client = Elasticsearch(cloud_id=cloud_id, http_auth=('elastic', pwd))
