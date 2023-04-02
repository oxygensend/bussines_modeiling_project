import json

temp = """
[
  {
    "name": "Order Processing",
    "actions": [
      "pick item",
      "place order",
      "confirm order",
      "pay order",
      "item out of stock",
      "reorder item",
      "create package",
      "send package",
      "package delivered",
      "payment reminder",
      "failed delivery"
    ]
  },
  {
    "name": "Inventory Management",
    "actions": [
      "pick item",
      "item out of stock",
      "reorder item"
    ]
  },
  {
    "name": "Shipping",
    "actions": [
      "create package",
      "send package",
      "package delivered",
      "failed delivery"
    ]
  },
  {
    "name": "Payment Processing",
    "actions": [
      "place order",
      "confirm order",
      "pay order",
      "payment reminder"
    ]
  }
]
"""

temp.replace("]", "").replace("[", "")
y = json.loads(temp)
dct = {}
for res in y:
    dct[res['name']] = res['actions']

print(dct)