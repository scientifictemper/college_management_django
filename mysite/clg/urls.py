from os import name
from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),
    path('signup/',views.registerPage,name='signup'),
    path('login/', views.loginPage, name="login"),  
	path('logout/', views.logoutUser, name="logout"),
    path('permission/',views.permission,name='permission'),
    path('material/',views.material,name='material'),
    path('payment/',views.payment,name='payment'),
    path('profile/',views.profile,name='profile'),
    path('viewper/',views.PermissionListView.as_view(),name='viewper'),
    path('giveper/<int:id>',views.givePermission,name='giveper'),
    path('viewpay/',views.viewpayment,name='viewpay'),
    path('letter/<int:id>',views.letter,name='letter'),
    path('time/',views.timetable,name='timetable'),
    path('balance/<int:id>',views.feebalance,name='balance'),
    path('cse/',views.cse,name='cse'),
    path('cse_pdf/',views.cse_pdf,name='cse_pdf'),
    path('it/',views.it,name='it'),
    path('eee/',views.eee,name='eee'),
    path('ece/',views.ece,name='ece'),
    path('mech/',views.mech,name='mech'),
    
]