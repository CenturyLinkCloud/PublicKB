#!/usr/bin/python

import sys
sys.path.append('../src/')
import clc


ALIAS = 'xxx'
USERS = [
	{'fn': 'firstname', 'ln': 'lastnamde', 'email': 'email', 'username': 'username', 'roles': ['Account'] },
]

clc._V1_API_KEY = 'xx'
clc._V1_API_PASSWD = 'xx'


for user in USERS:
	print clc.User.CreateUser(ALIAS, user['username'], user['email'], user['fn'], user['ln'], roles=user['roles'])['UserName']

