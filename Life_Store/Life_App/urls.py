from django.urls import path
from . import views

urlpatterns= [
	path('index/',views.index,name="index"),
	path('lifestyle/',views.lifestyle,name="lifestyle"),
	path('login/',views.login,name="login"),
	path('signup/',views.signup,name="signup"),
	path('cameras/',views.cameras,name="cameras"),
	path('cart/',views.cart,name="cart"),
	path('change/',views.change,name="change"),
	path('children/',views.children,name="children"),
	path('cre_deb/',views.cre_deb,name="cre_deb"),
	path('discount/',views.discount,name="discount"),
	path('netbank/',views.netbank,name="netbank"),
	path('others/',views.others,name="others"),
	path('contin/',views.contin,name="contin"),
	path('afterlog/',views.afterlog,name="afterlog"),
	path('concart/',views.concart,name="concart"),
	path('payment/',views.payment,name="payment"),
	path('phone/',views.phone,name="phone"),
	path('shirt/',views.shirt,name="shirt"),
	path('success/',views.success,name="success"),
	path('watches/',views.watches,name="watches"),

]