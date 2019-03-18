import paybook.sdk as paybook_sdk

from .abstract_paybook import AbstractPaybook
from .credential import Credential


class Transaction(AbstractPaybook):
    def __init__(self, user_id):
        AbstractPaybook.__init__(self)
        self.credential = Credential(user_id)

    def all(self):
        transactions = []
        for credential in self.credential.all():
            transaction = paybook_sdk.Transaction.get(session=self.credential.session, options={
                'id_credential': credential.id_credential
            })
            transactions.extend(transaction)
        return transactions
