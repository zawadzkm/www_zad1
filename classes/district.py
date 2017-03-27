from classes.area import Area
from classes.commune import Commune

class District(Area):

    def __init__(self, id, name, parent, data):
        super().__init__(id, name, parent, data)
        self._template_name = "district.html"

    def load(self):
        super().load()

        comms = self.data.groupby(["Kodgminy", "Gmina"]).size()

        for i, val in comms.iteritems():
            d = Commune(i[0], i[1], self, self.data[self.data['Kodgminy'] == i[0]])
            d.load()
            self.subareas.append(d)





