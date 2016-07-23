class NavBar:
    def __init__(self):
        self.page_list = []

    def add_page_nav(self, number, page_name):
        self.page_list.append('<li><a href="#section{}">{}</a></li>'.format(number, page_name))

    def render(self):
        markup = '''<nav class="navbar navbar-inverse" data-spy="affix" data-offset-top="197">
        <ul class="nav navbar-nav">'''
        markup += ''.join(li for li in self.page_list)
        return markup + '</ul></nav>'


class Page:
    def __init__(self, file, title):
        self.file = file
        self.title = title


class PageCreator:
    def __init__(self, *args, **kwargs):
        self.volume = 0
        self.date = '2016-07-11'
        self.output_file = 'regisseur{}.html'.format(self.volume)
        self.title_div = ''
        self.body = ''
        self.navbar = NavBar()
        self.style_appends = ''
        self.page_list = []
        self.fuckyou = None


    def render(self):
        for i in range(len(self.page_list)):
            self._add_content(i, self.page_list[i])
        with open(self.output_file, 'w') as file:
            file.write(self._wrap_file())

    def _add_content(self, number, page):
        self.navbar.add_page_nav(number, page.title)
        with open(page.file, 'r') as page_file:
            self.body += self._wrap_page(number, page_file.read())

    def _wrap_page(self, number, file_content):
        return '''<div id="section{}" class="container-fluid PageDiv">{}</div>'''.format(number, file_content)

    def _wrap_file(self):
        with open('wrapping.html', 'r') as template:
            template_string = template.read()
        with open('regisseur.css', 'r') as css_file:
            style = css_file.read()
        with open('regisseur.js', 'r') as js_file:
            script = js_file.read()
        style += self.style_appends


        return template_string.format(
            style=style,
            script=script,
            title=self.title_div,
            navbar=self.navbar.render(),
            body=self.body,
        )

if __name__ == '__main__':
    p = PageCreator()
    p.page_list = [Page('page1.html', 'Test')]
    p.render()
    print('ready')