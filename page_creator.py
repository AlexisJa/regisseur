# coding=utf-8
class NavBar:
    def __init__(self, date, volume):
        self.page_list = []
        self.date = date
        self.volume = volume

    def add_page_nav(self, number, page_name):
        self.page_list.append('<li><a href="#section{}">{}</a></li>'.format(number, page_name))

    def render(self):
        markup = self._add_jumbotron()
        markup += '''<nav class="navbar navbar-inverse" data-spy="affix" data-offset-top="250">
        <ul class="nav navbar-nav">'''
        markup += ''.join(li for li in self.page_list)
        return markup + '</ul></nav>'

    def _add_jumbotron(self):
        return '''
        <div class="container">
            <div class="jumbotron">
                <h1>Régisseur</h1>
                <h4>Le journal étudiant du Regroupement des Étudiants <br> de Génie Informatique et Électrique</h4>
                <h5>Volume {vol} - Édition {edition}</h5>
            </div>
        </div>
        '''.format(vol=self.volume, edition=self.date)


class Page:
    def __init__(self, file, title):
        self.file = file
        self.title = title


class PageCreator:
    def __init__(self, *args, **kwargs):
        self.volume = 1
        self.date = "Rentrée automne 2016"
        self.output_file = 'regisseur{}.html'.format(self.volume)
        self.title_div = ''
        self.body = ''
        self.navbar = NavBar(self.date, self.volume)
        self.style_appends = ''
        self.page_list = []
        self.host = "https://cdn.rawgit.com/AlexisJa/regisseur/master/"
        self.commit_id = ''

    def render(self):
        for i in range(len(self.page_list)):
            self._add_content(i, self.page_list[i])
        with open(self.output_file, 'w') as file:
            file.write(self._wrap_file())

    def _add_content(self, number, page):
        self.navbar.add_page_nav(number, page.title)
        with open(page.file, 'r') as page_file:
            self.body += self._wrap_page(number, page.title, page_file.read())

    def _wrap_page(self, number, title, file_content):
        return '''<div id="section{number}" class="container-fluid PageDiv">
        <h2>{title}</h2>
        {content}</div>'''.format(number=number, content=file_content, title=title)

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
    p.page_list = [
        Page('r1/new_regisseur.html', 'Bonne rentrée!'),
        # Page('r0/p2.html', 'Page 2'),
        # Page('r0/p2.html', 'Page 3'),
        # Page('r0/p1.html', 'Page 4'),
        # Page('r0/p1.html', 'Page 5'),
        # Page('r0/p1.html', 'Page 1'),
        # Page('r0/p2.html', 'Page 2'),
        # Page('r0/p2.html', 'Page 3'),
        # Page('r0/p1.html', 'Page 4'),
        # Page('r0/p1.html', 'Page 5'),

    ]
    p.render()
    print('ready')