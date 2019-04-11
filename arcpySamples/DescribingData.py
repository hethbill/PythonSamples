'''
Basic arcpy script to Describe spatial data
Written by Elizabeth Tulanowski, GIS Instructor, Colorado State University
For Python 3.6
This script describes an input feature class and writes some properties out to a text file
It also makes use of simple error handling with a Try -Except statement
'''

## Be sure to set the variables below before trying to run!

# Import the arcpy module
import arcpy

## *************************************** ##
# Set some variables #  F I L L   T H E S E   I N
txtfile = r"C:\data\describeinfo.txt"       # Full path to txt file you want to create
arcpy.env.workspace = r"C:\Data\Colorado\FtCollins.gdb"  # Full path to workspace
data = "city"              # Name only of data to describe
## *************************************** ##

# Create and open output text file
outFile = file(txtfile, "w")

# Describe the data
dsc = arcpy.Describe(data)

#Write information out to the text file
outFile.write("***** Describe information for "+data+" *****\n\n")       
try:
    outFile.write(data+ " has " +dsc.shapetype+ " geometry\n")
except:
    outFile.write(data+ " is a "+dsc.datatype+" and has no shapetype\n")
outFile.write("The full path is " + dsc.catalogpath+ "\n")

# Close files
outFile.close()

print ("Finished")
