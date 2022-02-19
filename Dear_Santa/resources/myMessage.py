
class Message:
    def __init__(self, attitude, gift2, gift3, gift1, drink, snack, name):
        self.attitude = attitude
        self.name = name
        self.attitude = attitude
        self.gift1 = gift1
        self.gift2 = gift2
        self.gift3 = gift3
        self.drink = drink
        self.snack = snack

    def __str__(self):
        return F"Dear Santa\n\nChristmas is comming up!\nI have been {self.attitude} this year,\
so I can't wait to find gifts under my tree.\nMy friends are all asking for {self.gift2} and {self.gift3} \
for Christmas, but if I had to pick the one thing I want most, it would be {self.gift1}.\nDon't forget \
to drink {self.drink} when you get to my house!\nI'll have plenty of {self.snack} for you, and extra \
snacks for reindeer.\n\nSincerely,\n\t{self.name}."