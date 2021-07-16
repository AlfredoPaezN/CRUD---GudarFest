from django.contrib.auth.mixins import LoginRequiredMixin
from django.db import models
from django.urls.base import reverse_lazy
from crud.forms import PersonForm
from crud.models import Person
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.urls import reverse
from django.views.generic.edit import CreateView, DeleteView, FormMixin, UpdateView


class PersonUpdateView(LoginRequiredMixin, UpdateView):
    form_class = PersonForm
    model = Person
    success_url = reverse_lazy('crud')
    template_name = 'users/person_detail.html'

class PersonDeleteView(LoginRequiredMixin, DeleteView):
    model = Person
    success_url = reverse_lazy('crud')

class PersonCreateView(LoginRequiredMixin, CreateView):
    model = Person
    template_name = 'users/person_create.html'
    form_class = PersonForm
    success_url = reverse_lazy('crud')
