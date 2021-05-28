from django.urls import path
from .views import HomePageView , SliderView ,RecommendPageView ,LoginPageView

app_name = 'property'

urlpatterns = [
path('', HomePageView.as_view(), name='home'),
path('slider/', SliderView.as_view(), name='slider'),
path('recommend/',RecommendPageView.as_view(), name='recommend'),
path('login/',LoginPageView.as_view(), name='login'),
]
