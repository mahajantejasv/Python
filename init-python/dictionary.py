dict_obj = {'key1':'value1','key2':'value2'}
print(dict_obj)
print(dict_obj['key2'])

dict_obj = {'key1':123,'key2':[12,23,33],'key3':['item0','item1','item2']}
print(dict_obj['key3'])
print(dict_obj['key3'][0])
str = dict_obj['key3'][0]
print(str.upper())

d = {'key1':{'nestkey':{'subnestkey':'value'}}}
d['key1']['nestkey']['subnestkey']

print(dict_obj.keys())

print(dict_obj.values())

print(dict_obj.items())