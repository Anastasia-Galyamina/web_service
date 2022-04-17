from django.shortcuts import render

from clusterization.clusterization.forms import UploadFileForm


def index(request):
    #надо передать файл или пустое место
    return render(request, 'clusterization/Index.html')

def info(request):
    return render(request, 'clusterization/Info.html')

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            #return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    #return render(request, 'upload.html', {'form': form})
    #file = request.FILES['file']
    return render(request, 'clusterization/Index.html')

#если загруженный файл меньше 2,5 мегабайт, Django будет хранить все содержимое загруженного файла в памяти
def handle_uploaded_file(f):
    with open('some/file/name.txt', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)