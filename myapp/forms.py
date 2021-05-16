from django import forms
from django.core.exceptions import ValidationError
from myapp.models import Person, MusicalStoreReg

class FirstNameForm(forms.Form):

    first_name = forms.CharField(max_length=50, required=True)
    email = forms.EmailField()

    def clean_email(self):
        email = self.cleaned_data['email']
        person_count = Person.objects.filter(email=email).count()

        if person_count == 0:
            return email
        else:
            raise ValidationError("A person with this email exists already!")

    def clean_first_name(self):
        """ Custom clean method following the patter clean_<YOUR FIELD NAME>
            Raise ValidationError to add error form
            Return clean field value if there is no error
        """

        if self.cleaned_data['first_name'] == 'Steve':
            raise ValidationError("Steve is a terrible name.")

        return self.cleaned_data['first_name']


    def clean(self):
        """ THis cleans stuff
        """
        return self.cleaned_data

"""class MusicalstoreRegform(forms.ModelForm):
    class Meta:
        model= MusicalStoreReg
        fields= ["Firstname", "Lastname", "Email", "Mobile", "Image", "Username", "Password", "Created", "Updated"]"""

class MusicalstoreRegform(forms.Form):

    firstname = forms.CharField(label='Firstname', max_length=255)
    lastname = forms.CharField(label='Lastname', max_length=255)
    email = forms.EmailField(label='Email')
    mobile = forms.CharField(label='Mobile', max_length=10)
    img = forms.ImageField(label='Image')
    status = forms.BooleanField(label='Status')
    username = forms.CharField(label='Username', max_length=255)
    password = forms.CharField(label='Password', max_length=255)
    created = forms.DateTimeField(label='Created')
    updated = forms.DateTimeField(label='Updated')