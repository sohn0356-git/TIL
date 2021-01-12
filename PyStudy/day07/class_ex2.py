class Human:

    def __init__(self, age, name):
        self.age = age
        self.name = name

    def __len__(self):
        return self.age

#     def __str__(self):
#         return "이름 %s, 나이 %d" %(self.name, self.age)
#
#     def __eq__(self, other):
#         return self.age == other.age and self.name == other.name
#
#
# kim = Human(29, "김상형")
# sang = Human(29, "김상형")
# moon = Human(44, "문종민")
# print(kim == sang)
# print(kim == moon)
# print(kim is sang)


class Card:

    spade = []
    heart = []
    clover = []
    diamond = []

    def __init__(self, spade, heart, clover, diamond):
        self.spade.extend(spade)
        self.heart.extend(heart)
        self.clover.extend(clover)
        self.diamond.extend(diamond)

    def __len__(self):
        return len(self.spade) + len(self.heart) + len(self.clover) + len(self.diamond)

card = Card([0,1,2,3],[3,4,5,6],[1,2,7,'J'],['Q','K'])
print(len(card))