#!/usr/bin/python
#-*- coding:utf-8 -*-

import yaml
import psycopg2
import psycopg2.extras
import re

#------------------------------------------------------------------------------
# 社員クラス
#------------------------------------------------------------------------------
class Employees:
    def __init__(self, id, account_id, email, passwd, emp_no, ename, jname, hire_date, fire_date, reg_date, mod_date, permissions):
        self.id = id
        self.account_id = account_id
        self.email = email
        self.passwd = passwd
        self.emp_no = emp_no
        self.ename = ename
        self.jname = jname
        self.hire_date = hire_date
        self.fire_date = fire_date
        self.reg_date = reg_date
        self.mod_date = mod_date
        self.permissions = permissions


# yaml読み込み
# pip install pyyaml
ymlf = open('psycopg2_and_class.yml', 'r')
yml = yaml.load(ymlf)
print("-- yml contents --\nhost={}\nport={}\ndbname={}\nuser={}\npassword={}".format(
    yml['dbinfo']['host'],
    yml['dbinfo']['port'],
    yml['dbinfo']['dbname'],
    yml['dbinfo']['user'],
    yml['dbinfo']['password']))
print('------------------')

conn = psycopg2.connect('postgresql://{user}:{password}@{host}:{port}/{dbname}'
    .format(
        host=yml['dbinfo']['host'],
        port=yml['dbinfo']['port'],
        dbname=yml['dbinfo']['dbname'],
        user=yml['dbinfo']['user'],
        password=yml['dbinfo']['password']
    ))
cur1 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
cur1.execute('SELECT * FROM t_employees')

employees = []

for row in cur1:
    cur2 = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    sql = 'SELECT r.name AS role_name FROM t_permission AS p' \
          ' INNER JOIN t_role AS r ON r.id = p.role_id' \
          ' WHERE p.user_id = %s'
    param = [row['id']]
    cur2.execute(sql, param)
    permissions  = []
    for row2 in cur2:
        permissions.append(row2['role_name'])
    employees.append(Employees(
        row['id'],
        row['account_id'],
        row['email'],
        row['passwd'],
        row['emp_no'],
        row['ename'],
        row['jname'],
        row['hire_date'],
        row['fire_date'],
        row['reg_date'],
        row['mod_date'],
        permissions))

# ソート
employees = sorted(employees, key=lambda emp : (emp.hire_date, emp.ename))

# フィルタ (名前が E1 or E2)
employees = filter(lambda emp : re.match('(.*E1$|.*E2$)', emp.ename), employees)

for emp in employees:
    print("{}\t{}\t{}\t{}".format(emp.emp_no, emp.account_id, emp.ename, emp.permissions))

conn.close()
