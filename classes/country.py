import os, sys
from classes.voivodeship import Voivodeship
from classes.area import Area

class Country(Area):

    def __init__(self, data):

        super().__init__(id, "Poland", None, data)
        self._template_name = "country.html"

    def get_output_dir(self):
        return os.path.join(os.path.dirname(sys.argv[0]), "www")

    def get_url(self):
        return "."

    def load(self):
        super().load()

        vois = self.data.groupby(["Nrwoj", "Wojewodztwo"]).size()

        for i, val in vois.iteritems():
            v = Voivodeship(i[0], i[1], self, self.data[self.data['Nrwoj'] == i[0]])
            v.load()
            self.subareas.append(v)


