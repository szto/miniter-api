from django.http import JsonResponse, HttpResponse
from django.shortcuts import get_object_or_404
from .models import User
from django.views.generic import TemplateView
from .forms import IndexForm
from django.shortcuts import render
from django.views import View
import json

class IndexView(TemplateView):
    template_name = 'user/user.html'

    def get(self, request):
        form = IndexForm() 
        return render(request, self.template_name, {'form': form} )

    def post(self, request):
        form = IndexForm(request.POST)
        if form.is_valid():
            text = form.cleaned_data['post']
            form = IndexForm()
        
        args = { 'form': form, 'text': text}
        return render(request, self.template_name, args)

#def index(TemplateView):
#    template_name = 'user/user.html'

class UserView(View):
    
    def get(self, request, user_id):
        user=User.objects.get(id=user_id)

        return JsonResponse({'name':user.name})

    def post(self, request):
        new_user = json.loads(request.body)
        User(
            name = new_user['name']
        ).save()

        return HttpResponse(status=200)
    

#    def post(self, request):




#def detail(request, user_id):
#
#    data = get_object_or_404(User, pk=user_id)
#    return JsonResponse(
#            {
#                "data": data.id, 
#                "name": data.name
#            }
#        )

#def add(request, user_id):
#    return 0

# Create your views here.
