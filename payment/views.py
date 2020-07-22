# from django.conf import settings
# from django.urls import reverse
# from django.shortcuts import render, get_object_or_404
# from paypal.standard.forms import PayPalPaymentsForm
# from orders.models import Orders
# from django.views.decorators.csrf import csrf_exempt
#
#
# @csrf_exempt
# def payment_done(request):
#     return render(request, 'payment/done.html')
#
# @csrf_exempt
# def payment_cancelled(request):
#     return render(request,'payment/cancelled.html')
#
#
# def payment_process(request, ord_id):
#     host = request.get_host()
#     # order = get_object_or_404(Map, id=ord_id)
#     paypal_dict = {
#         'business': settings.PAYPAL_RECEIVER_EMAIL,
#         'amount': '1',
#         # 'item_name': 'Order {}'.format(ord_id),
#         'item_name': 'O',
#         'invoice': '1',
#         'currency_code': 'USD',
#         'notify_url': 'http://{}{}'.format(host, reverse('paypal-ipn')),
#         'return_url': 'http://{}{}'.format(host, reverse('payment_done')),
#         'cancel_return': 'http://{}{}'.format(host, reverse('payment_canceled')),
#     }
#     form = PayPalPaymentsForm(initial=paypal_dict)
#     return render(request, 'payment/process.html', {'form': form})
