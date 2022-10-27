#! /usr/bin/env/python 3.1
#
# handle the transformation of the scanner results files. 
# use MOT as transformattor
# author: Andreas Wagner
#
from AnalyzeToolConfig import AnalyzeToolConfig
import os.path
import glob
import py_common
from csv import reader

class TransformTool(object):
    def __init__(self, config):
        self.config = config

    def transformResult(self, scannerName, cwefileList, tmpDataDir):
         for cwefile in cwefileList:
            cwe_name = cwefile.split("/")[3]
            if(cwe_name != 'CWE476_NULL_Pointer_Dereference'):
                continue;
            files = glob.glob(tmpDataDir+ "/*" + cwe_name + "*.csv")
            summary_file = os.getcwd() + "/tmpData/" + scannerName + "_report.csv"
            with open(summary_file, "w") as outfile:
                outfile.write('Tool,File,Line,Value,Detail\n')
                for file in files:
                    with open(file, 'r') as read_obj:
                        csv_reader = reader(read_obj)
                        header = next(csv_reader)
                        if header != None:
                            for row in csv_reader:
                                file = str(row[0]).strip()
                                if("framac" in scannerName or "infer" in scannerName or "pvsstudio"):
                                    file_full_path = str(row[0]).strip().split('/')
                                    file = file_full_path.pop()
                                line = str(row[1]).strip()
                                value = str(row[2]).strip()
                                write_line = scannerName + ',' + file + "," + line + "," + value + "\n"
                                outfile.write(write_line)  
    
    def transformResults(self):
        cfg = self.config
        ccppScannerList = cfg.getCCppScannerList()
        searchPathCCpp = cfg.ccpptestsuiteFolderPath
        cwefileList = glob.glob(searchPathCCpp)
                
        if(len(ccppScannerList)>0):
            for scanner in ccppScannerList:
                scannerName = scanner.getName()
                result_path = cfg.tmpCppDataPath + scannerName
                self.transformResult(scannerName, cwefileList, result_path)
        
if __name__ == '__main__':
    cfg = AnalyzeToolConfig('config.cfg')
    
    tool = TransformTool(cfg)
    tool.transformResults()
