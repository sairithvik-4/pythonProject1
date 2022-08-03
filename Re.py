import re
txt = "use of the python in machine learning"
x=re.search("^use.*learnin$",txt)
if(x):
    print("YES! we have a match")
else:
    print("no match found")
