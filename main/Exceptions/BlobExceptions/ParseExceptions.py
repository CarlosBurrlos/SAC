from .BaseBlobException import BaseBlobException


class BaseParseException(BaseBlobException):

	"""
	Root Parse Exception class. All other parse exceptions will inherit from this
	By default the BaseParseException will be thrown as itself. However, 
	it does accept an Exception: Exception argument if a split/parse based exception is
	thrown.
	Interigate this item to determine the cause
	"""
	def __init__(self, CID, blob: str, Exception:Exception = None):
		super().__init__(blob)
		if Exception is not None:
		#If we have an exception thrown by another library we will just apppend its message
			self.msg += Exception.msg
		else:
			self.msg += f'Parsing Exception raised for offending blob {blob}\n'

class BadParseRuleException(BaseParseException):

	"""
	Thrown if the parsing rule being used is malformed. Will be interigated before
	use. However, check is not guaranteed to be complete
	"""

	def __init__(self, CID, blob, line: str, rule: str):

		super().__init__(blob)

		self.msg += '\tParser experienced a bad parse rule for the desired blob'
		self.msg += f'\tParser saw {line}'
		self.msg += f'\tBut parser expected a line delimited by the following {rule}'

class NothingToParseException(BaseParseException):
	def __init__(self, CID, rule: str):

		super().__init__(CID)

		self.msg += '\tNo blob(s) were sent to the parser\n'
		self.msg += f'\tParser expected a line delimited by the following {rule}'


class BadFileFormatException(BaseParseException):
	def __init__(self, CID, blob, rule: str):

		super().__init__(CID, blob)
		
		self.msg += f'\tBlob {blob} has an invalid file format for parsing\n'
		self.msg += '\tExpected file formats include the following:\n'
		self.msg += '\t\t*.txt\n\t\t*.json\n\t\t*.xml'
		self.msg += f'\tParser expected a line delimited by the following {rule}\n'


class NoParseResultsException(BaseParseExceptio):
	def __init__(self, CID, blob, rule: str):
		super().__init__(CID, blob)

		self.msg += f'\tBlob {blob} either has no information or the parse rule used resulted in not results\n'
		self.msg += '\tPlease check that the blob to be parsed has the correct information'
		self.msg += f'\tParser expected a line delimited by the following {rule}\n'