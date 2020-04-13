from django.contrib.auth import get_user_model
from django.contrib.auth.forms import UserCreationForm

class UserCreateForm(UserCreationForm):
    class Meta:
        fields = ('username', 'email', 'password1', 'password2')
        model = get_user_model()

    def __init__(self, *args, **kwargs):
        '''
        chose what you want to display instead of the generic name
        '''
        super().__init__(*args, **kwargs)
        self.fields['username'].label = "Username"
        self.fields['email'].lable = "Email Address"
