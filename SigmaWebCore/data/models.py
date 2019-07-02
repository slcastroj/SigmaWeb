class User():
    rut = None
    nombre = None
    clave = None
    email = None
    nacimiento = None
    id_tipo = None
    loged = False
    def Drop(self):
        self.rut = None
        self.nombre = None
        self.clave = None
        self.email = None
        self.nacimiento = None
        self.id_tipo = None
        self.loged = False
    def IsLoged(self):
        return self.loged
    def LogIn(self):
        self.loged = True