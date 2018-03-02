import django_tables2 as tables
from table.models import Variants

class VariantTable(tables.Table):
    class Meta:
        model = Variants
        template_name = 'django_tables2/bootstrap.html'
