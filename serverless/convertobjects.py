#!/usr/bin/env python
import csvtoparquetlib
import sys
import json

def main(args):
    creds = args['__bx_creds']['cloud-object-storage'] 
    convert_objs = args['convert_objs']
    new_names = args['new_names']
    
    csvp = csvtoparquetlib.convert_objects(creds['apikey'], args['endpoint'], args['bucket'])

    if len(convert_objs) != len(new_names):
        print(json.dumps({"error": "The length of convertable objects doesn't match new names."}))
        return

    if not new_names:
        print(json.dumps({"error": "You need to provide new names for your objects."}))
        return

    csvp.convert_selected_objects(convert_objs, new_names)

    results = {
        "converted_objects": "done"
    }

    print(json.dumps(results))

if __name__ == "__main__":
    main(json.loads(sys.argv[1]))
