class UserDomain:
    def __init__(self, name, email, password, cpf, endereco):
        self.name = name
        self.email = email
        self.password = password
        self.cpf = cpf
        self.endereco = endereco

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "cpf": self.cpf,
            "endereco": self.endereco
        }