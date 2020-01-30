from django.shortcuts import render, redirect
from django.views import View
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

class RegisterFormView(View):
    form_class = UserCreationForm
    template_name = "user_registration/register.html"

    def get(self, request, *args, **kwargs):
        form = self.form_class()
        return render(request, self.template_name, {'form': form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            messages.success(request, f"Account created for {email}!")
            return redirect("website-home")
        
        return render(request, self.template_name, {'form': form})
    