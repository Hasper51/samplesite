from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
# Create your views here.
from django.http import HttpResponse
from .models import Bb
from .models import Rubric
from django.views.generic.edit import CreateView
from .forms import BbForm
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth import logout, authenticate, login
class BbCreateView(PermissionRequiredMixin, CreateView):
  permission_required = ('bboard.add_bb', 'bboard.change_bb', 'bboard.delete_bb')
  template_name = 'bboard/create.html'
  form_class = BbForm
  success_url = reverse_lazy('index')
  def get_context_data(self, **kwargs):
    context = super().get_context_data(**kwargs)
    context['rubrics'] = Rubric.objects.all()
    return context
@login_required
@permission_required(('bboard.add_rubric','bboard.change_rubric','bboard.delete_rubric'))
def index(request):
    bbs = Bb.objects.all()
    rubrics = Rubric.objects.all()
    context = {'bbs': bbs, 'rubrics':rubrics}
    return render(request, 'bboard/index.html', context)

  
def logout_view(request):
    logout(request)
    return render(request, 'bboard/index.html')

def by_rubric(request, rubric_id):
  bbs = Bb.objects.filter(rubric=rubric_id)
  rubrics = Rubric.objects.all()
  current_rubric = Rubric.objects.get(pk=rubric_id)
  context = {'bbs': bbs , 'rubrics': rubrics, 'current_rubric': current_rubric}
  return render(request, 'bboard/by_rubric.html', context)
  



