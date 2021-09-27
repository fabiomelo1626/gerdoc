from django.shortcuts import render
from django.views.generic import CreateView
from .forms import DocumentosForm
from .models import *


class NovoDocumento(CreateView):
    form_class = DocumentosForm
    