from django import forms

def file_path():
    return '/{0}'.format('temp.txt')

# Our form that will allow us to upload a file
class uploadFileForm(forms.Form):
    # This will allow us to upload our file to the MEDIA_ROOT/path location
    fileUpload = forms.FileField(upload_to=file_path)

# Our form that will allow us to download a file
#class downloadFileForm(forms.Form):
