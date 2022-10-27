from cProfile import label
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
import sys
import random
import numpy as np
import re

class Issues(object):
  def __init__(self, code, label, file):
    self.file = file 
    self.code = code
    self.label = label
    
def readManifestFile(self,root):
		flawMap = dict()
		for testcase in root:
			issueList = []
			for file in testcase.iter("file"):
				fileName = os.path.basename(file.get("path")).lower()
				if("w32" in fileName or "wchar" in fileName):
								continue
				if(file.findall("flaw")):
					for item in file.findall("flaw"):
						newIssue = Issue(fileName,item.get("name").split(":")[0], item.get("line"))
						issueList.append(newIssue)

				issueComparision = IssueComparison(fileName)
				issueComparision.addExistingIssues(issueList)
				flawMap[fileName] = issueComparision
		return flawMap
    
def remove_comments(string):
    pattern = r"(\".*?\"|\'.*?\')|(/\*.*?\*/|//[^\r\n]*$)"
    regex = re.compile(pattern, re.MULTILINE|re.DOTALL)
    def _replacer(match):
        if match.group(2) is not None:
            return "" 
        else: 
            return match.group(1) 
    return regex.sub(_replacer, string)
      
def removeComments(string):
  string = re.sub(re.compile("/\*.*?\*/",re.DOTALL ) ,"" ,string) # remove all occurrences streamed comments (/*COMMENT */) from string
  string = re.sub(re.compile("//.*?\n" ) ,"" ,string) # remove all occurrence single-line comments (//COMMENT\n ) from string
  return string 
if __name__ == '__main__':
  
  eTree_issues = ET.parse('./existingIssues.xml')
  path_result = 'bad_code.csv'
  
  root_isssues = eTree_issues.getroot()
  
  f = open(path_result, 'w')
  writer = csv.writer(f)
  writer.writerow(["file", "code", "label"])

  existingIssuesFile ='manifest.xml'
  eTree = ET.parse(existingIssuesFile)
  root = eTree.getroot()
  flawMap = readManifestFile(root)
  
  # flawMap = self.readManifestFile(root)
  
  list_line_issues = []            
  for files in root_isssues:
    for file in files.iter("file"):
      fileName = os.path.basename(file.get("path"))
      if("w32" in fileName or "wchar" in fileName):
        continue
      # if("CWE758" in fileName):
      if(file.findall("issue")):
        for item in file.findall("issue"):
          path = file.get("path")
          with open(path, "r") as code:
            lines = code.readlines()
            count = 0
            list_lines = ""
            for line in lines:
              count +=1
              startLine = int(item.get("startLine")) 
              endLine = item.get("endLine") 
              endLine = int(endLine) if endLine else startLine + 20 
              if count >= startLine + 2 and count <= endLine - 2:
                list_lines += removeComments(remove_comments(line))
            issues = Issues(fileName, list_lines, 0)
            list_line_issues.append(issues)      
              
                   
  np.random.shuffle(list_line_issues)
  for item in list_line_issues:
    writer.writerow([item.file, item.code, item.label])       
  f.close()  
      



    