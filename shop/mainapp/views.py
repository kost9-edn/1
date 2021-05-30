from django.shortcuts import render

def test_viev(request):
    return render(request, 'base.html', {})
