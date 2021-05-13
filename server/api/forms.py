from django import forms

class BookMarkForm(forms.Form):
    bookMarkID = forms.IntegerField()