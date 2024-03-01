from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from core.models import Product

def index(request):
    products = Product.objects.all()

#    if str(request.user) == "AnonymousUser":
#        status = "Não logado"
#    else:
#        status = "Logado"

    context = {
        "curso": "Programação Web com Django Framework",
        "outro": "Nossa, que legal!",
        "produtos": products
#       "status": status
    }
    return render(request, "index.html", context)

def contact(request):
    return render(request, "contact.html")

def product(request, id):
#    product = Product.objects.get(id=id)
    product = get_object_or_404(Product, id=id)

    context = {
        "produto": product
    }

    return render(request, "product.html", context)

def error404(request, exception):
    template = loader.get_template("404.html")
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=404)

def error500(request):
    template = loader.get_template("500.html")
    return HttpResponse(content=template.render(), content_type="text/html; charset=utf8", status=500)