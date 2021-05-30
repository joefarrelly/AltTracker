from django.urls import path

from . import views

urlpatterns = [
    # path('test/',views.index,name='index'),
    path('', views.wowProfHome, name='wowprof_home'),
    path('redirect/', views.wowProfRedirect),
    # path('redirect/<str:codeState/', views.wowProfRedirect),
    # path('', views.calcHome,name='calc_home'),
    path('alts/', views.wowProfAlts, name='wowprof_alts'),
    path('alts/<str:name>/<str:realm>/profession/<str:profession>', views.wowProfAltsProfession, name='wowprof_alts_profession'),
    path('alts/<str:name>/<str:realm>/details', views.wowProfAltsMoreDetails, name='wowprof_alts_more'),
    path('requiem/', views.wowProfRequiem, name='wowprof_requiem'),
    path('checker/', views.wowProfChecker, name='wowprof_checker'),
    path('test_ajax/', views.ajax_view),
    path('test_ajax_1/', views.ajax_view_1),
]
