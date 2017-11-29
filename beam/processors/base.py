
class BaseProcessor(object):

    def translate(self, key):
        return self.site.translate(key, self.language)

    def file(self, filename):
        return self.site.copy(filename)

    def href(self, href):
        return self.site.href(href)

    def scss(self, filename):
        return self.site.scss(filename)

    def __init__(self, site, params, language):
        self.site = site
        self.params = params
        self.language = language

    