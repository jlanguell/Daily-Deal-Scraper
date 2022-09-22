# Imports
import sys
import json

# Import local files
from GUI import *
from scrape import *
from whatsapp import WhatsAppSender


def main():
    # Local Variables
    params_file = 'params.json'
    number_file = 'number.txt'

    # Create new params file

    try:

        gui()

        with open(params_file) as f:
            params = json.load(f)
            f.close()

        # Webscraper Call
        absoluteURL = formatRequest(params)
        soup = getProducts(absoluteURL)
        data = parser(soup)
        # data = list(data)

        with open(number_file) as f:
            phone_num = "+" + f.read()

        # WhatsApp Sender Call
        ws = WhatsAppSender(data, phone_num)
        message = ""
        for items in data:
            items_values = items.values()
            for item in items_values:
                message += str(item)
                message += "\n"
            message += "\n\n"
        print(message)
        '''
        for item in data:
            message += str(item)
            message += "\n"
        '''
        # message = ws.format_scraped_info(data)
        ws.send_to_whatsapp(message)

    except:
        print("DealScraper encountered an error. Closing...")
        sys.exit()


if __name__ == "__main__":
    main()
