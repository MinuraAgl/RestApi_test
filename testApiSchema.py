import json

import requests
import jsonschema
from jsonschema import validate

schema = {
      "type": "object",
      "required": ["uuid", "title", "description", "id"],
      "properties": {
         "uuid": {
            "type": "string"
         },
         "id": {
            "type": "object",
            "required": ["timestamp", "date"],
            "properties": {
               "timestamp": {"type": "number"},
               "date": {"type": "string"}
            }},
         "title": {
            "type": "string"
         },
         "description": {
            "type": "string"
         }
      }
}


def validate_json(json_data):

   try:
      validate(instance=json_data, schema=schema)
   except jsonschema.exceptions.ValidationError as err:
      print(err)
      err = "Given JSON data is InValid"
      return False, err

   message = "Given JSON data is Valid"
   return True, message


def test_read_one_operation_has_expected_schema():
   response = requests.get('http://45.33.71.199:31000/user/subscriptions?uuid=06e2097f-d5b9-407e-aec8-cc2f335708cb')
   subs = json.loads(response.text)
   print(subs)
   for sub in subs:
      is_valid, msg = validate_json(sub)
      assert(is_valid)

