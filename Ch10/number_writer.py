#https://docs.python.org/ko/3/library/json.html#module-json

import json
import pickle
json.dumps("{'name':'kim','age':'22}")

json.dumps(['foo', {'bar': ('baz', None, 1.0, 2)}])

print(json.dumps({'4': 5, '6': 7}, sort_keys=True, indent=4))
print(json.loads('["foo", {"bar":["baz", null, 1.0, 2]}]'))
print(json.loads('"\\"foo\\bar"'))


data1 = json.parse("{'a':1,'b':2}")
type(data1)
print(data1.a)
print(data1.b)

data = json()
data = json.parse("{'name':'kim','age':'22}")
type(data)
print(data.name)
print(data.age)
