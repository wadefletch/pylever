#Python Lever Postings API Client
This is a Python 3 client for the [Lever](https://lever.co) [Postings API](https://github.com/lever/postings-api/blob/master/README.md). 
It is extremely simple, as the API is in v0 and has but three public endpoints. 

## Installation
```bash
$ git clone <INSERT LINK TO THIS REPO>
$ cd pylever
$ python setup.py install
```

## Quickstart
```python
from pylever import Lever
lever = Lever('YOUR API KEY HERE', 'YOUR SITE NAME HERE')
for posting in Lever.list_postings(limit=6):
    print(posting.text)
```