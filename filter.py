
from sys import stderr
from panflute import *

headers = []

def prepare(doc):
    doc.replace_keyword("BOLD", Strong(Str("BOLD")))

def upper_headers(elem, doc):
    if isinstance(elem, Header) and elem.level > 2:
        return Header(Str(stringify(elem).upper), level=elem.level)


"""
Функция, которая делала слово BOLD жирным. Закоментирована, потому что переписана лучше

def bolder(elem, doc):
    if isinstance(elem, Para):
        content = elem.content
        new_content = []
        for el in content:
            if isinstance(el, Str) and el.text == "BOLD":
                new_content.append(Strong(el))
            else:
                new_content.append(el)
        return Para(*new_content)
"""

def header_attention(elem, doc):
    if isinstance(elem, Header):
        text = stringify(elem)
        if text in headers:
            print("Повторные заголовки: " + text, file=stderr)
        else:
            headers.append(text)


def finalize(doc):
    pass

def main(doc=None):
    return run_filters([upper_headers, header_attention], prepare=prepare, finalize=finalize, doc=doc)

if __name__ == '__main__':
    main()
