from django.views.generic import ListView
from .models import User
from django.views.generic import DetailView
from .models import User

class UserDetailView(DetailView):
    model = User
    template_name = 'user_detail.html'

class UserListView(ListView):
    model = User
    template_name = 'user_list.html'
