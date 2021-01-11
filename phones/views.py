import os

from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from phones.forms import PhoneForm
from phones.models import Phone


def index(req):
    if req.user.is_authenticated:
        return render(req, 'home_auth.html')
    return render(req, 'home.html')


# @login_required
# def show_phones(req):
#     phones = Phone.objects.all()
#     context = {
#         'phones': phones,
#         'user': req.user
#
#     }
#     return render(req, 'phones.html', context)
class ShowPhonesView(LoginRequiredMixin,generic.ListView):
    model = Phone
    template_name = 'phones.html'
    context_object_name = 'phones'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['user'] = self.request.user
        return context
# @login_required
# def add_phone(req):
#     if req.method == "GET":
#         context = {
#             'form': PhoneForm()
#         }
#         return render(req, 'add_phone.html', context)
#     else:
#         form = PhoneForm(req.POST, req.FILES)
#         if form.is_valid():
#             phone = form.save(commit=False)
#             phone.owner = req.user
#             phone.save()
#             return redirect('phones')
#
#         context = {
#             'form': form,
#         }
#
#         return render(req, 'add_phone.html', context)


class CreatePhoneView(LoginRequiredMixin, generic.CreateView):
    template_name = 'add_phone.html'
    model = Phone
    form_class = PhoneForm

    def get_success_url(self):
        return reverse_lazy('details phone', kwargs={'pk': self.object.id})

    def form_valid(self, form):
        phone = form.save(commit=False)
        phone.owner = self.request.user.userprofile
        phone.save()
        # return redirect('details phone', phone.id)
        return super().form_valid(form)


# def delete_phone(req, pk):
#     phone = Phone.objects.get(pk=pk)
#     if not req.user.is_superuser and phone.owner.user != req.user:
#         return redirect('index')
#     form = PhoneForm(instance=phone)
#     if req.method == "GET":
#         context = {
#             'form': form,
#             'phone': phone
#         }
#         return render(req, 'delete_phone.html', context)
#     else:
#         phone.picture.delete()
#         phone.delete()
#         return redirect('phones')


class DeletePhoneView(LoginRequiredMixin, generic.DeleteView):
    model = Phone
    template_name = 'delete_phone.html'
    success_url = reverse_lazy('phones')

    def dispatch(self, request, *args, **kwargs):
        phone = self.get_object()
        if not phone.owner.id != request.user.id and not request.user.is_superuser:
            return self.handle_no_permission()
        # if phone.picture:
        #     os.remove(phone.picture.path)
        return super().dispatch(request, *args, **kwargs)


def edit_phone(req, pk):
    phone = Phone.objects.get(pk=pk)
    old_image = phone.picture
    if not req.user.is_superuser and phone.owner.user != req.user:
        return redirect('index')
    if req.method == 'GET':
        context = {
            'form': PhoneForm(instance=phone),
            'phone': phone
        }
        return render(req, 'phone_edit.html', context)
    else:
        form = PhoneForm(
            req.POST,
            req.FILES,
            instance=phone,
        )
        if form.is_valid():
            form.picture = form.cleaned_data["picture"]
            form.save()

            if form.picture != old_image:
                os.remove(old_image.path)
            return redirect('details phone',phone.pk)
        context = {
            'form': form
        }
        return render(req, 'phone_edit.html', context)



class EditPhoneView(LoginRequiredMixin, generic.UpdateView):
    template_name = 'phone_edit.html'
    model = Phone
    form_class = PhoneForm

    def get_success_url(self):
        url = reverse_lazy('details phone', kwargs={'pk': self.object.id})
        return url

    def form_valid(self, form):
        old_image = self.get_object().picture
        if old_image:
            os.remove(old_image.path)
        return super().form_valid(form)


def details_phone(req, pk):
    phone = Phone.objects.get(pk=pk)
    owner = User.objects.get(pk=phone.owner.user.id)
    context = {
        'owner': owner,
        'phone': phone
    }
    return render(req, 'phone_details.html', context)

# ZSjY4JJdfjUc+G7
