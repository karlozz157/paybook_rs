import paybook.sdk as paybook_sdk

from .abstract_paybook import AbstractPaybook


class User(AbstractPaybook):
    def all(self):
        return paybook_sdk.User.get()

    def get(self, id_user):
        users = self.all()
        for user in users:
            if user.id_user == id_user:
                return user
        return None

    def create(self, name):
        return paybook_sdk.User(name=name)

    def delete(self, id_user):
        return paybook_sdk.User.delete(id_user)
