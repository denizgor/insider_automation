#######INSIDER PANEL#######

Searchbox $(input[name = searchValue])

CreateButton $("#qa-create-button")

###CREATE CAMPAIGN SCREEN
Next Button $("#accept")

Error Message .in-text-input-wrapper__error-message

###CAMPAIGN SETTINGS SCREEN

Link Text : Segments Rules Design Goals Launch
By.linkText('Segments')

Save Button
#save-and-next

Rules Wrapper
.qa-page-rules
.qa-[rule-name, e.g: page-beavior-rules, weather-rules etc.]

Add Rule Group Button
$("#qa-add-group")

Campaign Trigger Bar
$.qa-accordion-toggle-icon[0]

Enable Campaign Radio Button
[title = "Enable Campaign Trigger"]

Diplay Time Bar
$.qa-accordion-toggle-icon[1]

Show Later Radio Button
#show-later

Input - Show
#show

Input - Hide
#hide



#######AMAZON#######
#https://www.amazon.com.tr/

#Giriş Butonu
$("#nav-link-accountList")
//a[@tabindex = 0][@data-nav-role='signin']

#Siparişler Butonu
$("#nav-orders")
//a[@id='nav-orders']

Sepet Butonu
$("#nav-cart")
//a[@id='nav-cart']

#Searchbox
$("#twotabsearchtextbox")
//input[@id='twotabsearchtextbox']
//input[@dir='auto']


#Logo
$("#nav-logo-sprites")
//a[@id='nav-logo-sprites']


#######SPX#######
#https://www.spx.com.tr/

#Kategori: Kadın 
$(".navigation__desktop-item")[3] 
[href = "/kadin/"][2]

#Ürün 
$(".product-card")[2] 
//div[@class = 'product-card'][@data-position = 2]

#Beden Tablosu 
$(".d-flex.flex-wrap.mb-sm-3.mb-2")[1] 
//div[@data-variant-key='integration_first_size']

#Beden 
$(".text-center.product__variant--size")[1] 
//span[text() = 'S']

#Sepete Ekle Buton 
$(".pz-button__add-to-cart") 
//button[@data-toggle = 'modal']

#Sepete Git 
$(".go-basket-btn") 
[class= 'icon-basket']
