from django.urls import path, include
from .views import DashboardView ,LeadDetailView ,LeadCreateView , login_view
from django.contrib.auth.views import LogoutView

app_name = 'dash'


urlpatterns = [
path('', DashboardView.as_view(), name='home'),
path('lead/<int:pk>/',LeadDetailView.as_view(),name='detail'),
path('lead/new',LeadCreateView.as_view(), name='lead_new'),
path('login/', login_view, name="login"),
path('logout/', LogoutView.as_view(), name="logout"),
#path('accounts/', include('django.contrib.auth.urls')),
#path('success/', success, name='user_success'),
#path('logout/', user_logout, name='user_logout'),
#path('profile/', MyProfile.as_view(), name='my_profile'),
]
