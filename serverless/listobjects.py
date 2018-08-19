#!/usr/bin/env python
import csvtoparquetlib
import sys
import json

def main(args):
    creds = args['__bx_creds']['cloud-object-storage'] 
    listobjs = csvtoparquetlib.convert_objects(creds['apikey'], args['endpoint'], args['bucket'])
    print(json.dumps({"names": listobjs.list_csv_objects_names()}))

if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
