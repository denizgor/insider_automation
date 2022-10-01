class WebPush:
    def __init__(self, platform: str, optin: bool, global_frequency_capping: int, start_date: str, end_date: str,
                 language: str, push_type: str):
        self.platform = platform
        self.optin = optin
        self.global_frequency_capping = global_frequency_capping
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        push_type = self.push_type
        push_message = "{} gönderildi"
        print(push_message.format(push_type))


class TriggerPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 trigger_page: str):
        super(WebPush, self).__init__()
        self.trigger_page = trigger_page



class BulkPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 send_date: int):
        super(WebPush, self).__init__()
        self.send_date = send_date


class Segment_Push(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 segment_name: str):
        super(WebPush, self).__init__()
        self.segment_name = segment_name


class PriceAlertPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 price_info: int, discount_rate: float):
        #super().__init__(platform, optin, global_frequency_capping, start_date, end_date, language, push_type)
        super(WebPush, self).__init__()
        self.price_info = price_info
        self.discount_rate = discount_rate

    def discount_price(self, price_info, discount_rate):
        self.price_info = price_info
        self.discount_rate = discount_rate
        return price_info * (discount_rate/100)


class InStockPush(WebPush):
    def __init__(self, platform, optin, global_frequency_capping, start_date, end_date, language, push_type,
                 stock_info: bool):
        super(WebPush, self).__init__()
        self.stock_info = stock_info

    def stockUpdate(self):
        updated_stock_info = True

        if self.stock_info == True:
            updated_stock_info = False

        return updated_stock_info



#TEST
web_push_obj1 = WebPush("Web", True, 3, "21.09.2022", "21.09.2023", "TR", "Instock Push")
web_push_obj1.send_push()

stock_push_obj1 = InStockPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "In stock Push", True)
print("In Stock:", stock_push_obj1.stock_info)

print("SPO-1 Update:", stock_push_obj1.stockUpdate())

stock_push_obj2 = InStockPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "In stock Push", False)
print("SPO-2 Update:", stock_push_obj2.stockUpdate())

# PRICE ALERT
price_alert_obj1 = PriceAlertPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "Price Alert Push", None, None)
print("Discount Amount:", price_alert_obj1.discount_price(80, 25))

price_alert_obj1.send_push()
