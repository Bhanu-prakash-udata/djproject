from django.urls import path
from bikebook import views
from django.contrib.auth import views as v
urlpatterns = [
   path('',views.home,name="hm"),
   path('abt/',views.abt,name="ab"),
   path('reg/',views.regis,name="rg"),
   path('lg/',v.LoginView.as_view(template_name="btm/login.html"),name="log"),
   path('lgo/',v.LogoutView.as_view(template_name="btm/logout.html"),name="lgg"),
   path('bb/',views.bookbike,name='bb'),
   path('hn/',views.honda,name='hn'),
   path('ry/',views.royal,name='ry'),
   path('bm/',views.bmw,name='bm'),
   path('ad/',views.address,name='ad'),
   path('ab/',views.addbike,name='addbike'),
   path('allbikes/',views.allbike,name='allbikes'),
   path('viewmore/<int:id>/',views.viewmore,name='viewmore'),
   path('profile/',views.profile,name='profile'),
   path('allbrands/',views.allbrands,name='allbrands'),
   path('viewbikes/',views.viewbikes,name='viewbikes'),
]