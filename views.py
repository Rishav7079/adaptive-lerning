from django.shortcuts import render
from django.shortcuts                   import render,redirect
from django.http                        import HttpResponse, Http404, HttpResponseRedirect
from django.utils.decorators            import method_decorator
from django.contrib.auth.decorators     import login_required
from django.views.generic               import View, ListView
from django.views.generic.detail        import SingleObjectMixin, DetailView
from django.conf                        import settings
from django.template                    import loader
from django.contrib.auth.decorators     import login_required
import datetime
from django.core.exceptions             import ValidationError
from django.contrib                     import messages
from django.urls                        import reverse,reverse_lazy
from datetime                           import datetime
from pytz                               import timezone 
from django.conf                        import settings
from .models                            import Courses
from django.db.models                   import Q
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
import boto3

# Create your views here.

@login_required
def showCourses(request):
    course_object = Courses.objects.all()
    template = loader.get_template('/home/vivekkumarsingh/Test/vivekKumarSIngh/Navigus/CourseManager/cms/templates/showCouses.html')
    context = {'postInventoryUpdateDetails': course_object}
    return HttpResponse(template.render(context, request))
    # return render(request, template, {
    #     'postInventoryUpdateDetails' : course_object
    # })

def courseChange(request):
    return redirect("/admin/cms/courses/")