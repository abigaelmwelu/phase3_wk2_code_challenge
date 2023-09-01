class Customer:
    all_customers = []

    def _init_(self, given_name, family_name):
        self.given_name = given_name
        self.family_name = family_name
   
        self._class_.all_customers.append(self)

    @property
    def first_name(self):
        return self.given_name

    @property
    def last_name(self):
        return self.family_name

    @property
    def full_name(self):
        return f"{self.given_name} {self.family_name}"

    @classmethod
    def all(cls):
        return cls.all_customers