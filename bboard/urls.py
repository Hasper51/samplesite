from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView, PasswordChangeView, PasswordChangeDoneView, PasswordResetView, PasswordResetDoneView, PasswordResetConfirmView, PasswordResetCompleteView
from .views import BbCreateView
from .views import index, by_rubric
urlpatterns = [
  path('add/', BbCreateView.as_view(), name='add'),
  path('accounts/login/', 
      LoginView.as_view(), 
      name='login'),
  path('accounts/logout/', 
      LogoutView.as_view(
      next_page='bboard:index'), 
      name='logout'),
  path('accounts/password_change/', 
      PasswordChangeView.as_view(
      template_name='registration/change_password.html'), 
      name='password_change'),
  path('accounts/password_change/done/', 
      PasswordChangeDoneView.as_view(
      template_name='registration/password_changed.html'), 
      name='password_change_done'),
  path('accounts/password_reset/', 
      PasswordResetView.as_view(
      from_email='vahitov.ainur@bk.ru',
      template_name='registration/reset_password.html',
      subject_template_name='registration/reset_subject.txt',
      email_template_name='registration/reset_email.html'),
      name='password_reset'),
  path('accounts/password_reset/done/', 
      PasswordResetDoneView.as_view(
      template_name='registration/email_sent.html'),
      name='password_reset_done'), 
  path('accounts/reset/<uidb64>/<token>/',
      PasswordResetConfirmView.as_view(
      template_name='registration/confirm_password.html'),  
      name='password_reset_confirm'),
  path('accounts/reset/done/',
      PasswordResetCompleteView.as_view(
      template_name='registration/password_confirmed.html'),  
      name='password_reset_complete'),           
  path('<int:rubric_id>/', by_rubric, name='by_rubric'),
  path('', index, name='index' ),
  

]  
LOGOUT_REDIRECT_URL = 'bboard:index'
LOGIN_REDIRECT_URL = 'bboard:index'