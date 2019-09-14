from django import template
from django.contrib.humanize.templatetags.humanize import intcomma
from django.utils.encoding import force_text

def formataReal(real):
    if real:
        real = round(float(real), 2)
        return "R$ %s%s" % (intcomma(int(real)), ("%0.2f" % real)[-3:])
    else:
        return ''

def formataReal2(real):
    val_text = force_text(real)
    try:
        val_new = int(val_text)
    except ValueError:
        return ''
    
    val_new = '{:,d}'.format(val_new)
    val_new = val_new.replace(',', '.')
    return val_new

def formataPreco(x):
    return '{0:,}'.format(str(x)).replace(',','.')