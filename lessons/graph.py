from collections import deque

graph = {}
graph['you'] = ['alice','bob','claire']
graph['bob'] = ['anuj','peggy']
graph['alice'] = ['peggy','gram']
graph['claire'] = ['thom','jonny']
graph['anuj'] = []
graph['peggy'] = []
graph['thom'] = []
graph['jonny'] = []
graph['gram'] = []


def personSeller(name):
    return name[-1] == 'm'

def search(name):
    searchQueue = deque() # экземпляр вызова очереди
    searchQueue += graph[name] # передаем в очередь новые значения
    searched = []
    while searchQueue:
        person = searchQueue.popleft() # возвращает первый (левый) элемент очереди
        if not person in searched:
            if personSeller(person):
                print(person, 'is a mango seller!')
                return True
            else:
                searchQueue += graph[person]
                searched.append(person)
    return False

search('you')