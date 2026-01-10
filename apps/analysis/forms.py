from django import forms

class AnalysisForm(forms.Form):
    address = forms.CharField(
        label="Address",
        max_length=255,
        widget=forms.TextInput(attrs={
            "placeholder": "Enter address or area "
        })
    )
