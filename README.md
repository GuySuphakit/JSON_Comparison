To use this script:

1. Ensure you have two JSON files named 'source.json' and 'target.json' in the same directory as this script.

   Example source.json:
   {
       "event": {
           "name": "Global Music Festival",
           "location": {
               "city": "Tokyo",
               "country": "Hokkaido"
           }
       }
   }

   Example target.json:
   {
       "event": {
           "name": "Global Music Festival",
           "date": "2024-08-10",
           "location": {
               "city": "Tokyo",
               "country": "Japan"
           }
       }
   }

2. Run the script:
   python json_compare.py

3. The script will generate an 'output.json' file with the comparison results and log information to the console.

   Example output.json:
   [
       {
           "operation": "add_new_key",
           "value": {"date": "2024-08-10"},
           "parent_key": ["event"],
           "after_key": "name"
       },
       {
           "operation": "modify_value",
           "value": {"country": "Japan"},
           "parent_key": ["event", "location"],
           "after_key": "city"
       }
   ]

This output shows the steps needed to transform the source JSON into the target JSON.
