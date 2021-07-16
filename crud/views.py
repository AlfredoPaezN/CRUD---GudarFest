from .models import Person
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin


class CrudListView(LoginRequiredMixin, ListView):
    paginate_by = 20
    template_name = 'crud/index.html'
    queryset = Person.objects.all().order_by('-id')
    context_object_name = 'people'

