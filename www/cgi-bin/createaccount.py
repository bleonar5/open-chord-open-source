#!/usr/bin/env python

import cgitb
cgitb.enable()

import cgi
form = cgi.FieldStorage()

name = form['_name'].value
username = form['_user'].value
pw = form['_pass'].value

import sqlite3

conn = sqlite3.connect('accounts.db')
c = conn.cursor()

c.execute('insert into users values (?, ?, ?)', (name, username, pw))
conn.commit()


# prints a minimal HTTP header
print 'Content-Type: text/html'
print

print '''<html>
	<head>
		<title>Open Chord Open Source</title>
	</head>'''
print'''	<body>
		<h1>Open Chord Open Source</h1>
'''
print "Hello, " + name + "."
print username
print pw

#print 'THE GREAT DIVIDE'
#for r in c.execute('select * from users;'):
#	name = r[0]
#	age = r[1]
#	image = r[2]
#
#	print '<h2>' + name + '</h2>'
#	print '<h2>' + str(age) + '</h2>'
#
#	print image
#	print '<hr/>'
conn.close()



print '''
	</body>
</html>'''
