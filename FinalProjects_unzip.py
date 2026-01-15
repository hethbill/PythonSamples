# Script to loop through final project folder and unzip anything that's zipped.
# Needs to name it with the first part of the filename up to the _


print("***Starting zip file basics script.......\n")
import zipfile, os, sys

dir = r"N:\Classes\workspace\Tulanowski\grading\NR427 final project"   ## Replace with your folder path

#Loop through each file in the folder, for each file, check if zip file, unzip and set name
for filename in os.listdir(dir):
    # Check if it's a file (not a directory)
    #if os.path.isfile(os.path.join(dir, filename)):
    #     print(filename)

    if zipfile.is_zipfile(os.path.join(dir, filename)):
        print (os.path.join(dir, filename) +" needs to be unzipped")
        outdir = os.path.join (dir, filename.split("_")[0])
        print(outdir)
        zippath = os.path.join(dir, filename)
    # #Extract all the files from the zip file. Will go into the current working directory
    # # So let's set the cwd first:
        print ("Creating a new folder for the extracted files and setting CWD to it...")
        newcwd =os.path.join(dir, outdir)
        #
        # #If that folder doesn't already exist, create it here:
        if not os.path.exists(newcwd):
            os.mkdir(newcwd)
            print ("Created the new folder")
        #
        # #Change the current working directory to that new folder:
        os.chdir(newcwd)
        #
        # #Finally, extract all the files from the zip file:
        # print ("Extracting the files from {0} to {1}".format(myzip,newcwd))
        zipref = zipfile.ZipFile(zippath, 'a')
        try:
            zipref.extractall(outdir)
            print ("unzipped "+ filename.split("_")[0][:-4])
        except:
            print("Couldn't extract it")
    #


    else:
        print (filename + " doesn't need to be unzipped")



# myzip = r"____.zip"   ## Replace with your zip filename
#
# zippath =                  ## Type the code to join the path and file name
#
# zip = zipfile.ZipFile(zippath, 'a') #Open in r, w, or a mode for read, write, append
#
# #Test if the input file is even a zipfile:
# if zipfile.is_zipfile(zippath):
#     print ("Yes, {0} is a valid zipfile, carry on with your extracting".format(zippath))
# else:
#     print ("Sorry, {0} is not a valid zip file, please choose another one".format(zippath))
#     sys.exit()
#
# #Report the contents of the zipfile:
# print("These are the contents of that zip file, poorly formatted:")
# print(zip.namelist())
#
# print("These are the contents of that zip file, in a nice list:")
# for z in zip.namelist():
#     print (z)
#
# #Use zip.printdir() to get a tabified report of the zip file's contents:
# print ("\nThese are the contents of that zip file, very nicely formatted:")
# print(_______)    ## Replace with the correct method
# print()
#
#
# #Add a new file into the zip file:
# newfile = r"C:\Student\Lesson 2 CSVs Dates Files\CSUlocations.csv"
# #zip.write(newfile)
#
#
# #Read files in the zip file without extracting:
# print ("Reading the contents of just one file...")
# print (zip.read("Campsite_Data.txt")) #This could be a txt or csv, then used directly in other operations
#
#
#
# #Extract all the files from the zip file. Will go into the current working directory
# # So let's set the cwd first:
# print ("Creating a new folder for the extracted files and setting CWD to it...")
# newcwd =os.path.join(dir, "scratch")
#
#
#
# #If that folder doesn't already exist, create it here:
# if not os.path.exists(newcwd):
#     os.mkdir(newcwd)
#     print ("Created the new folder")
#
# #Change the current working directory to that new folder:
# os.chdir(newcwd)
#
# #Finally, extract all the files from the zip file:
# print ("Extracting the files from {0} to {1}".format(myzip,newcwd))
# try:
#     zip.extractall()
# except:
#     print("Couldn't extract it")
#
#
# #Be sure to close the zip file at the end:
# zip.close()
#
# print ("Zip file basics script completed...")
