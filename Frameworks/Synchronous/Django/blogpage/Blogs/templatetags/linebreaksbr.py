from django.template.library import Library
from django.utils.safestring import mark_safe
from django.utils.text import normalize_newlines
import re

register = Library()

@register.filter(is_safe=True, needs_autoescape=True)
def linebreaksbr(value, bootstrap_class, autoescape=True):
  """
  Converts line breaks to `<br>` tags.
  """
  value = normalize_newlines(value)

  value = '<p class="p-1">' + value
  value = re.sub(r'(\<br\>){2,}|(\n)+|(\r)+', '</p><p class="p-1">', value)
  value += '</p>'

  return mark_safe(f'<div class="{bootstrap_class}" id="html-content">{value}</div>')
