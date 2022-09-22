# Imports
import pywhatkit


# Class function sends a message to pre-specified WhatsApp number
class WhatsAppSender:

    def __init__(self, data, phone_num):
        self.data = data
        self.phone_num = phone_num
        self.tab_close = True  # bool: closes WhatsApp window that was opened
        self.wait_time = 15  # int: time until message is sent

    def send_to_whatsapp(self, message):
        return pywhatkit.sendwhatmsg_instantly(
            self.phone_num,
            message,
            self.wait_time,
            self.tab_close
        )
