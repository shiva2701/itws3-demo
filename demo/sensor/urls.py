from django.conf.urls import url, include
from .views import add_temp_reading, get_temp_readings
urlpatterns = [
    url(r'addtempreading/$', add_temp_reading ),
    url(r'gettempreadings/$', get_temp_readings),
]