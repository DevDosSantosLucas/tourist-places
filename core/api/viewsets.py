from argparse import Action
from rest_framework.response import Response
from rest_framework import viewsets
from core.models import tourist_places  
from .serializers import TouristPlacesSerializer

class TouristPlaceViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    #queryset = tourist_places.objects.all()
    serializer_class = TouristPlacesSerializer
    #http_method_names = ['DELETE',]
    
    def get_queryset(self):#query String
    #http://127.0.0.1:8000/touristplaces/?id=3&name=createee&description=teste%20outr
        id = self.request.query_params.get('id',None)
        name = self.request.query_params.get('name',None)
        description = self.request.query_params.get('description',None)
        queryset = tourist_places.objects.all()
        if id:
            queryset = tourist_places.objects.filter(pk=id)

        if name:
            #queryset = queryset.filter(name=name)
            queryset = queryset.filter(name__iexact=name) #__iexact => case sensitive

        
        if description:
            queryset = queryset.filter(description__iexact=description)

        return queryset

    def list(self, request, *args, **kwargs):
        return super().list(request, *args, **kwargs)
    
    def create(self, request, *args, **kwargs):
        return super().create(request, *args, **kwargs)
    
    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
        

    def retrieve(self, request, *args, **kwargs):
        return super().retrieve(request, *args, **kwargs)
         

    def update(self, request, *args, **kwargs):
        return super(TouristPlacesSerializer,self).update(request, *args, **kwargs)
    
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)
    
    #@Action(method =['get'],detail=True)
    #def denounce(self, request, pk=None):
    #    pass

    #@Action(method=['get'],detail=False)
    #def teste(self,request):
    #    pass  