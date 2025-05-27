from django import forms 
from artikel.models import Kategori, Artikel

class KategoriForms(forms.ModelForm):
    class Meta:
        model = Kategori
        fields = ['nama',]
        widgets = {
            'nama': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
        }

class ArtikelForms(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = ['kategori', 'judul', 'konten', 'gambar', 'status']
        widgets = {
            'kategori': forms.Select(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),

            'judul': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'konten': forms.Textarea(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'gambar': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
            'status': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'required': True
                }
            ),
        }