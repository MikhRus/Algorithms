from functools import reduce


voted = {}
voted['Joe'] = True
def checkVoter(name):
    if voted.get(name):
        print('Get OUT!')
    else:
        voted[name] = True
        print('Let them vote!')

checkVoter('Tom')
checkVoter('Joe')
print(voted.keys())

reduce
map