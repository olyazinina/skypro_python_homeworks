from smartphone import Smartphone

phone1 = Smartphone("Apple", "iPhone 14 Pro", "89270000001")

phone2 = Smartphone("Samsung", "Galaxy A55", "89370000001")

phone3 = Smartphone("Honor", "100", "89270000002")

phone4 = Smartphone("TECNO", "Spark Go 2024", "89270000003")

phone5 = Smartphone("Google Pixel", "6A", "89370000002")

catalog = [phone1, phone2, phone3, phone4, phone5]

for phone in catalog:
    print(phone.brand_phone, phone.model_phone, phone.subscriber_number)