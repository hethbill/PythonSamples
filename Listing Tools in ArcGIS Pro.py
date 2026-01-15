'''
Fun sample code to list every tool from every toolbox
to get a total number of tools in ArcGIS
Written by E. Tulanowski, revised January 2026
'''

#imports
import arcpy

#list toolboxes
toolboxes = arcpy.ListToolboxes()

print (f"There are {len(toolboxes)} toolboxes in ArcGIS Pro\n")
print ("The toolboxes are:")

totaltools = 0  #instantiate a variable to hold the number of tools

for toolbox in toolboxes: #loop through each toolbox
    print("\t" + toolbox)
    alias = toolbox.split('(')[1][:-1]
            #Gets just the alias off the end of the toolbox name

    # Now list each tool in each toolbox
    tools = arcpy.ListTools(f"*_{alias}")
    print(f"\t {toolbox} has {len(tools)} tools:")
    totaltools = totaltools+len(tools)
    #for tool in tools:
        #print("\t\t" + tool)
    print()

# Use GetInstallInfo to return a dictionary containing version and license info
d = arcpy.GetInstallInfo()
#Commenting out, but this returns all the install info values:
# for key, value in list(d.items()):
#     # Print a formatted string of the install key and its value
#     print("{:<13} : {}".format(key, value))


print (f"Total tools available in ArcGIS Pro "
       f"{d['Version']}, {d['LicenseLevel']}:\n {(totaltools)} ")
