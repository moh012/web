
from django import forms
from .models import Financial_Movement

class fmForm(forms.ModelForm):
    class Meta:
        model = Financial_Movement
        fields = ['reference', 'img']

        labels = {

            'reference': 'رقم العملية أو (الحوالة)',
            'img': 'ارفع الصورة '
        }

        widgets = {
            'reference': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'أدخل الرقم هنا'}),
            'img': forms.FileInput(attrs={'class': 'form-control-file'})
        }
