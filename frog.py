import collections
n = int(input())
# print(n)
cards = []
for i in range(n):
    card = int(input())
    cards.append(card)

hash = collections.defaultdict(int)
for card in cards:
    hash[card] += 1

for key in sorted(hash.keys()):
    print(key,hash[key])