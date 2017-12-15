#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect("my-py-sample.db")

cur = conn.cursor()

for row in cur.execute("SELECT * FROM user ORDER BY user_id;"):

    print (u"{user_id}\t{account_id}\t{emp_no}\t{email}\t{password}\t{user_nm}\t{user_nm_kn}\t{user_nm_en}\t{join_dt}".format( \
        user_id=row[0] \
        , account_id=row[1] \
        , emp_no=row[2] \
        , email=row[3] \
        , password=row[4] \
        , user_nm=row[5] \
        , user_nm_kn=row[6] \
        , user_nm_en=row[7] \
        , join_dt=row[8]).encode("utf-8"))

conn.close()
