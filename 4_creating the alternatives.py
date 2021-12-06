import arcpy
fc = arcpy.GetParameterAsText(0)
field=arcpy.GetParameterAsText(1)
str=arcpy.GetParameterAsText(2)
exp=arcpy.GetParameterAsText(3)
mtrx=arcpy.GetParameterAsText(4)
value=arcpy.GetParameterAsText(5)
if len(field)==0:
	field=str
arcpy.AddField_management(fc,field,"DOUBLE")
arcpy.SelectLayerByAttribute_management(fc, 'NEW_SELECTION',exp)
arcpy.CalculateField_management(fc,field,value,"PYTHON_9.3")
