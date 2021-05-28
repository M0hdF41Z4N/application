from django.shortcuts import render , redirect
from django.utils.timezone import datetime
from django.views import View
from django.views.generic import ListView , DetailView
from django.views.generic.edit import CreateView
from .models import Lead
from .forms import LeadCreateForm , LoginForm
from django.contrib.auth import authenticate, login
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
"""class Dashboard(LoginRequiredMixin, UserPassesTestMixin, View):
    def get(self, request, *args, **kwargs):
        today = datetime.today()
        orders = OrderModel.objects.filter(created_on__year=today.year,
          created_on__month=today.month, created_on__day=today.day)
        total_revenue = 0        for order in orders:
            total_revenue += order.price

        context = {
            'orders': orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }
        return render(request, 'restaurant/dashboard.html', context)"""


# Dashboard View
class DashboardView(LoginRequiredMixin,ListView):  #(DetailView):
    login_url = 'login/'
    model = Lead
    template_name = 'dash/home.html'

# Leads Detail View
class LeadDetailView(LoginRequiredMixin,DetailView):
    login_url = 'login/'
    model = Lead
    template_name = 'dash/lead_detail.html'


"""def LeadCreateView(request):
    context = {}

    # Create object to form
    form = LeadCreateForm(request.POST or None, request.FILES or None)

    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()
    context['form']= form
    return render(request, "dash/home.html", context)"""


class LeadCreateView(LoginRequiredMixin,CreateView):
    login_url = 'login/'
    template_name = 'dash/lead_new.html'
    form_class = LeadCreateForm

    def form_valid(self,form):
        form.instance.created_by = self.request.user
        return super().form_valid(form)

def login_view(request):
    form = LoginForm(request.POST or None)

    msg = None

    if request.method == "POST":

        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("/")
            else:
                msg = 'Invalid credentials'
        else:
            msg = 'Error validating the form'

    return render(request, "dash/login.html", {"form": form, "msg" : msg})
