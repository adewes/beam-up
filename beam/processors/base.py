
class BaseProcessor(object):

    def file(self, filename):
        return self.site.copy(filename)

    def href(self, href):
        return self.site.href(href)

    def scss(self, filename):
        return self.site.scss(filename)

    def __init__(self, site, params):
        self.site = site
        self.params = params

    