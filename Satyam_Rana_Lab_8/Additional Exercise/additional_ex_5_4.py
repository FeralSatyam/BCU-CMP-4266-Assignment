from datetime import date

class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        """
        birthdate should be a datetime.date object, e.g. date(2000, 5, 17)
        """
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def age(self):
        """Return age in full years based on today's date."""
        today = date.today()
        years = today.year - self.birthdate.year

        if (today.month, today.day) < (self.birthdate.month, self.birthdate.day):
            years -= 1
        return years


if __name__ == "__main__":
    p = Person(
        name="Al",
        surname="Smith",
        birthdate=date(1995, 3, 10),
        address="123 Main Street",
        telephone="+1-555-1234",
        email="al.smith@example.com"
    )

    print(f"{p.name} {p.surname} is {p.age()} years old.")
