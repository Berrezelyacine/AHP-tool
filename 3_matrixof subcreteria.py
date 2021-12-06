import arcpy
fc = arcpy.GetParameterAsText(0)
field=arcpy.GetParameterAsText(1)
listlyr=arcpy.GetParameterAsText(2)
f=arcpy.Describe(fc)
f=f.path
a=f+"\\"+field
arcpy.CreateTable_management(f,field)
listlyr=listlyr.split(';')
arcpy.AddField_management(a,"layername","TEXT")
for lyr in listlyr:
	arcpy.AddField_management(a,lyr,"DOUBLE")
cursor = arcpy.da.InsertCursor(a, ["layername"])
for lyr in listlyr:
        cursor.insertRow([lyr])
del cursor

domains=arcpy.da.ListDomains(f)
for domain in domains:
	domname=domain.name
for lyr in listlyr:
	arcpy.AssignDomainToField_management(a, lyr, domname)