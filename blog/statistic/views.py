from django.shortcuts import render
from django.http import HttpResponse

from .models import Visitor, VisitorHistory

# Create your views here.
def add_visitor_history(request):
    remote_addr = request.META.get('REMOTE_ADDR')
    visitor = Visitor.objects.filter(ip=remote_addr).first()
    if visitor:
        visitor_history = VisitorHistory.objects.create(visitor_id=visitor.vid)
        visitor_history.save()
        Visitor.objects.filter(vid=visitor.vid).update(cnt=visitor.cnt+1)
    else:
        visitor = Visitor.objects.create(ip=remote_addr)
        visitor.save()
        visitor_history = VisitorHistory.objects.create(visitor_id=visitor.vid)
        visitor_history.save()
    #return HttpResponse("OK") 


def show_visitor_history(request):
    add_visitor_history(request)
    callback = request.GET.get('callback')
    visitors =[{'ip': visitor.ip, 'count':visitor.cnt} for visitor in Visitor.objects.all()]
    return HttpResponse(('%s(%s)') % (callback, visitors))
