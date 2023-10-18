from typing import Any
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.paginator import Paginator
from django.db.models.query import QuerySet
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from . import models, forms
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.urls import reverse, reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.decorators import login_required


def index(request):
    return render(request, "kirpykla/index.html")

def about_us(request):
    about_us_content = models.AboutUs.objects.first()
    return render(
        request,
        "kirpykla/about_us.html",
        {"about_us_content": about_us_content}
    )


class ServiceListView(ListView):
    model = models.Service
    template_name = 'kirpykla/service_list.html'
    context_object_name = 'services'


def book_service(request):
    if request.method == 'POST':
        form = forms.ServiceOrderForm(request.POST)
        if form.is_valid():
            form.instance.customer = request.user
            form.save()
            return redirect('booking_success')
    else:
        form = forms.ServiceOrderForm()
    return render(request, 'kirpykla/booking_form.html', {'form': form})

def booking_success(request):
    return render(request, 'kirpykla/booking_success.html')

