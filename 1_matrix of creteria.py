# Name: CreateTable_Example2.py
# Import system modules
import arcpy
import numpy as np
import numpy
from array import array
import math
import os
# Set workspace
out_path = arcpy.GetParameterAsText(0)
# Create a geodatabase
GDB_name = arcpy.GetParameterAsText(1)
GDBname = GDB_name + ".gdb"
arcpy.CreateFileGDB_management(out_path, GDBname)
GDBpath = out_path+"\\"+GDBname
# Create Table
Tablename = arcpy.GetParameterAsText(2)
arcpy.CreateTable_management(GDBpath, Tablename)
#Listing fields name
listlyr=arcpy.GetParameterAsText(4)
listlyr=listlyr.split(';')
#Add a field
Tablepath=GDBpath+"\\"+Tablename
arcpy.AddField_management(Tablepath,"layername","TEXT")
#Add more fields
n=0
for lyr in listlyr:
        arcpy.AddField_management(Tablepath,lyr,"DOUBLE")
        n=n+1
#Add rows
cursor = arcpy.da.InsertCursor(Tablepath, ["layername"])
for lyr in listlyr:
        cursor.insertRow([lyr])

del cursor
#Create domaine
domName = "AHPdomaine"
arcpy.CreateDomain_management(GDBpath, domName, "domain_AHP", "DOUBLE", "CODED")
#Create domaine dictionary
domDict = {"0,5":"1/2", "0,333": "1/3", "0,25": "1/4", "0,20": "1/5", "0,1666": "1/6", "0,142857": "1/7", "0,125": "1/8", "0,11111": "1/9", "0,1": "1/10", "1":"1", "2": "2", "3": "3", "4": "4", "5": "5", "6": "6", "7": "7", "8": "8", "9": "9", "10": "10"}
#Add domDic to domaine
for code in domDict:        
    arcpy.AddCodedValueToDomain_management(GDBpath, domName, code, domDict[code])
n=0
for lyr in listlyr:
	arcpy.AssignDomainToField_management(Tablepath, lyr, domName)
        n=n+1
#Classifing domaine by ascending orde 
arcpy.SortCodedValueDomain_management(GDBpath, domName, "CODE", "ASCENDING")