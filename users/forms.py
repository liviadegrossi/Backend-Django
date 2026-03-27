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

    password_1 = forms.CharField(
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

    password_2 = forms.CharField(
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

    def clean_username(self):
        # get the username provided by the user
        username = self.cleaned_data.get('username')

        if username:
            # clean blank spaces in the username
            username = username.strip()

            # check whether there is blank spaces in the username
            if ' ' in username:
                raise forms.ValidationError('Não pode haver espaço em branco no nome de usuário')
            else:
                return username
    
    def clean_password_2(self):
        password_1 = self.cleaned_data.get('password_1')
        password_2 = self.cleaned_data.get('password_2')

        if password_1 and password_2:
            if password_1 != password_2:
                raise forms.ValidationError('Senhas não são iguais')
            else:
                return password_2
        