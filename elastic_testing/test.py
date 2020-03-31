from datetime import datetime
from elasticsearch import Elasticsearch

es = Elasticsearch('127.0.0.1', port=9205, timeout=60, max_retries=10, retry_on_timeout=True)

doc = {
    'author': 'cag',
    'text': 'Elasticsearch: works2',
    'timestamp': datetime.now(),
}

res = es.index(index="test-index", doc_type='tweet', id=2, body=doc)
print(res['result'])

res = es.get(index="test-index", doc_type='tweet', id=2)
print(res['_source'])

es.indices.refresh(index="test-index")

res = es.search(index="test-index", body={"query": {"match_all": {}}})
result = res['hits']['total']
print("Got {} Hits:".format(result))
for hit in res['hits']['hits']:
    print("%(timestamp)s %(author)s: %(text)s" % hit["_source"])