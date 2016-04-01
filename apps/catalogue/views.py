from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse, HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.template import loader
from .models import ProductItem, ProductType, OptionGroup


def Product1View(request):
    list = ProductItem.objects.filter(product_type__name="test1").filter(status="p").distinct()
    template = loader.get_template('catalogue/list1.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))


def Product2View(request):
    type = ProductType.objects.filter(name="krovati")
    #list = ProductItem.objects.filter(product_type=type)
    template = loader.get_template('catalogue/list2.html')
    context = {
        'list': list,
    }
    return HttpResponse(template.render(context, request))


def AkciiView(request):
    list = ProductItem.objects.all()
    for e in list:
        print(e.name)
    template = loader.get_template('catalogue/akcii.html')
    context = {
        'products': list,
    }
    return HttpResponse(template.render(context, request))


def index(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'catalogue/index.html',
        context_instance = RequestContext(request,
        {
            'title':'Home Page',
            'year':datetime.now().year,
        })
    )


def product_detail(request, product_id):
    product = ProductItem.objects.get(id=product_id)
    product_options = OptionGroup.objects.filter(producttype__id=(ProductType.objects.filter(type__in=product_id)))
    template = loader.get_template('catalogue/detail.html')
    context = {
        'product': product,
        'product_options': product_options,
    }
    return HttpResponse(template.render(context, request))

