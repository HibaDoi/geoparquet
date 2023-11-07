from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import geopandas as gpd
from django.views.decorators.csrf import csrf_exempt
# Create your views here.
def acceuil(request):
    return render(request,'acceuil.html')
@csrf_exempt
def up(request):
        if request.method == 'POST' and request.FILES['p']:
            myfile = request.FILES['p']
            fs = FileSystemStorage()
            filename = fs.save(myfile.name, myfile)
            uploaded_file_url = fs.url(filename)
            print(uploaded_file_url)
            gdf = gpd.read_file(uploaded_file_url)
            #gdf = gpd.read_file(str(request.GET["p"]))
            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
def upp(request):
       
            gdf = gpd.read_file(str(request.GET["pp"]))

            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
            