from authtools.views import LoginView
from django.contrib.auth.forms import AuthenticationForm


class CustomAuthenticationForm(AuthenticationForm):
    def clean_username(self):
        return self.cleaned_data['username'].strip().lower()


class CustomLoginView(LoginView):
    form_class = CustomAuthenticationForm
