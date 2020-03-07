from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.views.generic import DetailView, CreateView
from shop.models import Listing
from datetime import timezone
# Create your views here.


class ItemListView(ListView):
    model = Listing

    def get(self, request):
        listing = self.get_queryset().all()
        return render(request, 'list.html', {'listing': listing})

class ItemDetailView(DetailView):
    model = Listing

    def get(self,request,slug):
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {'page': page})
