from django.shortcuts import render


def show_phones(request):
    return render(request, 'where_to_go/index.html')
