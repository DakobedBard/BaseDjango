from django import forms

class AudioFilesForm(forms.Form):
    def __init__(self, *args, **kwargs):
        files = kwargs.pop('files')
        super(AudioFilesForm, self).__init__(*args, **kwargs)
        counter = 1
        for q in files:
            #self.fields['files-' + str(counter)] = forms.CharField(label='file')
            self.fields[str(q)] = forms.BooleanField(required=False)
            counter += 1
