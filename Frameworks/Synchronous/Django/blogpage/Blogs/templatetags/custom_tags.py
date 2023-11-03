from django.template import Library
from bs4 import BeautifulSoup

register = Library()

@register.simple_tag
def inject_html(html_as_string: str):
    soup = BeautifulSoup(html_as_string, "html.parser")
    soup.find("div", attrs={"id":"blog-content"}).insert(0, )
    return 
