from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('',views.index,name='index'),
    path('index/',views.index,name='index'),
    path('route/',views.route,name='route'),
    path('register/',views.register,name='register'),
    path('login/',views.logins,name='login'),
    path('logout/',views.logouts,name='logout'),
    path('contact/',views.contact,name='contact'),
    path('book_ticket/<int:t_id>/<slug:t>/<int:s>',views.book_ticket,name='book_ticket'),
    path('pass_Details/',views.pass_detail,name='pass_Details'),
    path('complete/',views.complete,name='complete'),
    path('transaction/',views.transaction,name='transaction'),
    path('delete/',views.deletesession,name='delete'),
    path('pnr/',views.pnr,name='pnr'),
    path('complete/',views.complete,name='complete'),
    path('pdf/', views.ViewPDF.as_view(),name='pdf'), 
    path('downloadpdf/', views.DownloadPDF.as_view(),name='downloadpdf'), 
    path('change/',views.change,name='change'),
    path('reset_password/',auth_views.PasswordResetView.as_view(template_name="reset_password.html"),name='reset_password'),
    path('reset_sent/',auth_views.PasswordResetDoneView.as_view(template_name="reset_sent.html"),name='password_reset_done'),
    path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(template_name="reset_confirm.html"),name='password_reset_confirm'),
    path('reset_complete/',auth_views.PasswordResetCompleteView.as_view(template_name="reset_complete.html"),name='password_reset_complete'),
    path('saved/',views.saved,name='saved'),
    path('about',views.about,name='about')
    ]