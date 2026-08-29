from django.shortcuts import render,redirect

from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout
from django.urls import reverse_lazy
from .models import Task


def logout_user(request):
    logout(request)
    return redirect('login')

class logins(LoginView):
  template_name='base/logins.html'
  fields='__all__'
  redirect_authenticated_user=True 
  def get_success_url(self):
    return reverse_lazy('tasklist')
  

# Create your views here.
class tasklist(LoginRequiredMixin,ListView):
  model=Task
  context_object_name='tasks'
  def get_context_data(self,**kwargs):
    context=super().get_context_data(**kwargs)
    context['tasks']=context['tasks'].filter(user=self.request.user)
    return context



class taskdetail(LoginRequiredMixin,DetailView):
  model=Task
  context_object_name='task'
  template_name='base/task.html'

class taskcreate(LoginRequiredMixin,CreateView):
  model=Task
  fields=['title','description','complete']
  success_url=reverse_lazy('tasklist')
  def form_valid(self,form):
    form.instance.user=self.request.user
    return super(taskcreate,self).form_valid(form)

class taskupdate(UpdateView):
  model=Task
  fields=['title','description','complete']
  success_url=reverse_lazy('tasklist')

class taskdelete(DeleteView):
  model=Task
  context_object_name='task'
  template_name='base/taskdelete.html'
  success_url=reverse_lazy('tasklist')


class RegisterPage(FormView):
  template_name='base/register.html'
  form_class=UserCreationForm
  success_url=reverse_lazy('tasklist')
  redirect_authenticated_user=True
  def form_valid(self,form):
    user=form.save()
    # save optional email from the template (UserCreationForm doesn't include email by default)
    email = self.request.POST.get('email')
    if email:
      user.email = email
      user.save()
    if user is not None:
      auth_login(self.request,user)
    return super(RegisterPage,self).form_valid(form)
  def get(self,*args,**kwargs):
    if self.request.user.is_authenticated:
      return redirect('tasklist')
    return super(RegisterPage,self).get(*args,**kwargs)

