class NoClientFound(Exception):
    def __init__(self, message):
        super(NoClientFound, self).__init__(message)


class NoListFound(Exception):
    def __init__(self, message):
        super(NoListFound, self).__init__(message)


class WrongAPI(Exception):
    def __init__(self, message):
        super(WrongAPI, self).__init__(message)
