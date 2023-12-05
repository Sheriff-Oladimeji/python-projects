import clipboard
import sys
import json


def save_items(filepath, data):
    with open(filepath, "w") as f:
        json.dump(data, f)


save_items("test.json", {"key": "value"})


def load_items(filepath):
    with open(filepath, "r") as f:
        data = json.load(f)
        return data


if len(sys.argv) == 2:
    command = sys.argv[1]

    if command == "save":
        print("save")
    elif command == "load":
        print("load")
    elif command == "list":
        print("list")
    else:
        print("unknown command")
else:
    print("please provide exactly one command.")
