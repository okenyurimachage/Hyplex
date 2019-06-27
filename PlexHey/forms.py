from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordChangeForm
from django.contrib.auth.models import User
from django import forms
from django.core.exceptions import ValidationError
from .models import Profile, booking


class EditProfileForm(UserChangeForm):
    password = forms.CharField(widget=forms.TextInput(attrs={'type': 'hidden'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password')

    def __init__(self, *args, **kwargs):
        super(EditProfileForm, self).__init__(*args, **kwargs)

        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'
class EditProfile(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Identification_Number', 'Age', 'Driving_license', 'Phone_Number', 'image')

class PasswordForm(PasswordChangeForm):
        class Meta:
            model = User
            fields = ('old_password', 'new_password1', 'new_password2',)
            help_texts = {
                'new_password1': None,

            }

        def __init__(self, *args, **kwargs):
            super(PasswordForm, self).__init__(*args, **kwargs)

            self.fields['old_password'].widget.attrs['class'] = 'form-control'
            self.fields['old_password'].widget.attrs['placeholder'] = 'Enter Old Password'
            self.fields['new_password1'].widget.attrs['class'] = 'form-control'
            self.fields['new_password1'].widget.attrs['placeholder'] = 'Enter New Password'
            self.fields['new_password1'].help_text = '<ul class="form-text text-muted"> <small>' \
                                                 '<li>Your password can\'t be too similar to your other personal information.</li>' \
                                                 '<li>Your password must contain at least 8 characters.</li>' \
                                                 '<li>Your password can\'t be a commonly used password.</li>' \
                                                 '<li>Your password can\'t be entirely numeric.</li>' \
                                                 '</ul> </small>'
            self.fields['new_password2'].widget.attrs['class'] = 'form-control'
            self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirm New Password'




class SignUpForm(UserCreationForm):
    email = forms.EmailField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter Email'}))
    first_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'pattern' : '[a-z]+', 'placeholder': 'Enter First Name'}))
    last_name = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={'class': 'form-control', 'pattern' : '[a-z]+', 'placeholder': 'Enter Last Name'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2',)
        help_texts = {
            'username': None,
            'password1': None,
            'password2': None,
        }


    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].label = '<strong>"Username "</strong>'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields[
            'username'].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password1'].help_text = '<ul class="form-text text-muted"> <small>' \
                                             '<li>Your password can\'t be too similar to your other personal information.</li>' \
                                             '<li>Your password must contain at least 8 characters.</li>' \
                                             '<li>Your password can\'t be a commonly used password.</li>' \
                                             '<li>Your password can\'t be entirely numeric.</li>' \
                                             '</ul> </small>'

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        # self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirm Password'
        self.fields[
            'password2'].help_text = '<span class="form-text text-muted"><small>Enter the same password as before, for verification.</small></span>'


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('Identification_Number', 'Age', 'Driving_license', 'Phone_Number','image')


        widgets = {
            'Identification_Number': forms.NumberInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Enter ID Number'}),
            'Age': forms.NumberInput(attrs={'required': True, 'class': 'form-control', 'placeholder': 'Enter Age'}),
            'Driving_license': forms.FileInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Enter Driving license Number'}),
            'Phone_Number': forms.NumberInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Enter Phone Number'}),
            'image': forms.FileInput(
                attrs={'required': True, 'class': 'form-control', 'placeholder': 'Enter Phone Number'})

        }
        
    def clean_Age(self, *args, **kwargs):
        Age = self.cleaned_data.get('Age')
        if Age > 21:
            return Age
        else:
            
            raise forms.ValidationError('Too young to borrow a vehicle ')
    
