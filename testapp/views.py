from django.core.files.storage import FileSystemStorage
from django.shortcuts import render, redirect
from .forms import UploadsForm
from .models import Uploads
from .xl_handler import *

'''def index(request):
    if request.method == 'POST':
        uploaded_file = request.FILES['document']
        fs = FileSystemStorage()
        fs.save(uploaded_file.name, uploaded_file)

    return render(request, 'testapp/index.html')'''

table = get_xl_values()

def index(request):
    if request.method == 'POST':
        form = UploadsForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('main')
    else:
        form = UploadsForm()

    files = Uploads.objects.order_by('upl_date')


    tab_titles = table[0]
    tab_vals = table[1:]
    return render(request, 'testapp/index.html', {
                                                    'form': form,
                                                    'files': files,
                                                    'tab_titles': tab_titles,
                                                    'tab_vals': tab_vals
                                                  }
                  )


