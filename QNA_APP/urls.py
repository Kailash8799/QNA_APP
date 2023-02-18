
from django.contrib import admin
from django.urls import path,include
from QNA_APP import views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('authcreadentials/', include('auth_credentials.urls')),
    path('question_ans/', include('question_ans.urls')),
] + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
