from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from . import views
#
urlpatterns = [
    path('', views.list_product_controller, name='list_products'),
    path('detalhes/<int:id>/', views.product_details_controller, name='product_details'),
    path('categoria/<int:id>/', views.products_categories_controller, name='product_category'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
