class WebPush():
    def __init__(self, platform, optin, global_frequency, start_date, end_date, language, push_type):
        self.platform = platform
        self.optin = bool(optin)
        self.global_frequency = global_frequency
        self.start_date = start_date
        self.end_date = end_date
        self.language = language
        self.push_type = push_type

    def send_push(self):
        push_type = WebPush().push_type
        print(push_type.format("{} gönderildi"))

class TriggerPush(WebPush):
    trigger_page = ""


class BulkPush(WebPush):
    send_date = int()


class Segment_Push(WebPush):
    segment_name = ""


class PriceAlertPush(WebPush):
    price_info = int()
    discount_rate = float()

    def discount_price(self):


class InStockPush(WebPush):
    def stockUpdate(self):
        stock_info = bool

