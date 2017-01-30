# import urllib.request
import re


# fp = urllib.request.urlopen("http://www.basketball-reference.com/leaders/\
#         pts_career.html")

# mybytes = fp.read()
# note that Python3 does not read the html code as string
# but as html code bytearray, convert to string with
# mystr = mybytes.decode("utf8")

# fp.close()

# print(mystr)

line = "Cats are smarter than dogs"

searchObj = re.search(r'(.*) are (.*?) .*', line, re.M | re.I)

if searchObj:
    print("searchObj.group() : ", searchObj.group())
    print("searchObj.group(1) : ", searchObj.group(1))
    print("searchObj.group(2) : ", searchObj.group(2))
else:
    print("Nothing found!!")
