#Sample script to demonstrate 4 ways to combine objects
#ie, into a string or print statement

# Refer to the Python Scripting for ArcGIS Pro

'''
You want to build this statement from these 3 variables
The full path is C:\Data\Python\roads.shp and has _ characters
'''
folder = r"C:\Data\Python"
path =  "roads.shp"
length = len(path)

# 1:  concatenate with +
print ("Method #1:")
msg = "The full path is " + folder + "\\" + path + " and has " + str(length) + " characters"
print (msg)
#or use os to join the folder to the path
import os
msg2 = "The full path is " + os.path.join(folder,path) + " and has " + str(length) + " characters"
print (msg2)


#2:  .format and {}
msg3 = "The full path is {0} and has {1} characters".format(os.path.join(folder, path), length)
print ("\nMethod #2:")
print (msg3)


#3:  f-string
fullpath = os.path.join(folder, path)
msg4 = f"The full path is {fullpath} and has {length} characters"
print ("\nMethod #3:")
print (msg4)

#4:  % as placeholder
msg5 = "The full path is %s and has %i characters"%(fullpath, length)
print ("\nMethod #4:")
print (msg4)