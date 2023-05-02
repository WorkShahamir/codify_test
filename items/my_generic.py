from django.db.migrations import serializer
from rest_framework import views
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404


class MyGenericListCreateView(views.APIView):
    queryset = None
    serializer_class = None

    def get(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.queryset.all(), many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        if request.method == 'POST':
            serializer = self.serializer_class(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=201)


class MyGenericRetrieveUpdateDestroyView(views.APIView):
    queryset = None
    serializer_class = None

    def get_object(self, pk):
        item = get_object_or_404(self.queryset.all(), pk=pk)
        return item

    def get(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(pk))
        return Response(serializer.data)

    def put(self, request, pk, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(pk), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)

    def delete(self, pk, request, *args, **kwargs):
        self.get_object(pk).delete()
        return Response(status=204)
