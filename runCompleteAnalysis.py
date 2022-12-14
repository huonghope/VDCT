#! /usr/bin/env/python 3.1
#
# main file (or entry point) for the analysis. Handles all different stuff like, collection flaws, 
# start the security scanners and generate result-reports
#
import time
from FlawCollector import FlawCollector
from GoodCollector import GoodCollector
import sys
from AnalyzeToolConfig import AnalyzeToolConfig
from TestsuiteAnalyzer import TestsuiteAnalyzer
from CompareTool import CompareTool
from TransformTool import TransformTool
import os


if __name__ == '__main__':
    config = AnalyzeToolConfig('config.cfg')
    
    startTime = time.time()
    print("Start a complete analysis run")
    print("collection flaws in testsuite")
    
    flawCollector = FlawCollector(config)
    goodCollector = GoodCollector(config)
    # if(len(config.getCCppScannerList())>0):
    #     startFlawCollection=time.time()
    #     # flawCollector.collect('ccpp')
    #     goodCollector.collect('ccpp')
    #     endFlawCollection=time.time()
    #     print("collected ccpp flaws in "+str((endFlawCollection-startFlawCollection))+" seconds")
    #     for scanner in config.getCCppScannerList():
    #         tmpDir = config.tmpCppDataPath+scanner.name
    #         if (not os.path.exists(tmpDir)):
    #             os.mkdir(tmpDir)
    
    # print("start analyzing testsuite");
    # startAnalyzeTime = time.time()
    # analyzeTool = TestsuiteAnalyzer(config)
    # analyzeTool.runAnalyze()
    # endAnalyzeTime = time.time()
    # print("run static analyzers in "+str((endAnalyzeTime-startAnalyzeTime))+" seconds")
    

    print("transforming scanner results");
    startTransformTime = time.time();
    transformTool = TransformTool(config)
    transformTool.transformResults()

    endTransformTime = time.time();
    print("transformed scanner results in "+str((endTransformTime-startTransformTime))+" seconds")