from django.shortcuts import redirect
from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import TemplateView, CreateView, ListView, UpdateView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Stock
from .forms import RegisterForm, StockForm

class HomeView(TemplateView):
    template_name = 'home.html'

class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'register.html'
    success_url = reverse_lazy('login')

class CustomLoginView(LoginView):
    template_name = 'login.html'
    authentication_form = AuthenticationForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('dashboard')

class CustomLogoutView(LogoutView):
    next_page = reverse_lazy('login')

class DashboardView(LoginRequiredMixin, ListView):
    model = Stock
    template_name = 'dashboard.html'
    context_object_name = 'stocks'

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)

class AddStockView(LoginRequiredMixin, CreateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_form.html'
    success_url = reverse_lazy('dashboard')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class UpdateStockView(LoginRequiredMixin, UpdateView):
    model = Stock
    form_class = StockForm
    template_name = 'stock_form.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)

class DeleteStockView(LoginRequiredMixin, DeleteView):
    model = Stock
    template_name = 'stock_confirm_delete.html'
    success_url = reverse_lazy('dashboard')

    def get_queryset(self):
        return Stock.objects.filter(user=self.request.user)
