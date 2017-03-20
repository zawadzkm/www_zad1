from classes.district import District
from classes.area import Area

class Voivodeship(Area):

    def __init__(self, id, name, parent, data):
        super().__init__(id, name, parent, data)
        self._template_name = "voivodeship.html"

    def load(self):
        super().load()

        vois = self.data.groupby(["Nrokr", "Okreg"]).size()

        for i, val in vois.iteritems():
            d = District(i[0], i[1], self, self.data[self.data['Nrokr'] == i[0]])
            d.load()
            self.subareas.append(d)




