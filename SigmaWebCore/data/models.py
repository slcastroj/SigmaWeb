class User:
    rut : str
    nombre : str
    email : str

    def __init__(self, **kwargs):
        self.__dict__.update(kwargs)