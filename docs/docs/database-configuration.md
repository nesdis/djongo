---
title: Database Configuration
permalink: "/database-configuration/"
---

The following options are supported in `settings.py`:

```python
    DATABASES = {
        'default': {
            'ENGINE': 'djongo',
            'ENFORCE_SCHEMA': True,
            'NAME': 'your-db-name',
            'HOST': 'host-name or ip address',
            'PORT': port_number,
            'USER': 'db-username',
            'PASSWORD': 'password',
            'AUTH_SOURCE': 'db-name',
            'AUTH_MECHANISM': 'SCRAM-SHA-1',
            'REPLICASET': 'replicaset',
            'SSL': 'ssl',
            'SSL_CERTFILE': 'ssl_certfile',
            'SSL_CA_CERTS': 'ssl_ca_certs',
            'SSL_CERT_REQS': 'ssl_cert_reqs',
            'READ_PREFERENCE': 'read_preference'
        }
    }
```

All options except `ENGINE`, `NAME` and `ENFORCE_SCHEMA` are the same those listed in the [pymongo documentation](http://api.mongodb.com/python/current/api/pymongo/mongo_client.html#pymongo.mongo_client.MongoClient).

Attribute | Value | Description
---------|------|-------------
ENGINE | djongo | The MongoDB connection engine for interfacing with Django.
ENFORCE_SCHEMA | True | (Default) Ensures that the model schema and database schema are exactly the same. Raises `Migration Error` in case of discrepancy. 
ENFORCE_SCHEMA | False | Implicitly creates collections. Returns missing fields as `None` instead of raising an exception.
NAME | your-db-name | Specify your database name. This field cannot be left empty.
  


