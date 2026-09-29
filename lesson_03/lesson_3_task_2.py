from smartphone import Smartphone

catalog = []

catalog.append(Smartphone("Apple", "iPhone 15", "+79111234567"))
catalog.append(Smartphone("Samsung", "Galaxy S24", "+79222345678"))
catalog.append(Smartphone("Xiaomi", "Redmi Note 13", "+79333456789"))
catalog.append(Smartphone("Google", "Pixel 8", "+79444567890"))
catalog.append(Smartphone("Huawei", "Pura 70", "+79555678901"))

for phone in catalog:
    print(phone.brand + " - " + phone.model + ". " + phone.phone_number)
