from .base import *

DEBUG=True
ALLOWED_HOST=[]
DATABASES={
	'default':{
		'ENGINE':'sql_server.pyodbc',
		'NAME':'PFinal',
		'Trusted_Connection':'yes',
		'HOST':'localhost\SQLEXPRESS',
		'OPTIONS':{
			'driver':'SQL Server Native Client 11.0',
		}
	}
}
