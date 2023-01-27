from django.shortcuts import render

from django.views.generic import TemplateView

class adminHome(TemplateView):
    def get(self,request, *args, **kwargs):
        return render(request,'backend/home.html')
        