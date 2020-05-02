from django.shortcuts import render
from django.template import loader
import classes.objectmanager

# Create your views here.

from django.http import HttpResponse


def index(request):
    return HttpResponse("Hello, world. You're at the node admin index.")

def createNodeRequest (request):
    template = loader.get_template('nodeAdmin/createNode.html')
    if (len(request.POST) == 0):
        return HttpResponse(template.render(context = None, request=request)) 
    else:
        classes.objectmanager.createNode(name = request.POST['name'], 
                                         remoteAddress = request.POST['remoteAddress'], 
                                         maxUpBw = request.POST['maxUpBw'], 
                                         maxDownBw = request.POST['maxDownBw'], 
                                         maxSpace = request.POST['maxSpace']
                                         )
        
        context = {
                   'info_message': "Node: "+request.POST['name']+" created successfully",
                   }
        return HttpResponse(template.render(context, request=request)) 