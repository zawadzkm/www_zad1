from classes.area import Area

class Ambit(Area):

    def __init__(self, id, name, parent, entitled, cards, votes, valid, invalid):
        self.id = id
        self.name = name
        self.parent = parent

        self.entitled = entitled
        self.cards = cards
        self.votes = votes
        self.valid = valid
        self.invalid = invalid

    def load(self):
        pass

    def render(self):
        pass



