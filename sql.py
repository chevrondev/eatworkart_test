import sqlite3
with sqlite3.connect("eatworkart.db") as connection:
	c = connection.cursor()
	c.execute("""CREATE TABLE authors(fname TEXT, lname TEXT, description TEXT)""")
	c.execute('INSERT INTO authors VALUES ("David", "Smith", "Introduction to Jinja")')
	c.execute('INSERT INTO authors VALUES ("Stephen", "Johnson", "Advanced SQLite")')
	c.execute('INSERT INTO authors VALUES ("Miguel", "Grinberg", "Web Flask Developer")')
	c.execute('INSERT INTO authors VALUES ("Christopher", "Brown", "Web Databases")')
	c.execute('INSERT INTO authors VALUES ("Marc", "Jones", "Flask Jinja")')
	c.execute('INSERT INTO authors VALUES ("Marcus", "Miller", "My Database")')
	c.execute('INSERT INTO authors VALUES ("David", "Davis", "How to Develop Sites in Flask")')
	c.execute('INSERT INTO authors VALUES ("John", "Wilson", "Mastering Github")')