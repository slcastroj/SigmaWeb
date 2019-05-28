from SigmaWebCore.data.models import User

class BaseRepository:
    datasrc : list = []

class UserRepository(BaseRepository):
    def get_all(self):
        return list(self.datasrc)

    def get_single(self, rut):
        return next((x for x in self.datasrc if x.rut == rut), None)

    def post(self, **kwargs):
        self.datasrc.append(User(**kwargs))

    def patch(self, rut, **kwargs):
        user : User = next((x for x in self.datasrc if x.rut == rut), None)
        user.email = kwargs["email"]

    def delete(self, rut):
        user : User = next((x for x in self.datasrc if x.rut == rut), None)
        self.datasrc.remove(user)
