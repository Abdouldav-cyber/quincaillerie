# C:\Users\ASUS\Desktop\ProjetsDjango\quincaillerie\quincaillerie\rapports\templatetags\custom_filters.py
from django import template

register = template.Library()

@register.filter
def multiply(value, arg):
    """
    Multiplie deux valeurs.
    """
    try:
        return float(value) * float(arg)
    except (ValueError, TypeError):
        return 0

@register.filter
def mul(value, arg):
    """
    Alias pour multiply.
    """
    return multiply(value, arg)

@register.filter
def filter_by_stock_critique(stocks):
    """
    Filtre les stocks pour ne conserver que ceux dont la quantité est inférieure au seuil critique.
    """
    return [stock for stock in stocks if stock.quantite < stock.seuil_critique]