#!/usr/bin/python
# -*- coding:utf-8 -*-

import sqlite3

conn = sqlite3.connect("my-py-sample.db")
conn.text_factory = str

cur = conn.cursor()
cur.execute("DELETE FROM user");

sql = "insert into user (" \
    " account_id" \
    " , emp_no" \
    " , email" \
    " , password" \
    " , user_nm" \
    " , user_nm_kn" \
    " , user_nm_en" \
    " , join_dt" \
    " , quit_dt" \
    " , version_no" \
    " , created_at" \
    " , created_by" \
    " , updated_at" \
    " , updated_by" \
    " , is_actived" \
    " ) values (" \
    " :account_id" \
    " , :emp_no" \
    " , :email" \
    " , :password" \
    " , :user_nm" \
    " , :user_nm_kn" \
    " , :user_nm_en" \
    " , :join_dt" \
    " , NULL" \
    " , 1" \
    " , CURRENT_TIMESTAMP" \
    " , 'init'" \
    " , CURRENT_TIMESTAMP" \
    " , 'init'" \
    " , '1'" \
    " );"


file = open("user.tsv", "r")
for line in file:
    arr = line.split("\t")
    print ("{user_nm}".format(user_nm=arr[1]).encode("utf-8"))
    param = {
        "account_id"   : arr[1]
        , "emp_no"     : arr[2]
        , "email"      : arr[3]
        , "password"   : arr[4]
        , "user_nm"    : arr[5]
        , "user_nm_kn" : arr[6]
        , "user_nm_en" : arr[7]
        , "join_dt"    : arr[8]
    }
    cur.execute(sql, param)

file.close()

conn.commit()
conn.close()
