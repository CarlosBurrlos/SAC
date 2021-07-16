import atexit
import threading
from .clearCache import removeAll

def exitHandler():

    print('Exit Detected\n')
    cleanCacheThread = threading.Thread(target=removeAll())
    cleanCacheThread.start()
    while cleanCacheThread.is_alive() :
        print('...\n')
    cleanCacheThread.join()
    print('Cache Has Been Cleaned\n')
    print('Exiting\n')