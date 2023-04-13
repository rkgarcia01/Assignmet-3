from django.urls import path
from . import views
#from .views import bmi_measurement
#from .views import HomePageView
#from .views import bmi_measurement



#urlpatterns = [path("", HomePageView.as_view() , name="home")]
#working vvv
urlpatterns = [path("", views.homePageView , name="home")]