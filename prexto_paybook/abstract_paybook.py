import paybook.sdk as paybook_sdk

API_KEY = 'dbcd46a6da30ef8235815ad29e4a4e8c'


class AbstractPaybook(object):
    def __init__(self):
        paybook_sdk.Paybook(API_KEY)
