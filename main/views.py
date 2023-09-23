from django.views import View
from django.shortcuts import render

class homeView(View):
    def get(self, request):
        context = {
            'title' : '메인화면제목',
            'content' : 'CI/CDTest 메인화면',
        }
        return render(request, 'home.html', context)
