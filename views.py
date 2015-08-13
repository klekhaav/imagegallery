from django.shortcuts import get_object_or_404, render
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views import generic
from django.utils import timezone

# Create your views here.
from .models import Image, Author

class IndexView(generic.ListView):
    template_name = 'image/index.html'
    context_object_name = 'latest_added_image'

    def get_queryset(self):
        return Image.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:9]

class DetailView(generic.DetailView):
    model = Image
    template_name = 'image/detail.html'
    def get_queryset(self):
        return Image.objects.filter(pub_date__lte=timezone.now())