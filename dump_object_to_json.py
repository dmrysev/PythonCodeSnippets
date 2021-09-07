#!/usr/bin/env python

import json

class C1:
    v1 = 3
    v2 = True
    v3 = [1, 4]


c1 = C1()
c1.v1 = 3
c1.v2 = False
c1.v3 = [4, 6]

j = json.dumps(c1.__dict__)
print(j)
