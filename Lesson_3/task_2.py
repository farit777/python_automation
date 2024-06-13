from smartphone import Smartphone

# Объявление переменной catalog
catalog = []

# Создание пяти разных экземпляров класса Smartphone и добавление их в список catalog
phone1 = Smartphone("Apple", "iPhone 12", "+79123456789")
catalog.append(phone1)

phone2 = Smartphone("Samsung", "Galaxy S21", "+79234567890")
catalog.append(phone2)

phone3 = Smartphone("Xiaomi", "Mi 11", "+79345678901")
catalog.append(phone3)

phone4 = Smartphone("Google", "Pixel 5", "+79456789012")
catalog.append(phone4)

phone5 = Smartphone("OnePlus", "8T", "+79567890123")
catalog.append(phone5)

# Цикл для печати каталога
for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")