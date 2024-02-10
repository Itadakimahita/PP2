import json

f = open('sample-data.json')

data = json.load(f)

f.close()

info = []

for i in data['imdata']:
    el = i['l1PhysIf']['attributes']
    info.append([el['dn'], el['descr'], el['speed'], el['mtu']])


print('Interface Status')
print('================================================================================')
print('DN                                                 Description           Speed    MTU  ')
print('-------------------------------------------------- --------------------  ------  ------')
for i in info:
    print(f'{i[0]}         {i[1]}                     {i[2]}   {i[3]}')
