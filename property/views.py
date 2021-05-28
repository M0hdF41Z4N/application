from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView

# Create your views here.

class HomePageView(TemplateView):
    template_name = 'property/home.html'

class SliderView(TemplateView):
    template_name = 'property/slider.html'

class RecommendPageView(TemplateView):
    template_name = 'property/recommend.html'

class LoginPageView(TemplateView):
    template_name = 'property/login.html'
