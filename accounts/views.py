from django.contrib.auth import login
from django.contrib.auth import views as auth_views
from django.contrib.auth.models import User
from django.shortcuts import render
from django.views import generic
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from accounts.forms import RegistrationForm
from accounts.models import UserProfile

# def register_user(req):
#     if req.user.is_authenticated:
#         return redirect('index')
#     if req.method == "GET":
#         context = {
#             'form': RegistrationForm
#         }
#         return render(req, 'register_user.html', context)
#     else:
#         form = RegistrationForm(req.POST)
#
#         if form.is_valid():
#             user = form.save()
#             profile = UserProfile(user=user)
#             profile.save()
#             login(req, user)
#
#             return redirect('index')
#
#         context = {
#             'form': form
#
#         }
#         return render(req, 'register_user.html', context)
from phones.models import Phone


class RegisterView(generic.CreateView):
    form_class = RegistrationForm
    template_name = 'register_user.html'
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        valid = super().form_valid(form)
        user = form.save()
        profile = UserProfile(user=user)
        profile.save()
        login(self.request, user)

        return valid


# @login_required
# def logout_user(req):
#     logout(req)
#     return redirect('index')

class LogoutUserView(LoginRequiredMixin, auth_views.LogoutView):
    next_page = reverse_lazy('index')


class LoginUserView(auth_views.LoginView):
    template_name = 'login.html'


def user_profile(req):
    user = req.user
    phones = [x for x in Phone.objects.all() if x.owner.user_id == user.id]
    if req.method == "GET":
        context = {
            'user': user,
            'phones': phones

        }
        return render(req, 'profile.html', context)

