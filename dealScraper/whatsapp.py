import pywhatkit


class WhatsAppSender:


    def __init__(self, data, phone_num):
        self.data = data
        self.phone_num = phone_num
        self.tab_close = True  # int(input("min: "))
        self.wait_time = 15  # int: time until message is sent


    def format_scraped_info(self, data):

        message = ""
        for item in data:

            message += str(item)
            message += "\n"
        """
        for k, v in self.data.items():
            message += f"{k}: {v}\n"
        """
        """
        format the scraped info and assign it to the message
        attribute

        Pseudocode
        take in raw product info data
        convert
        """
        return message


    def send_to_whatsapp(self, message):

        return pywhatkit.sendwhatmsg_instantly(
            self.phone_num,
            message,
            self.wait_time,
            self.tab_close

        )
