from django import forms

from .models import Product

class ProductForm(forms.ModelForm):
    title = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            "placeholder": "Your title"
        }))
    email = forms.EmailField()
    description = forms.CharField(required=False
                                  ,widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                'class': "new-class-name two",
                'id':"my-id-for-textarea",
                'rows':20,
                'cols': 40
            }
        ))
    price = forms.CharField(initial=199.99)
    class Meta:
        model = Product
        fields = [

            'title',
            'description',
            'price'
        ]
    def clean_title(self,*args,**kwargs):
        title = self.cleaned_data.get('title')
        if not "CFE" in title:
            raise forms.ValidationError("This is not a valid title")
        return title
        #if "CFE" in title:
        #    return title
        #else:
        #    return forms.ValidationError("This is not a valid title")
    def clean_email(self,*args,**kwargs):
        email = self.cleaned_data.get("email")
        if not email.endswith("edu"):
            raise forms.ValidationError("This is not a valid Email")
        return email

class RawProductForm(forms.ModelForm):
    search = forms.CharField(label="")
    title = forms.CharField(label="",widget=forms.TextInput(
        attrs={
            "placeholder": "Your title"
        }))
    description = forms.CharField(required=False
                                  ,widget=forms.Textarea(
            attrs={
                "placeholder": "Your description",
                'class': "new-class-name two",
                'id':"my-id-for-textarea",
                'rows':20,
                'cols': 40
            }
        ))
    price = forms.CharField(initial=199.99)
    class Meta:
        model = Product
        fields = [
            'search',
            'title',
            'description',
            'price'
        ]
