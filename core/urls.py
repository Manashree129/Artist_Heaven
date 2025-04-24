from django.urls import path
from . import views

# ------to include media file ------
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.index,name='home'),
    path('about/',views.about),
    path('contact/',views.contact),
    path('paints/',views.paints,name='paints'),
    path('surfaces/',views.surfaces,name='surfaces'),
    path('drawing/',views.drawing,name='drawing'),
    path('tool_details/,<int:id>',views.tool_details,name='tooldetails'),
    path('registration/',views.registration,name='registration'),
    path('login/',views.log_in,name='login'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.log_out, name="logout"),
    path('changepassword/',views.changepassword, name="changepassword"),
    path('add_to_cart/<int:id>',views.add_to_cart,name="addtocart"),
    path('view_cart/',views.view_cart,name="viewcart"),
    path('add_quantity/<int:id>',views.add_quantity,name="add_quantity"),
    path('delete_quantity/<int:id>',views.delete_quantity,name="delete_quantity"),
    path('delete_cart/<int:id>',views.delete_cart, name='deletecart'),
    path('address/',views.address,name='address'),
    path('delete_address/<int:id>',views.delete_address,name='deleteaddress'),
    path('checkout/',views.checkout,name='checkout'),
    path('payment_success/<int:selected_address_id>/',views.payment_success,name='paymentsuccess'),
    path('payment_failed/',views.payment_failed,name='paymentfailed'),
    path('payment/',views.payment,name='payment'),
    path('order/',views.order,name='order'),
    path('buynow/<int:id>',views.buynow,name='buynow'),
    path('buynow_payment/<int:id>',views.buynow_payment,name='buynowpayment'),
    path('buynow_payment_success/<int:selected_address_id>/<int:id>',views.buynow_payment_success,name='buynowpaymentsuccess'),
    path('forgotpassword/',views.forgot_password, name="forgotpassword"),
    path('reset_password/<uidb64>/<token>/', views.reset_password, name='resetpassword'),
    path('password_reset_done/', views.password_reset_done, name='passwordresetdone'),
    path('search/', views.search, name='search')
]

if settings.DEBUG:
    urlpatterns +=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

