from address import Address
from mailing import Mailing

to_adr = Address("603000", "Нижний Новгород", "Белинского", "10", "45")

from_adr = Address("101000", "Москва", "Тверская", "7", "12")

mailing = Mailing(to_adr, from_adr, 350, "TRACK123456789")


print(
    "Отправление " + mailing.track + " из " +
    mailing.from_address.index + ", " + mailing.from_address.city + ", " +
    mailing.from_address.street + ", " + mailing.from_address.house + " - " +
    mailing.from_address.apartment + " в " +
    mailing.to_address.index + ", " + mailing.to_address.city + ", " +
    mailing.to_address.street + ", " + mailing.to_address.house + " - " +
    mailing.to_address.apartment + ". Стоимость " +
    str(mailing.cost) + " рублей."
)
