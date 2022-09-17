import pywhatkit

mock_data = {
    "title": "Product title",
    "price": "10.99",
    "link": "https://www.amazon.com/Passport-External-Portable-Compatible-systems/dp/B08RX3TWJZ/?_encoding=UTF8&pd_rd_i=B08RX3TWJZ&pd_rd_w=WVN5p&content-id=amzn1.sym.4d3375d7-b1e4-4223-90bf-0c57f2e88de3&pf_rd_p=4d3375d7-b1e4-4223-90bf-0c57f2e88de3&pf_rd_r=YCN1P49MXS2FTYXETHT2&pd_rd_wg=PTBsh&pd_rd_r=941c0800-0fd7-45e5-abd5-ada15d90ad17&ref_=deals&th=1"
}


class WhatsAppSender():

    def __init__(self, data, phone_num, hour, minute):
        self.data = data
        self.phone_num = phone_num
        self.hour = hour  # int(input("hour: "))
        self.minute = minute  # int(input("min: "))
        self.wait_time = 10  # int: time until message is sent

    def format_scraped_info(self):
        message = ""
        for k, v in self.data.items():
            message += f"{k}: {v}\n"
        """
        format the scraped info and assign it to the message
        attribute

        Pseudocode
        take in raw product info data
        convert
        """
        return message

    def send_to_whatsapp(self, message):
        return pywhatkit.sendwhatmsg(
            self.phone_num,
            message,
            self.hour,
            self.minute,
            self.wait_time,
        )


whatsAppSender = WhatsAppSender(mock_data, '+2404622142', 15, 29)
print(whatsAppSender.phone_num)
print(whatsAppSender.data)
message = whatsAppSender.format_scraped_info()
whatsAppSender.send_to_whatsapp(message)