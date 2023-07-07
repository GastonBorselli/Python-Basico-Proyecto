#hay 3 tipos de modulos
#modulos propios, de internet o modulos de python

import datetime
print(datetime.date.today())
print(datetime.timedelta(minutes=70))

from datetime import timedelta, date
print(date.today())

# import funcionMat

# funcionMat.sumar(10,2)
# funcionMat.restar(5,3)

from funcionMat import sumar, restar

sumar(10,10)
restar(10,5)