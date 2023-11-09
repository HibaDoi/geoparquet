from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings
from django.core.files.storage import FileSystemStorage
import geopandas as gpd
import pandas as pd
from django.views.decorators.csrf import csrf_exempt
import tempfile
from zipfile import ZipFile
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
            gdf = gpd.read_file("/parquet"+uploaded_file_url)
            #gdf = gpd.read_file(uploaded_file_url)
            #gdf = gpd.read_file(str(request.GET["p"]))
            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
def upp(request):
       
            gdf = gpd.read_file("E:/Desktop/doc/"+str(request.GET["pp"]))

            
            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
def uppp(request):
       
            gdf = gpd.read_file("E:/Desktop/doc/"+str(request.GET["ppp"]))

            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hereyouare.geoparquet"'},
            )
            gdf.to_parquet(response)
            return response
def to(request):
       
            df = pd.read_csv("E:/Desktop/doc/"+str(request.GET["pppp"]))
            gdf = gpd.GeoDataFrame(df, geometry=gpd.GeoSeries.from_wkt(df['geometry']))

            response = HttpResponse(
                content_type="text/geoparquet",
                headers={"Content-Disposition": 'attachment; filename="hhh.geoparquet"'},
            )
            gdf.to_parquet(response)

            return response
def too(request):
       
            gdf = gpd.read_parquet("E:/Desktop/doc/"+str(request.GET["geop_to_shp"]))
            basename = 'basename'

            # Convert to shapefile and serve it to the user
            with tempfile.TemporaryDirectory() as tmp_dir:

                # Export gdf as shapefile
                gdf.to_file(os.path.join(tmp_dir, f'{basename}.shp'), driver='ESRI Shapefile')

                # Zip the exported files to a single file
                tmp_zip_file_name = f'{basename}.zip'
                tmp_zip_file_path = f"{tmp_dir}/{tmp_zip_file_name}"
                tmp_zip_obj = ZipFile(tmp_zip_file_path, 'w')

                for file in os.listdir(tmp_dir):
                    if file != tmp_zip_file_name:
                        tmp_zip_obj.write(os.path.join(tmp_dir, file), file)

                tmp_zip_obj.close()

                # Return the file
                with open(tmp_zip_file_path, 'rb') as file:
                    response = HttpResponse(file, content_type='application/force-download')
                    response['Content-Disposition'] = f'attachment; filename="{tmp_zip_file_name}"'
                    return response

        

            #return response

def tooo(request):
       
            gdf = gpd.read_parquet("E:/Desktop/doc/"+str(request.GET["uuu"]))
            response = HttpResponse(
                content_type="text/geojson",
                headers={"Content-Disposition": 'attachment; filename="hhh.geojson"'},
            )
            gdf.to_file(response,driver='GeoJSON')

        

            return response
def toooo(request):
       
            gdf = gpd.read_parquet("E:/Desktop/doc/"+str(request.GET["uuui"]))
            #df = gdf.drop(columns=['geometry'])
            response = HttpResponse(
                content_type="text/csv",
                headers={"Content-Disposition": 'attachment; filename="hhh.csv"'},
            )
            gdf.to_csv(response,index=False)

    

            return response