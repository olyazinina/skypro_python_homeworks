from address import Address
from mailing import Mailing


from_address = Address("156005", "Kostroma", "Lagernaya", "38", "5")
to_address = Address("115569", "Moskow", "Dolskaya", "1", "56")
cost = 846
track = "44630540019732"

my_mailing = Mailing(to_address, from_address, cost, track)

print(f' Отправление {my_mailing.track} из {my_mailing.from_address.index} {my_mailing.from_address.city} {my_mailing.from_address.street} {my_mailing.from_address.house} {my_mailing.from_address.apartment} в {my_mailing.to_address.index} {my_mailing.to_address.city} {my_mailing.to_address.street} {my_mailing.to_address.house} {my_mailing.to_address.apartment} Стоимость {my_mailing.cost} рублей.')