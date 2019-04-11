#Solution code for NR 426 Lab 3 - Part 1
# Self directed activity:
# Write the code to loop through and print names and # features of each
# polygon feature class in the CityOfSanAntonio geodatabase
print ("Starting script to list polygon feature classes........")
#Import modules
import arcpy

# Set environments and variables
#Set the workspace
arcpy.env.workspace = r"C:\Student\ProgrammingPro\Databases\CityOfSanAntonio.gdb"

#Tool needed to get the count of features in an FC:
##  arcpy.GetCount_management (in_rows)
##  result = arcpy.GetCount_management(lyrfile)
##  print('{} has {} records'.format(lyrfile, result[0]))

# 1. Create a list of FCs in the workspace and loop through it as a test
print ("Creating list of all FCs")

fcList = arcpy.ListFeatureClasses()
print ("There are "+ str(len(fcList))+ " feature classes in "+ arcpy.env.workspace)
for fc in fcList:
    print (fc)

print()   #Empty line

# 2. Create a list of polygon FCs in the workspace and loop through it
print ("Creating list of just polygon FCs")
polyList1 = arcpy.ListFeatureClasses("*", "Polygon")
for poly in polyList1:
    print (poly)
print ()   #Another empty line

# 3. Modify the loop to print both the name and the count
polyList2 = arcpy.ListFeatureClasses("*","Polygon")
for poly in polyList2:
    print(poly)
    num_feat = arcpy.GetCount_management(poly)
    print (num_feat[0])
    print ()  #Empty line

print()

# 4. Modify the output to make it readable
polyList = arcpy.ListFeatureClasses("*","polygon")
#print out how many polygon FCs are in the list to the user:
print ("There are "+ str(len(polyList))+ " polygon feature classes in "+ arcpy.env.workspace)

for poly in polyList:
    num_feat = arcpy.GetCount_management(poly)
    print("{0} has {1} features.".format(poly, num_feat))
    #print ()  #Empty line


print ("Script completed. Pat yourself on the back!")