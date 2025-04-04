from django.shortcuts import render
from django.http import Http404, HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib import messages
from . import util

def index(request):
    arr = util.list_entries()
    newArr = []
    if 'q' in request.GET:
        q = request.GET['q'] 
        if q in arr:
            return HttpResponseRedirect(reverse('open', args=[q]))
        else:
            for i in arr:
                if q in i:
                    newArr.append(i)
    else:
        newArr = arr
    context = {'entries': newArr}
    return render(request, "encyclopedia/index.html", context)
    
def open(request, title):
    x = util.get_entry(title)
    if not x:
        messages.error(request, 'Such file does not exist.')
        response = render(request, 'encyclopedia/404.html')
        response.status_code = 404
        return response
    context = {'name': title, 'content': x}
    return render(request, 'encyclopedia/open.html', context)

def create(request):
    arr = util.list_entries()
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        if title in arr:
            messages.error(request, 'There already exists such file')
            response = render(request, 'encyclopedia/404.html')
            response.status_code = 404
            return response
        else:
            util.save_entry(title, content)
            return HttpResponseRedirect(reverse('open', args=[title]))
    return render(request, 'encyclopedia/create.html')