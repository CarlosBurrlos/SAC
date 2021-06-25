from enum import Enum as E

class errors(E):
    MSQLCLIENTERR = 1


class MySQLClientError(Exception):

    # For the future, any more error reporting information
    # can be added to these args

    def __init__(self, message, errors, query=None):
        super().__init__(message)  # Init parent class Exception
        self.message = message
        if len(errors) == 0:
            self.errors = None
        else:
            self.errors = errors
        if query is not None:
            self.query = query

    def __str__(self):
        if self.query is not None:
            retString: str = 'MYSQL-Client failed to execute the following query :: \n'
            retString += f'{self.query}\n'
            if self.errors is not None:
                n: int = 1
                # TODO :: Add a reasons item to our error messages in the future
                for error in self.errors:
                    retString += f'Error{n} :: {error}'
        else:
            retString: str = 'MYSQL-Client failed with the following message :: \n'
            retString += f'{self.message}'
        return retString
