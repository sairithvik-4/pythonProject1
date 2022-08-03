import re
txt = "use of the python in machine learning"
x=re.search("\s",txt)
print("the first white space is located after ",x)
