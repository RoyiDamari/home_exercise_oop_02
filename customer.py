class Customer:
    def __init__(self, id, first_name, last_name, address, mobile):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.mobile = mobile

    def __str__(self):
        return f'id:{self.id} name:{self.first_name} {self.last_name} address:{self.address} mobile:{self.mobile}'

    def __repr__(self):
        return f"Customer({self.id}, '{self.first_name}', '{self.last_name}', '{self.address}', '{self.mobile}')"

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return NotImplemented

        return (isinstance(other, Customer) and
                self.id == other.id and
                self.first_name == other.first_name and
                self.last_name == other.last_name and
                self.address == other.address and
                self.mobile == other.mobile)

    def __ne__(self, other):
        return not (self == other)

    def __hash__(self):
        return hash((self.id, self.first_name, self.last_name, self.address, self.mobile))

