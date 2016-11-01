import collections
from collections import OrderedDict



inv = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12}
inv_1 = OrderedDict(sorted(inv.items(), key=lambda t:t[1]))
print(inv_1)
for k, v in inv_1.items():
    print (k, " ", v)

