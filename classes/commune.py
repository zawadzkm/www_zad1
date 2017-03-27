from classes.area import Area

class Commune(Area):

    def __init__(self, id, name, parent, data):
        super().__init__(id, name, parent, data)
        self._template_name = "commune.html"
        self._output_name = str(self.id)+".html"

    def get_output_dir(self):
        return self.parent.get_output_dir()

    def get_url(self):
        return self.get_output_name()
