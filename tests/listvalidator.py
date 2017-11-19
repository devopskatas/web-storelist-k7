from bs4 import BeautifulSoup
import os, os.path
import sys

masterList = [] 
nextList = []

curfilePath = os.path.abspath(__file__)
curDir = os.path.abspath(os.path.join(curfilePath, os.pardir))
parentDir = os.path.abspath(os.path.join(curDir, os.pardir))
print(parentDir)

with open(parentDir + '/storelist.htm') as fp:
    soup = BeautifulSoup(fp, "html.parser")
    
    
    print("SECTIONS:")
    # for content in soup.find_all("ul", {"id":"grocerySections"}):
    #     if content.text:
    #         print (content.text)
    
    #print("MASTERLIST:")
    for content in soup.find_all("ol", {"id":"masterList"}):
        if content.text:
            masterList = content.text.splitlines()
    
    #print("NEXTVISIT:")
    for content in soup.find_all("ol",{"id":"nextList"}):
        if content.text:
            nextList = content.text.splitlines()

    #print("MISMATCH:")

#print(len(masterList))
#print(len(nextList))

diff = list(set(nextList) - set(masterList))
numDiffs = len(diff)

print(diff)

if numDiffs > 0:
    print('LIST INVALID ' + str(len(diff)))
    sys.exit(1)

sys.exit(0)