"""
DB DYNAMIC INSERT TESTING:
 > Will test dynamic insert of data into backend
    - Current issue, can create models and appropriately assign fields
      from list or arguments
    - However, cannot .save() method does not work
"""
import random
import string
from random import randint
from main.models import snapshot


class DBTestDataContainer():
    def __init__(self, a: int, b: int, c: str, d: str, e: int, f:float, g:float):
        self.a = a
        self.b = b
        self.c = c
        self.d = d
        self.e = e
        self.f = f
        self.g = g

#nTests : Number of random test lists we desire

def DynamicInsertTest(n: int):
    try:
        testObjects = []
        tests = createTestItems(n)
        for test in tests:
            snapObject = snapshot(
                auditid=test.a,
                storeid=test.b,
                itemid=test.c,
                sizeid=test.d,
                qtyonhand=test.e,
                cost=test.f,
                retailprice=test.g
            )

            testObjects.append(snapObject)
        id = 0
        for testObject in testObjects:
            testObject.id = id
            testObject.save()
            id = id + 1
    except Exception as e:
        return -1
    return 1

def createTestItems(nTests: int):
    """
    Snapshot schema:
        a   b    c    d   e    f    g
     > int int text text int real real
        - We will use all lower case for text
          and use randInt() + 0.10 for the real
          field
    """

    letters = string.ascii_lowercase
    tests = []
    for n in range(0,nTests, 1):
        a = randint(0,10)
        b = randint(0,10)
        c = (''.join(random.choice(letters) for i in range(10)))
        d = (''.join(random.choice(letters) for i in range(10)))
        e = randint(0,10)
        f = randint(0,10) + 0.10
        g = randint(0,10) + 0.10
        newTest = DBTestDataContainer(a, b, d, c, e, f, g)
        tests.append(newTest)

    return tests
