from .base import BaseProcessor

from jinja2 import Environment, FileSystemLoader, ChoiceLoader, DictLoader

from pygments import highlight
from pygments.styles import get_style_by_name
from pygments.lexers import get_lexer_by_name
from pygments.formatters import HtmlFormatter

try:
    from bs4 import BeautifulSoup as bs
    with_bs = True
except ImportError:
    with_bs = False

class JinjaProcessor(BaseProcessor):

    def highlight_styles(self, code, style_name='monokai'):
        style = get_style_by_name(style_name)
        return '<style type="text/css">{}</style>'.format(HtmlFormatter(style=style).get_style_defs('.highlight .{}'.format(style_name)))

    def highlight(self, code, language='python', style_name='monokai', strip=True):
        lexer = get_lexer_by_name(language)
        style = get_style_by_name(style_name)
        if strip:
            code = code.strip()
        return highlight(code, lexer, HtmlFormatter(style=style, cssclass='{}'.format(style_name)))

    def get_jinja_env(self, input):
        dict_loader = DictLoader({'input' : input})
        theme_path = self.site.theme_path
        choice_loader = ChoiceLoader([dict_loader, FileSystemLoader('{}/templates'.format(theme_path)), FileSystemLoader(self.site.src_path)])
        env = Environment(loader=choice_loader)
        env.filters['href'] = self.href
        env.filters['file'] = self.file
        env.filters['highlight'] = self.highlight
        env.filters['highlight_styles'] = self.highlight_styles
        env.filters['translate'] = self.translate
        for filters in self.site.addons['jinja-filters']:
            for name, f in filters:
                env.filters[name] = f
        return env

    def process(self, input, vars):
        env = self.get_jinja_env(input)
        template = env.get_template('input')
        result = template.render(**vars)
        if with_bs and False:
            soup=bs(result, "html.parser")
            return soup.prettify()
        return result