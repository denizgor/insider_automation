#TEST KODLARI
#WEB PUSH
web_push_obj1 = WebPush("Web", True, 3, "21.09.2022", "21.09.2023", "TR", "Web Push")
web_push_obj1.send_push()

#TRIGGER PUSH
trigger_push_obj1 = TriggerPush("Tablet", True, 1, "12.01.2022", "12.12.2022", "DE", "Trigger Push", "Product Page")
trigger_push_obj1.send_push()

#BULK PUSH
bulk_push_object1 = BulkPush("Mobile", True, 2, "23.04.2022", "13.09.2022", "FR", "Bulk Push", 12112022)
bulk_push_object1.send_push()

#SEGMENT PUSH
segment_push_obj1 = Segment_Push("Web", False, 1, "02.03.2022", "02.04.2022", "TR", "Segment Push", "Cart Abandoner")
segment_push_obj1.send_push()

#PRICE ALERT
price_alert_obj1 = PriceAlertPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "Price Alert Push", None, None)
print("Discount Amount:", price_alert_obj1.discount_price(80, 25))
price_alert_obj1.send_push()

#STOCK PUSH
stock_push_obj1 = InStockPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "In Stock Push", True)
print("In Stock:", stock_push_obj1.stock_info)
print("SPO-1 Update:", stock_push_obj1.stockUpdate())

#stock_push_obj2 = InStockPush("Mobile", False, 4, "23.20.2021", "25.11.2022", "TR", "In stock Push", False)
#print("SPO-2 Update:", stock_push_obj2.stockUpdate())
