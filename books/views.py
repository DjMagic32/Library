from django.shortcuts import render
from django.views.generic import ListView
from .models import book

# Create your views here.


class BookListView(ListView):
    model = book
    template_name = 'book_list.html'
