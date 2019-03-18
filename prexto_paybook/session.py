import paybook.sdk as paybook_sdk

from .abstract_paybook import AbstractPaybook


class Session(AbstractPaybook):
    def create(self, user):
        return paybook_sdk.Session(user=user)
