from django.http import HttpResponse
from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework import views
from rest_framework import viewsets

from .models import Category, Item
from .serializers import CategorySerializers, ItemSerializers
from rest_framework.decorators import api_view
from .my_generic import MyGenericListCreateView, MyGenericRetrieveUpdateDestroyView


class CategoryListCreateApiView(generics.ListCreateAPIView):
    """
    category create and licr view
    """
    queryset = Category.objects.all()
    serializer_class = CategorySerializers


class ItemListCreateApiView(generics.ListCreateAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializers


@api_view(http_method_names=['GET', 'POST'])
def item_list_create_api_view(request):
    # print(request.query_params)
    # print(request.data)
    # data = [
    #     {
    #         'name': 'codify',
    #         'address': '7 mkr',
    #     }
    # ]
    if request.method == 'GET':
        queryset = Item.objects.all()
        serializer = ItemSerializers(queryset, many=True)
        return Response(serializer.data)
    if request.method == 'POST':
        serializer = ItemSerializers(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)
        else:
            return Response(serializer.errors, status=400)


@api_view(http_method_names=['GET', 'PUT', 'DELETE'])
def item_retrieve_update_destroy_api_view(request, pk):
    item = get_object_or_404(Item, pk=pk)
    # try:
    #     item = Item.objects.get(pk=pk)
    # except Item.DoesNotExist:
    #     return Response({'detail': 'not found'}, status=404)

    if request.method == 'GET':
        serializer = ItemSerializers(instance=item)
        return Response(serializer.data)
    if request.method == 'PUT':
        serializer = ItemSerializers(instance=item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=400)
    if request.method == 'DELETE':
        item.delete()
        return Response(status=204)


class ItemListCreateView(MyGenericListCreateView):
    queryset = Item.objects.all()
    serializer = ItemSerializers


class ItemRetrieveUpdateDestroyView(MyGenericRetrieveUpdateDestroyView):
    queryset = Item.objects.all()
    serializer = ItemSerializers


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializers
