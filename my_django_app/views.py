from django.shortcuts import HttpResponse, redirect
from django.http import JsonResponse

def index(request):
    return HttpResponse("placeholder to later display a list of all blogs")

def root(request):
    return redirect("/blogs")

def new(request):
    return HttpResponse("Placeholder to display a new form to create a new blog")

def redirect_new(request):
    return redirect('/blogs/new')

def create(request):
    return redirect('/')

def show(request, number):
    return HttpResponse("Placeholder to display blog number: {number}".format(number=number))

def edit(request, number):
    return HttpResponse("Placeholder to edit blog {number}".format(number=number))

def destroy(request, number):
    return redirect('/blogs')

# def hell_yeah(request, title, content):
#     title = None
#     content = None
#     responseData = {
#         title: "My first blog",
#         content: "This the content of a JsonResponse..."
#     }
#     return JsonResponse(responseData)

