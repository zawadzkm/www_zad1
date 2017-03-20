import os, sys
from jinja2 import Environment, FileSystemLoader
from classes.constants import Constants
from classes.candidate import Candidate

class Area:
    __template = None

    def __init__(self, id, name, parent, data):
        self.id = id
        self.name = name
        self.parent = parent

        self._template_name = ""
        self._output_name = "index.html"
        self.entitled = 0
        self.cards = 0
        self.votes = 0
        self.valid = 0
        self.invalid = 0
        self.attendance = 0

        self.data = data
        self.subareas = []
        self.candidates = []

    def get_output_name(self):
        return self._output_name

    def get_output_dir(self):
        return os.path.join(self.parent.get_output_dir(), str(self.id))

    def get_output_path(self):
        return os.path.join(self.get_output_dir(), self.get_output_name())

    def get_url(self):
        return str(self.id)+"/"+self.get_output_name()

    def load(self):
        grouped = self.data[[Constants.ENTITLED, Constants.CARDS, Constants.VOTES, Constants.VALID, Constants.INVALID]].sum()

        self.entitled = grouped[Constants.ENTITLED]
        self.cards = grouped[Constants.CARDS]
        self.votes = grouped[Constants.VOTES]
        self.valid = grouped[Constants.VALID]
        self.invalid = grouped[Constants.INVALID]
        self.attendance = round(self.votes/self.entitled*100, 2)

        rs = self.data[Constants.CANDIDATES].sum()

        for c in Constants.CANDIDATES:
            self.candidates.append(Candidate(c, rs[c], round(rs[c]/self.valid*100, 2)))

    def load_template(self):
        path = os.path.dirname(sys.argv[0])
        env = Environment(autoescape=True, loader=FileSystemLoader(os.path.join(path, 'templates')))
        return env.get_template(self._template_name)

    def get_template(self):
        if self.__class__.__template is None:
            self.__class__.__template = self.load_template()
        return self.__class__.__template

    def render(self):
        html = self.get_template().render(area=self)
        self.save_html(html)

        for sa in self.subareas:
            sa.render()

    def save_html(self, html):
        if not os.path.exists(self.get_output_dir()):
            os.makedirs(self.get_output_dir())

        with open(self.get_output_path(), "w", encoding="utf-8") as f:
            f.write(html)
            f.close()