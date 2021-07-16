from django.contrib import admin
from django.urls import path, include
from gudarfest import views as local_views
from users import views as users_views
from crud import views as crud_views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('login/',auth_views.LoginView.as_view(template_name='users/login.html'),name='login'),
    path('login/',auth_views.LogoutView.as_view(template_name='users/logout.html'),name='logout'),    
    path('', crud_views.CrudListView.as_view(), name='crud'),


    path('person-detail/<int:pk>/',users_views.PersonUpdateView.as_view(), name='person_detail' ),
    path('person-delete/<int:pk>/',users_views.PersonDeleteView.as_view(), name='person_delete' ),
    path('person-create/',users_views.PersonCreateView.as_view(), name='person_create' ),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 
