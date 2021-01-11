from django.contrib.auth.forms import UserCreationForm


class RegistrationForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for (_, fields) in self.fields.items():
            fields.widget.attrs['class'] = 'form-control'