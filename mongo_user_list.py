#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
import pymongo

username = 'appuser'
password = 'appuser'

client = pymongo.MongoClient( \
    'mongodb://%s:%s@127.0.0.1:28002/strz01t' \
        % (username, password) \
)

db = client.strz01t

coll = db.user

for data in coll.find():
    print ("%s %s %s %s" % (data["accountId"], data["empNo"], data["userNm"], data["email"]))

db.close
