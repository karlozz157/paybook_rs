import paybook.sdk as paybook_sdk

from .abstract_paybook import AbstractPaybook
from .user import User
from .session import Session


class Credential(AbstractPaybook):
    def __init__(self, user_id):
        AbstractPaybook.__init__(self)
        user = User()
        self.user = user.get(user_id)
        session = Session()
        self.session = session.create(self.user)

    def all(self):
        return paybook_sdk.Credentials.get(self.session)

    def get(self, id_credential):
        credentials = self.all()
        for credential in credentials:
            if credential.id_credential == id_credential:
                return credential
        return None
