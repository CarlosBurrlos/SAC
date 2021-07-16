
from django.contrib.sessions.backends.file import SessionStore
import os
# Store the account name, key and container name inside a session variable in our cache

# Determine if we can use the URI I setup through Azure CLI >> Eliminating need to store key in cache

os.environ['AZURE_STORAGE_URI'] = 'https://sactesting.blob.core.windows.net'
os.environ['AZURE_ACCOUNT'] = 'sactesting'
os.environ['AZURE_CONTAINER_NAME'] = 'sac'
os.environ['AZURE_STORAGE_KEY'] = 'EFGG6vWns1QpLxOWGiq58t7ZDYGpmg0BnhFQ+Abzlexbk+gcgxuP24UTkuMUnvlrUnjuiU79Ud8VXvyyQqKFSA=='


#s = SessionStore()
#s['AZURE_ACCOUNT_NAME'] =
#s['AZURE_ACCOUNT_KEY'] = ''
#s['CONTAINER_NAME']
#s['ACCOUNT_URI'] =
#s.create()
