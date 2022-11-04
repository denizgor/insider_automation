#######INSIDER PANEL#######

#Searchbox 
$(input[name = searchValue])

![searchbox](https://user-images.githubusercontent.com/71087556/199945653-8dab07fc-d7d3-436d-9d7c-821132251be7.png)


#CreateButton 
$([data-title="CREATE"])
![image](https://user-images.githubusercontent.com/71087556/199946141-9f799725-b788-4fdb-b397-20fd3b53e8f8.png)


###CREATE CAMPAIGN SCREEN
#next Button 
$("#accept")

![next bttn](https://user-images.githubusercontent.com/71087556/199946312-bf5c9e17-b5b0-4844-92a4-a74536a455cb.png)


#Error Message 
.in-text-input-wrapper__error-message

![error message](https://user-images.githubusercontent.com/71087556/199946431-eea6b956-dcf5-4fa6-b06c-86f21e75ce5f.png)


###CAMPAIGN SETTINGS SCREEN

Segments> Rules> Design> Goals> Launch
By.linkText('Segments') ['Rules' / 'Design' etc.]

![segments](https://user-images.githubusercontent.com/71087556/199946581-13c4be57-9eba-4af4-b5e7-efbc4e8028f9.png)


Save Button
#save-and-next

![save bttn](https://user-images.githubusercontent.com/71087556/199946740-51157682-a274-4da8-9be5-29b514fbbe22.png)


Rules Wrapper
.qa-page-rules
.qa-[rule-name, e.g: page-beavior-rules, weather-rules etc.]

![rules](https://user-images.githubusercontent.com/71087556/199946776-5127f93c-eae0-4ea1-952e-8e2323c339a1.png)


Add Rule Group Button
$("#qa-add-group")

![image](https://user-images.githubusercontent.com/71087556/199947156-97187581-b9b8-4fee-b4a1-92394073a63b.png)


Campaign Trigger Bar
$.qa-accordion-toggle-icon[0]

![image](https://user-images.githubusercontent.com/71087556/199947334-d85824e2-4862-48cb-9a5c-e450a7310633.png)


Enable Campaign Radio Button
[title = "Enable Campaign Trigger"]

![image](https://user-images.githubusercontent.com/71087556/199948038-4a461cc7-529f-43eb-a9c1-7d9ff5d48f17.png)


Diplay Time Bar
$.qa-accordion-toggle-icon[1]

![image](https://user-images.githubusercontent.com/71087556/199948151-6aaa196e-3298-4897-a956-b0a84d59d4aa.png)


Show Later Radio Button
#show-later

![image](https://user-images.githubusercontent.com/71087556/199948381-76b617fa-558c-4237-9770-d0bbf10d0f9a.png)


Input - Show
#show

![image](https://user-images.githubusercontent.com/71087556/199948512-bd3dbabf-279b-4ae7-bf5a-e74ae09518ec.png)

Input - Hide
#hide

![image](https://user-images.githubusercontent.com/71087556/199948595-3bb53825-bbaf-46e1-88a6-f3f2ed1ca7de.png)



#######AMAZON#######
#https://www.amazon.com.tr/

#Giriş Butonu
$("#nav-link-accountList")
//a[@tabindex = 0][@data-nav-role='signin']

![giriş bttn](https://user-images.githubusercontent.com/71087556/199943016-2627d1d1-3418-4ed4-90c9-695bc9a1fe5e.png)

#Siparişler Butonu
$("#nav-orders")
//a[@id='nav-orders']

![siparişler bttn](https://user-images.githubusercontent.com/71087556/199943059-373d91e3-2d88-4534-80aa-4cec0e404eb0.png)


Sepet Butonu
$("#nav-cart")
//a[@id='nav-cart']

![sepet bttn](https://user-images.githubusercontent.com/71087556/199943090-00e58b46-f552-45e4-89fd-269e1d052ab6.png)


#Searchbox
$("#twotabsearchtextbox")
//input[@id='twotabsearchtextbox']
//input[@dir='auto']


![search box](https://user-images.githubusercontent.com/71087556/199943174-70844f98-7b16-4804-a542-24d7002c2ca3.png)


#Logo
$([id=nav-bb-logo])
//a[@id='nav-bb-logo']

![image](https://user-images.githubusercontent.com/71087556/199943562-7d684f16-b45d-4e88-b867-16dab87ecc25.png)


#######SPX#######
#https://www.spx.com.tr/

#Kategori: Kadın 
$(".navigation__desktop-item")[3] 
[href = "/kadin/"][2]

![kadın css](https://user-images.githubusercontent.com/71087556/199945173-ce4fb568-5afe-40d9-acb7-a1eb70d186f5.png)


#Ürün 
$(".product-card")[2] 
//div[@class = 'product-card'][@data-position = 2]

![ürün](https://user-images.githubusercontent.com/71087556/199945206-ab3a6b2f-a153-4a1a-82c1-85ecccae7d4a.png)


#Beden Tablosu 
$(".d-flex.flex-wrap.mb-sm-3.mb-2")[1] 
//div[@data-variant-key='integration_first_size']


![beden tablosu](https://user-images.githubusercontent.com/71087556/199945239-5dde90d7-75a0-4e23-9246-45d0673cc920.png)

#Beden 
$(".text-center.product__variant--size")[1] 
//span[text() = 'S']

![image](https://user-images.githubusercontent.com/71087556/199945465-363250d8-e4c5-4d97-bb7a-fb696441ddd1.png)


#Sepete Ekle Buton 
$(".pz-button__add-to-cart") 
//button[@data-toggle = 'modal']

![sepete ekle bttn](https://user-images.githubusercontent.com/71087556/199945495-14961ce5-4898-4916-b06d-d8792b1588bd.png)


#Sepete Git 
$(".go-basket-btn") 
[class= 'icon-basket']

![sepete git](https://user-images.githubusercontent.com/71087556/199945530-f9055975-2193-4916-abd3-260a9a340ce4.png)



