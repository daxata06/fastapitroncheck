class CommonError(Exception):
    def __str__(self):
        return self.__class__.__name__


class AddressNotFoundError(CommonError):
    pass
