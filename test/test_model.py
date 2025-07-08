import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
from aggregatorpy import Aggregator, GetSHA256String, GetSHA256StringFromFile
from aggregatorpy.common import *
from aggregatorpy.model import *
from sys import argv
import datetime
from os.path import abspath, basename

if __name__ == "__main__":
    if len(argv)<4:
        print("Usage: test.py url user pass")
        exit(-1)

    agg = Aggregator(argv[1], argv[2], argv[3])
    # Initialize aggregator used for common properties and tags
    set_common_aggregator(agg)

    _tool = Tool(agg, "AggregatorPy Test", GetSHA256String("Test"), GetSHA256StringFromFile(__file__), "0.1", "Test tool for aggregator py implementation")
    _scan = Scan(agg, _tool, GetSHA256String("Test Scan"+str(datetime.datetime.now())), "Test arguments: "+argv[1])
    # Can be called, but it should automatically be resolved when we submit any result anyway
    _scan.start() 

    # In general all objects that are created will be submitted lazily when their ids are required.

    # Creating our own tag that isn't in the common list
    testTag = Tag(agg, "test", "test", "Marks test data", "pink")

    # Creating a root subject to demonstrate tree view
    parent = Subject(agg, 'root', GetSHA256String('root'), -1, [FilePathProperty(abspath(".")), DirNameProperty(basename(abspath(".")))], [openTag, rootTag, dirTag, testTag])

    for filename in ["testFileA", "testFileB", "testFileC", "testFileD"]:
        subj = Subject(agg, filename, GetSHA256String(filename), parent, [FilePathProperty(abspath(filename)), FileNameProperty(filename)], [openTag, fileTag, testTag])
        if not subj:
            print("Aborting couldn't create subject for", filename)
            exit(-1)
        result_text = f"## Test Result\n```There's no problem with {filename} this is just a test```"
        res = Result(agg, _scan.get_id(), subj.get_id(), GetSHA256String(result_text), 'Test Result 1', result_text, [ContainingPathProperty(abspath(filename))], [openTag, testTag])

        result_text = f"## Test Result 2\n```There's no problem with {filename} this is just another test```"
        res2 = Result(agg, _scan.get_id(), subj.get_id(), GetSHA256String(result_text), 'Test Result 2', result_text, [ContainingPathProperty(abspath(filename))], [openTag, testTag])
        #result = Result(scan.scan_hash, subj.hash, GetSHA256String(result_text), GetSHA256String(result_text), risk, 'Test Result', result_text, [open_tag, test_tag])
        # Submitting here should recursively trigger the creation of 
        res.submit()
        res2.submit()

    # Creating a second root subject to demonstrate tree diff
    parent = Subject(agg, 'root2', GetSHA256String('root2'), -1, [FilePathProperty(abspath(".")), DirNameProperty(basename(abspath(".")))], [openTag, rootTag, dirTag, testTag])

    for filename in ["testFileA", "testFileB", "testFileC", "testFileE"]:
        #Changed hard hash to make it a separate subject
        subj = Subject(agg, filename, GetSHA256String(filename+"2"), parent, [FilePathProperty(abspath(filename)), FileNameProperty(filename)], [openTag, fileTag, testTag])
        if not subj:
            print("Aborting couldn't create subject for", filename)
            exit(-1)
        result_text = f"## Test Result\n```There's no problem with {filename} this is just a test for diff```"
        res = Result(agg, _scan.get_id(), subj.get_id(), GetSHA256String(result_text), 'Test Result 1', result_text, [ContainingPathProperty(abspath(filename))], [openTag, testTag])
        #result = Result(scan.scan_hash, subj.hash, GetSHA256String(result_text), GetSHA256String(result_text), risk, 'Test Result', result_text, [open_tag, test_tag])
        # Submitting here should recursively trigger the creation of 
        res.submit()
        res2.submit()

    _scan.stop() # Scan should be stopped explicitly, even if it wasn't explicitly started
    print("Done submitting")
    exit(0)