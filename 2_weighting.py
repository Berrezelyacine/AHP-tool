import arcpy
import numpy as np
import numpy
from array import array
import math
import os
#input matrix
fc = arcpy.GetParameterAsText(0)
#Ctreate a field named Weight to calculate on it
arcpy.AddField_management(fc,"Weight","DOUBLE")

#Listing fields name
fieldNameList = []
fields = arcpy.ListFields(fc)
for field in fields: 
	fieldNameList.append(field.name)

#Create a function to multiplicate the element of a list
def produit(liste):
	_produit = 1
	for i in liste:
		_produit = _produit * i
	return _produit

#Calculate the geometrical mean
with arcpy.da.UpdateCursor(fc, fieldNameList) as cursor:
	for row in cursor:
		row[-1]=produit(row[2:-1])**(1./len(row[2:-1]))
		cursor.updateRow(row)
# Convert to numpy array.  "test" is the field name
field = arcpy.da.TableToNumPyArray (fc, fieldNameList[-1], skip_nulls=True)
sum = field[fieldNameList[-1]].sum()

#calculate the Weight of each element of the list
with arcpy.da.UpdateCursor(fc, fieldNameList) as cursor:
	for row in cursor:
		row[-1]=row[-1]/sum
		cursor.updateRow(row)
if len(arcpy.GetParameterAsText(1)) <> 0:
	a = arcpy.GetParameterAsText(1)
	a=a.replace(",",".")
	a=float(a)
	with arcpy.da.UpdateCursor(fc, fieldNameList) as cursor:
		for row in cursor:
			row[-1]=row[-1]*a
			cursor.updateRow(row)
