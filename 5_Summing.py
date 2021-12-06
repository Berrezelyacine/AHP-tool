import arcpy
fc = arcpy.GetParameterAsText(0)
field=arcpy.GetParameterAsText(1)
value = arcpy.GetParameterAsText(2)
arcpy.AddField_management(fc,field,"DOUBLE")
arcpy.CalculateField_management(fc,field,value,"PYTHON_9.3")
arcpy.AddField_management(fc,"Absolute","DOUBLE")
with arcpy.da.SearchCursor(fc,field)as cursor:
	a= max(cursor)
for i in a:
	i=float(i)

value2='!'+field+'!'+'/'+str(i)
arcpy.CalculateField_management(fc,"Absolute",value2,"PYTHON_9.3")