import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aggregatorpy import Aggregator, Result, GetSHA256String, GetSHA256StringFromFile
from sys import argv
import datetime
from os.path import abspath

if __name__ == "__main__":
    if len(argv)<4:
        print("Usage: test.py url user pass")
        exit(-1)
    agg = Aggregator(argv[1], argv[2], argv[3])
    tool = agg.createTool("Test", GetSHA256String("Test"), GetSHA256StringFromFile(__file__), "Test tool for aggregator py implementation")
    if not tool:
        print("Aborting, couldn't create tool")
        exit(-1)
    scan = agg.startScan(tool, GetSHA256String("Test Scan"), GetSHA256String("Test Scan"+str(datetime.datetime.now())), "Test arguments: "+argv[1])
    if not scan:
        print("Aborting, couldn't start scan")
        exit(-1)
    for filename in ["testFileA", "testFileB"]:
        subj = agg.createSubject(filename, abspath(filename), GetSHA256String(filename), GetSHA256String(abspath(filename)))
        if not subj:
            print("Aborting couldn't create subject for", filename)
            exit(-1)
        result_text = f"There's no problem with {filename} this is just a test"
        risk = "Test"
        result = Result(scan.scan_hash, subj.hash, GetSHA256String(result_text), GetSHA256String(result_text), risk, result_text)
        if not agg.submitResult(result):
            print("Aborting couldn't submit result for", filename)
    agg.stopScan(scan)
    print("All tests successful")
    exit(0)