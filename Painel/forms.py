from django import forms
from .models import DataInfo


# creating a form
class CovidForm(forms.ModelForm):
    # create meta class

    def __init__(self, *args, **kwargs):
        super(CovidForm, self).__init__(*args, **kwargs)
        self.fields['name']=forms.CharField(max_length=200)


        for name in self.fields.keys():
            self.fields[name].widget.attrs.update({
                'class': 'form-control',
            })

    class Meta:
        # specify model to be used
        model = DataInfo

        # specify fields to be used
        fields = [
            "confirmedCases",
            "deaths",
            "recovered",
        ]
