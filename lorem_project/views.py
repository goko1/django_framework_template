from django.http import HttpResponse
from django.shortcuts import render

# index , about, contact

def show_index(request):
    lorem ="jdhfkjhsdjkfhjkdhsjkhfjkdshfjksdhsdhghfgsdhgfsdffffffffffffffffffffffffffffffffffffffffffffffffffffweyfgeglwegyfgwelfweygfgewlfeyfefyefefıefegıfeıefııgfıeıfıeffegf"

    names = [
        'ibrahim',
        'umit',
        'guven',
        'suayip',
        'yusuf',
    ]

    return render(
        request,
        'index.html',
        {"title": "Index page",# title dictionaryi üste context olarak tanımlayıp gönderebilirim.
        "url" : "https://google.com.tr" ,
        "names" : names,
        "lorem" : lorem,
        }
    )

def show_about(request):
    return render(
        request,
        'about.html',
        {"title": "About page"}
    )
    

def show_contact(request):
    return render(
        request,
        'contact.html',
        {"title": "Contact page"}
    )