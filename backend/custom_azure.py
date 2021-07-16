from storages.backends.azure_storage import AzureStorage

class AzureBlobStorage(AzureStorage):
    account_name = 'sactesting'
    account_key = 'EFGG6vWns1QpLxOWGiq58t7ZDYGpmg0BnhFQ+Abzlexbk+gcgxuP24UTkuMUnvlrUnjuiU79Ud8VXvyyQqKFSA=='
    azure_container = 'sac'
    expiration_secs = None