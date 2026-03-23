from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(
        label='Nome de login',
        required=True,
        max_length=100,
        widget=forms.TextInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com"
            }
        )
    )

    password = forms.CharField(
        label='Senha',
        required=True,
        max_length=60,
        widget=forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

class RegistrationForm(forms.Form):
    username = forms.CharField(
        label = 'Nome completo',
        required = True,
        max_length=100,
        widget=forms.TextInput(
            attrs= {
                "class": "form-control",
                "placeholder": "Ex.: João Silva"
            }
        )
    )

    email = forms.EmailField(
        label="Email",
        required=True,
        max_length=100,
        widget= forms.EmailInput(
            attrs={
                "class": "form-control",
                "placeholder": "Ex.: joaosilva@xpto.com"
            }
        )
    )

    senha_1 = forms.CharField(
        label='Senha',
        required=True,
        max_length=60,
        widget = forms.PasswordInput(
            attrs={
                "class": "form-control",
                "placeholder": "Digite sua senha"
            }
        )
    )

    senha_2 = forms.CharField(
        label='Confirmação de senha',
        required=True,
        max_length=60,
        widget = forms.PasswordInput(
            attrs = {
                "class": "form-control",
                "placeholder": "Digite sua senha mais uma vez"
            }
        )
    )