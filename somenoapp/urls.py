from django.urls import path
    from .views import delivery_receipt_list

    urlpatterns = [
        path('delivery-receipts/', delivery_receipt_list, name='delivery_receipt_list'),
        # 他のビューのURLパターンを追加
    ]
