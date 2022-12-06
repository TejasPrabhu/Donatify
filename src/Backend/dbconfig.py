from asyncio import constants
import sys

# Constant Variables
if 'win' in sys.platform:
	constants = {
		"host": "localhost",
		"port": 3306,
		"user": "root",
		"password": "",
		"database": "donationsystem"
	}

else:
	constants = {
		"host": "127.0.0.1",
		"port": 8888,
		"user": "root",
		"password": "password",
		"database": "donationsystem"
	}
