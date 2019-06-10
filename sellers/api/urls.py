from django.urls import path
from .views import SellerRudView, SellerAPIViewAll, SellerTypeRudView, SellerTypeAPIViewAll, SellerImageAPIViewAll, \
    SellerImageRudView, SellerManageAddressInfoRudView, SellerUpdateProfileRudView, SellerUpdateCoverRudView, \
    SellerUpadteContactInfoRudView

urlpatterns = [
    # seller
    path('sellers/list/', SellerAPIViewAll.as_view(), name='seller_list'),
    path('sellers/<int:pk>/', SellerRudView.as_view(), name='seller_rud'),

    # seller type
    path('seller_types/list/', SellerTypeAPIViewAll.as_view(), name='seller_types_list'),
    path('seller_types/<int:pk>/', SellerTypeRudView.as_view(), name='seller_types_rud'),

    # seller type
    path('seller_images/list/', SellerImageAPIViewAll.as_view(), name='seller_images_list'),
    path('seller_images/<int:pk>/', SellerImageRudView.as_view(), name='seller_images_rud'),

    # seller manage address info
    path('sellers/manage_address/<int:pk>/', SellerManageAddressInfoRudView.as_view(),
         name='seller_manage_address_list'),

    # seller update profile Picture
    path('sellers/profile_pic/<int:pk>/', SellerUpdateProfileRudView.as_view(), name='seller_update_profile_rud'),

    # seller update cover Picture
    path('sellers/cover_pic/<int:pk>/', SellerUpdateCoverRudView.as_view(), name='seller_update_cover_rud'),

    # seller update contact info
    path('sellers/contact_info/<int:pk>/', SellerUpadteContactInfoRudView.as_view(), name='seller_update_contact_info_rud')
]
