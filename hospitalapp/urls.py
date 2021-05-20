from django.urls import path,include
from .views import login_user
from django.contrib.auth import views as auth_views
from django.views.generic.base import TemplateView
from rest_framework import routers
from hospitalapp import views

"""For auto config the urls Router will be use
and in router views need to register"""

router = routers.DefaultRouter()
router.register('patient',views.PatientViewSet)
router.register('doctor',views.DoctorViewSet)
router.register('appointment',views.AppointmentViewSet)


"""all the urls mapping done in urlpatters"""

urlpatterns = [
    path('accounts/',include('django.contrib.auth.urls')),
    path('',TemplateView.as_view(template_name = 'home.html'),name = 'home'),
    path('',include(router.urls)),

]