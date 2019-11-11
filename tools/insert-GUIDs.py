# -*- coding: utf-8 -*-
"""
Spyder Editor

Insert GUID ids into manifest schema

"""
import os
import uuid

# decus10-manifest.xml
# tops10-tape-manifest.xml
# <decusProject>
# <tape>

directory = "C:\\Users\\username\Desktop\\Guid Experiment\\"
inputFileName = "tops10-tape-manifest.xml"
outputFileName = "tops10-tape-manifest.xml.new"

element = "<tape>"

with open(directory + inputFileName, 'r') as fileIn:
    fileOut = open(directory + outputFileName, 'w+')
    lines = fileIn.readlines()
    for line in lines:
        if element in line:
            guid = str(uuid.uuid4())
            newLine = line[0:len(line)-2] + ' id="' + guid + '">' + '\n'
        else:
            newLine = line
        print(newLine, end="")
        fileOut.write(newLine )
    fileOut.close()
