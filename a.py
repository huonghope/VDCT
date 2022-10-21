from IssueComparison import IssueComparison
from ComparisonResultHolder import ComparisonResultHolder
from Issue import Issue
from AnalyzeToolConfig import AnalyzeToolConfig
from collections import OrderedDict
import xml.etree.ElementTree as ET
from xml.dom.minidom import parseString
import os
from pylab import *
from ScannerCWEMapping import ScannerCWEMapping
import csv
from ScannerIssueHolder import ScannerIssueHolder
from SecurityModel import SecurityModel
from SecurityModelComparision import SecurityModelComparision
from HTMLReport import HTMLReport
import shutil
import sys


def file_line_error_header(file_path):
    if os.path.exists(file_path):
        os.remove(file_path)
    sys.stdout = open(file_path,"w")
    print("File, Line, Error, CWE")
    sys.stdout = sys.__stdout__

if __name__ == '__main__':
  eTree = ET.parse('./manifest.xml')
  path = 'result.csv'
  root = eTree.getroot()

  file_line_error_header(path)
  for testcase in root:
    for file in testcase.iter("file"):
      fileName = os.path.basename(file.get("path"))
      if("w32" in fileName or "wchar" in fileName):
        continue
      if("CWE476" in fileName):
        print(fileName)
        if(file.findall("flaw")):
          for item in file.findall("flaw"):
            sys.stdout = open(path, "a")
            print(fileName, ",", item.get("line"), ",", item.get("name"), ",", item.get("name").split(":")[0])
            sys.stdout = sys.__stdout__
      
    