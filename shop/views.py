from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.views.generic.list import ListView
from django.urls import reverse_lazy, reverse
from django.views.generic import DetailView, TemplateView, CreateView, DeleteView
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
    template_name = 'new_listing.html'
    success_url = reverse_lazy('item-list-page')

class DeleteItem(DeleteView):
    model = Listing
    template_name = 'item_delete.html'

    def get_object(self):
        slug = self.kwargs.get('slug')
        return get_object_or_404(Listing, slug=slug)

    def get_success_url(self):
        return reverse('item-list-page')