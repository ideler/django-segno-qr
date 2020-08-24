import segno
from io import BytesIO
from django import template
from django.utils.safestring import mark_safe


register = template.Library()


@register.simple_tag
def segno_qr(content, size=5, border=None, dark="black",
             light=None, micro=False, **kwargs):
    kwargs.update({'micro': micro})

    qr = segno.make(content, **kwargs)
    svg = BytesIO()
    qr.save(svg, 'svg', scale=size, dark=dark, light=light)
    result = svg.getvalue().decode('utf8')
    return mark_safe(result)
