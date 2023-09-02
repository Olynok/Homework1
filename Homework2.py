class Human:
    def __init__(self, fullName, birthday, phoneNum, city, country, homeAddress):
        self.full_name = fullName
        self.birthdate = birthday
        self.contact_phone = phoneNum
        self.city = city
        self.country = country
        self.home_address = homeAddress

    def show_info(self):
        print("FullName:", self.full_name)
        print("Дата народження:", self.birthdate)
        print("Контактний телефон:", self.contact_phone)
        print("Місто:", self.city)
        print("Країна:", self.country)
        print("Домашня адреса:", self.home_address)

    def set_full_name(self, new_full_name):
        self.full_name = new_full_name

    def set_birthdate(self, new_birthdate):
        self.birthdate = new_birthdate

    def set_contact_phone(self, new_contact_phone):
        self.contact_phone = new_contact_phone

    def set_city(self, new_city):
        self.city = new_city

    def set_country(self, new_country):
        self.country = new_country

    def set_home_address(self, new_home_address):
        self.home_address = new_home_address


Human1 = Human(
    "Онипко Михайло Олегович",
    "28.05.2012",
    "+48576449983",
    "Дніпро",
    "Україна",
    "вул. Робоча, 75"
)
Human1.show_info()

class City:
    def __init__(self, cityName, regionName, countryName, population, postalCode, phoneCode):
        self.city_name = cityName
        self.region_name = regionName
        self.country_name = countryName
        self.population = population
        self.postal_code = postalCode
        self.phone_code = phoneCode

    def show_info(self):
        print("Назва міста:", self.city_name)
        print("Назва регіону:", self.region_name)
        print("Назва країни:", self.country_name)
        print("Кількість жителів:", self.population)
        print("Поштовий індекс:", self.postal_code)
        print("Телефонний код:", self.phone_code)

    def set_city_name(self, new_city_name):
        self.city_name = new_city_name

    def set_region_name(self, new_region_name):
        self.region_name = new_region_name

    def set_country_name(self, new_country_name):
        self.country_name = new_country_name

    def set_population(self, new_population):
        self.population = new_population

    def set_postal_code(self, new_postal_code):
        self.postal_code = new_postal_code

    def set_phone_code(self, new_phone_code):
        self.phone_code = new_phone_code

if __name__ == "__main__":
    city1 = City("Дніпро", "Дніпропетровська область", "Україна", 1000000, "49000", "+38")
    city1.show_info()