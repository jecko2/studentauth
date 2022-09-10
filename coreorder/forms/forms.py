from django import forms
from coreorder.models import InitialCalOrder
from coreorder.store.assignmentstore import SUBJECT_TYPE, ACC_LEVEL


class InitialOrderForm(forms.ModelForm):
    subject = forms.CharField(
        label=False,
        widget=forms.Select(
            choices=SUBJECT_TYPE,
            attrs={
            "class": "py-1 form-control form-control-lg"
            })
        )
    accademic_level = forms.CharField(
        label=False,
        widget=forms.Select(
            choices=ACC_LEVEL,
            attrs={
            "class": "form-control form-control-lg"
            })
        )
    pages = forms.IntegerField(
        label=False,
        widget=forms.NumberInput(attrs={
        "class": "form-control cl1",
        "placeholder": "(275words/pages)"
    }))
    class Meta:
        model = InitialCalOrder
        fields = ("subject", "accademic_level", "pages")
        
        

