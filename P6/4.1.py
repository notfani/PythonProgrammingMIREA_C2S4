class HTML:
    def __init__(self):
        self.code = []

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        pass

    def get_code(self):
        return '\n'.join(self.code)

    def _add_tag(self, tag, content=''):
        if content:
            self.code.append(f'<{tag}>{content}</{tag}>')
        else:
            self.code.append(f'<{tag}>')
            self.code.append(f'</{tag}>')

    def body(self):
        return TagManager(self, 'body')

    def div(self):
        return TagManager(self, 'div')

    def p(self, content):
        self._add_tag('p', content)


class TagManager:
    def __init__(self, html, tag):
        self.html = html
        self.tag = tag

    def __enter__(self):
        self.html._add_tag(self.tag)
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.html._add_tag(self.tag)

# Пример использования
html = HTML()
with html.body():
    with html.div():
        with html.div():
            html.p('Первая строка.')
            html.p('Вторая строка.')
        with html.div():
            html.p('Третья строка.')

print(html.get_code())
