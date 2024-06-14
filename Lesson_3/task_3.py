from address import Address
from mailing import Mailing

# Создание экземпляра класса Address для адреса назначения и адреса отправителя
to_address = Address("123456", "Москва", "Примерная улица", "10", "5")
from_address = Address("654321", "Санкт-Петербург", "Тестовая улица", "20", "15")

# Создание экземпляра класса Mailing
mailing = Mailing(to_address, from_address, 500, "TR123456789")

# Вывод информации о почтовом отправлении
print(f"Отправление {mailing.track} из {mailing.from_address.index}, \
      {mailing.from_address.city}, {mailing.from_address.street}, \
      {mailing.from_address.house} - {mailing.from_address.apartment} в \
      {mailing.to_address.index}, {mailing.to_address.city}, \
      {mailing.to_address.street}, {mailing.to_address.house} - \
      {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")