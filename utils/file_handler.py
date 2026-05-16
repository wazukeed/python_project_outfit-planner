import json
import os

DATA_FILE = "data/outfits.json"


def load_outfits():

    if not os.path.exists(DATA_FILE):
        return []

    try:

        with open(DATA_FILE, "r") as file:

            return json.load(file)

    except json.JSONDecodeError:

        print("JSON file is empty or corrupted.")
        return []

    except Exception as e:

        print("Unexpected error:", e)
        return []


def save_outfits(outfits):

    try:

        with open(DATA_FILE, "w") as file:

            json.dump(outfits, file, indent=4)

    except Exception as e:

        print("Error while saving:", e)