import os
import json

def add_output(name, value):
    with open(os.environ["GITHUB_OUTPUT"], "a") as fh:
        print(f"{name}={value}", file=fh)

my_dict={"coucou": "tu", "veux": "voir"}

add_output("my_dict", json.dumps(my_dict))
