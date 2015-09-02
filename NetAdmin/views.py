from django.shortcuts import render
from django.http import HttpResponseRedirect , HttpResponse
import settings
import os
from django.template import RequestContext
from django.core.servers.basehttp import FileWrapper
import mimetypes
from django.utils.encoding import smart_str

def landing_page_view(request):
    return render(request, 'landing.html')

def index_page_view(request):
    if request.user.is_authenticated():
        if request.user.is_student:
            return HttpResponseRedirect('/student/')
        elif request.user.is_TA:
            return HttpResponseRedirect('/ta/')
        elif request.user.is_admin:
            return HttpResponseRedirect('/agent/')
        elif request.user.is_parents:
            return HttpResponseRedirect('/parents/')
    else:
        return HttpResponseRedirect('/account/login/')

def files_list(request):
    return render(request, 'file_list.html', {'total_files': os.listdir(settings.MEDIA_ROOT), 'path': settings.MEDIA_ROOT},
                  context_instance=RequestContext(request))

def download(request,file_name):
    file_path = settings.MEDIA_ROOT +'/'+ file_name
    file_wrapper = FileWrapper(file(file_path,'rb'))
    file_mimetype = mimetypes.guess_type(file_path)
    response = HttpResponse(file_wrapper, content_type=file_mimetype )
    response['X-Sendfile'] = file_path
    response['Content-Length'] = os.stat(file_path).st_size
    response['Content-Disposition'] = 'attachment; filename=%s' % smart_str(file_name)
    return response
