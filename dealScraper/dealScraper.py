# Imports
import sys
import json

# Import local files
from GUI import *
from scrape import *
# from whatsapp import *


def main():

    # Local Variables
    params_file = 'params.json'

    # Create new params file

    try:
        gui()
        with open(params_file) as f:
            params = json.load(f)
            f.close()
            formatRequest(params)
    except FileNotFoundError:
        print("DealScraper encountered an error. Closing...")
        sys.exit()


if __name__ == "__main__":
    main()
