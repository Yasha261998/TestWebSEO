from django.shortcuts import render
from django.views.generic.base import View


class HomeViews(View):
    template_name = 'task_app/index.html'

    def get(self, request):
        return render(request, self.template_name)

