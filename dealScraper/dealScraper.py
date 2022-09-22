# Imports
import sys
from pathlib import Path

# Import local files
from GUI import *
from scrape import *
from whatsapp import WhatsAppSender


def main():
    # Local File Variables
    params_file = 'params.json'
    number_file = 'number.txt'
    params_path = Path(params_file)
    number_path = Path(number_file)

    # Checks for params.json and number.txt, if non-existent, loads GUI
    if params_path.is_file() and number_path.is_file():
        print("'params.json' and 'number.txt' currently exist in this local directory. \n"
              "If you wish to update these and re-run the GUI, please delete them both from this folder and re-run the "
              "application.")
    else:
        # Create new params file
        print("Let's create your preference files!")
        gui()

    try:
        # Load preferences from local file params.json
        with open(params_file) as f:
            params = json.load(f)
            f.close()

        # Webscraper Call
        absolute_url = format_request(params)
        soup = get_products(absolute_url)
        data = parser(soup)

        with open(number_file) as f:
            phone_num = "+" + f.read()

        # WhatsApp Sender Call / Message Formatting
        ws = WhatsAppSender(data, phone_num)
        message = ""
        for items in data:
            items_values = items.values()
            for item in items_values:
                message += str(item)
                message += "\n"
            message += "\n\n"
        ws.send_to_whatsapp(message)

    # Any unexpected error closes application
    except:
        print("DealScraper encountered an error. Closing...")
        sys.exit()


if __name__ == "__main__":
    main()
