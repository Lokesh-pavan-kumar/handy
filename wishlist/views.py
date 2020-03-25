from django.shortcuts import render, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from handy.models import Product
from .models import WishList
from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

@login_required(login_url='login')
def add_to_wishlist(request, pk):
	product = Product.objects.get(id=pk)

	checker = WishList.objects.filter(user=request.user, product=product)

	if len(checker) == 0:
		item = WishList(product=product, user=request.user)
		item.save()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

class WishListView(LoginRequiredMixin, ListView):
	context_object_name = 'items'
	ordering = ['-date_added']

	def get_queryset(self):
		return WishList.objects.filter(user=self.request.user)

@login_required(login_url='login')
def del_from_wishlist(request, pk):
	removable_wish = WishList.objects.get(id=pk)
	removable_wish.delete()

	return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

