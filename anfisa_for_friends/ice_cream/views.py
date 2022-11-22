from django.shortcuts import render


def ice_cream_detail(request, pk):
    template = 'ice_cream/detail.html'
    context = {}
    return render(request, template, context)


def ice_cream_list(request):
    template = 'ice_cream/list.html'
    context = {}
    return render(request, template, context)
