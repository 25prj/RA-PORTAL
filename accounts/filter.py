import django_filters
from . models import *

#creating a class for filtering the queries

#filter class for type approvals
class typeApprovalFilter(django_filters.FilterSet):
    class Meta:
        model = TypeApproval
        fields = ('customer','company_name', 'status')
