from .base import BaseProcessor

from jinja2 import Environment, FileSystemLoader, ChoiceLoader, DictLoader

class JinjaProcessor(BaseProcessor):

    def get_jinja_env(self, input):
        dict_loader = DictLoader({'input' : input})
        choice_loader = ChoiceLoader([dict_loader, FileSystemLoader('{}/templates'.format(self.site.theme_path))])
        env = Environment(loader=choice_loader)
        env.filters['href'] = self.href
        env.filters['file'] = self.file
        env.filters['scss'] = self.scss
        return env

    def process(self, input, vars):
        env = self.get_jinja_env(input)
        template = env.get_template('input')
        return template.render(**vars)