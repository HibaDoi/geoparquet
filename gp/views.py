from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import geopandas as gpd
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import tempfile
import zipfile
import os
import io
# Create your views here.
def acceuil(request):
    return render(request,'acceuil1.html')
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
def uppp(request):
       
            gdf = gpd.read_file(str(request.GET["ppp"]))

            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
def to(request):
       
            df = pd.read_csv(str(request.GET["pppp"]))
            gdf = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_wkt(df['geometry']))

            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hhh.geoparquet"'},
            )
            gdf.to_parquet(response)

            return response
def too(request):
       
            gdf = gpd.read_parquet(str(request.GET["geop_to_shp"]))
            response = HttpResponse(
                content_type="application/zip",
                headers={"Content-Disposition": 'attachment; filename="E://Desktop//AA//hhh.shp"'},
            )
            gdf.to_file(response,driver='ESRI Shapefile')

        

            return response

def tooo(request):
       
            gdf = gpd.read_parquet(str(request.GET["uuu"]))
            response = HttpResponse(
                content_type="text/geojson",
                headers={"Content-Disposition": 'attachment; filename="hhh.geojson"'},
            )
            gdf.to_file(response,driver='GeoJSON')

        

            return response
def toooo(request):
       
            gdf = gpd.read_parquet(str(request.GET["uuui"]))
            #df = gdf.drop(columns=['geometry'])
            response = HttpResponse(
                content_type="text/csv",
                headers={"Content-Disposition": 'attachment; filename="hhh.csv"'},
            )
            gdf.to_csv(response,index=False)

    

            return response


