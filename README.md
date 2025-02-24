# GeoFormat Converter: Web-Based Geospatial Data Transformation

## Problem Solved  
- Developed a **web application** to **convert between multiple geospatial file formats efficiently**.  
- Supports **Shapefile (SHP), GeoJSON, CSV, and GeoParquet**, allowing **easy transformation** between formats.  
- Automates **geospatial data handling**, enabling **GIS professionals** to work with different data standards seamlessly.  

## Tech Stack  
- **Backend:** Django (Python), GeoPandas, GDAL, Fiona, Pandas  
- **Frontend:** HTML, CSS, JavaScript (Bootstrap)  

### **File Handling & Conversion**  
- **Uploads & Reads:** SHP, GeoJSON, CSV, GeoParquet  
- **Writes & Converts:**  
  - **SHP → GeoParquet**  
  - **GeoParquet → SHP**  
  - **GeoParquet → GeoJSON**  
  - **GeoParquet → CSV**  
- **Storage & Processing:** FileSystemStorage, ZipFile (for SHP exports)  

## Key Contributions  
- **Built the Django-based backend** for handling **geospatial file uploads and format conversion**.  
- **Implemented GeoPandas-based format conversion functions** to ensure **accurate transformations**.  
- **Created downloadable outputs**, including **compressed shapefile exports** for ease of distribution.  
- **Developed GeoJSON and CSV conversion features**, allowing easier **web and database integration**.  

## Key Features  
✅ **Automatic conversion** between SHP, GeoJSON, CSV, and GeoParquet  
✅ **Downloadable files** after transformation  
✅ **Support for large geospatial datasets** with optimized processing  
✅ **Integration-ready** for GIS professionals working with different formats  

## Key Results  
✅ **Increased processing speed**, allowing **instant format transformations**.  
✅ **Enabled seamless data interoperability** between **GIS software, databases, and web applications**.  
✅ **Successfully converted large datasets** to **lightweight GeoParquet format**, reducing file size and improving performance.  
