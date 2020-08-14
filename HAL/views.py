from django.shortcuts import render


def base_foot(request):
    return render(request,'base_foot.html')