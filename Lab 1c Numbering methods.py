# Example code to show 3 three ways to number a list


FourCorners = ["Colorado", "New Mexico", "Utah", "Arizona"]
   

##  Using Enumerate
print ("Using enumerate")
for index, value in enumerate(FourCorners, 1):
    print(f'{("{}. {}".format(index, value))} - {str(len(value))}')

## Using a counter variable
c = 1
print ("\nUsing a counter variable:")
for x in FourCorners:
    print (f"{c}. {x} - {len(x)}")
    c += 1

print ("\n Using the index number")
## Using the index
for x in FourCorners:
    print (f"{FourCorners.index(x)+1}. {x} - {len(x)}")
