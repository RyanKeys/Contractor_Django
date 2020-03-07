from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.views.generic.list import ListView
from django.urls import reverse_lazy
from django.views.generic import DetailView, TemplateView, CreateView
from shop.models import Listing
from datetime import timezone
from shop.forms import AddItem
# Create your views here.


class ItemListView(ListView):
    model = Listing
    template_name = "list.html"

    def get(self, request):
        listing = self.get_queryset().all()
        return render(request, 'list.html', {'listing': listing})

class ItemDetailView(DetailView):
    model = Listing

    def get(self,request,slug):
        page = self.get_queryset().get(slug__iexact=slug)
        return render(request, 'page.html', {'page': page})

class NewItem(CreateView):
    form_class = AddItem
    success_url = reverse_lazy('shop-details-page')
    template_name = 'new_listing.html'