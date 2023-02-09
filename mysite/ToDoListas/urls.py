
from django.urls import path
from . import views
from .views import UzduotysList, UzduotisDetail, VartotojoUzduotysDetail, VartotojoUzduotisList, UzduotisVartotojoCreate, UzduotisVartotojoUpdate, UzduotisVartotojoDelete


urlpatterns = [
    path("", views.index, name="index"),
    path('register/', views.register, name='register'),
    path("uzduotys/", UzduotysList.as_view(), name="uzduotys"),
    path('uzduotys/<int:pk>/', UzduotisDetail.as_view(), name='uzduotis'),
    path("vartotojouzduotys/", VartotojoUzduotisList.as_view(), name="vartotojo_uzduotys"),
    path('vartotojouzduotys/<int:pk>', VartotojoUzduotysDetail.as_view(), name='vartotojo-uzduotys'),
    #path('uzduotis/<int:pk>/', UzduotisDetail.as_view(), name='uzduotis'),
    path('uzduotis-sukurti/', UzduotisVartotojoCreate.as_view(), name='uzduotis-sukurti'),
    path('uzduotis-redaguoti/<int:pk>/', UzduotisVartotojoUpdate.as_view(), name='uzduotis-redaguoti'),
    path('uzduotis-trinti/<int:pk>/', UzduotisVartotojoDelete.as_view(), name='uzduotis-trinti'),

    # path("uzduotys/", views.UzduotisList.as_view(), name="uzduotys"),
    # #path('uzduotys/<int:pk>', views.UzduotisListView.as_view(), name='uzduotis-detail'),
    # path('uzduotys/sukurti', views.UzduotisCreate.as_view(), name='sukurti-nauja'),
    # path('uzduotys/<int:pk>/redaguoti', views.UzduotisUpdate.as_view(), name='taisyti-uzduoti'),
    # path('uzduotys/<int:pk>/trinti', views.UzduotisDelete.as_view(), name='trinti-uzduoti'),
]