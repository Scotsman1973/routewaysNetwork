# routewaysNetwork
This QGIS plugin (under preparation) will carry out network  analysis from data entered.  The data will be random, derived from a least-cost-path algorithm, or from archaeogaming.
There have to be three categories of input for the routeway network analysis: routes (a shapefile), addresses (a shapefile) and places to visit (eg monuments or gyms).
One method for creating a realistic routeway is a least-cost-path algorithm, using a DEM converted into slope as the cost.
To clip (for example) an entire contry's slopeDEM, makr a mask layer as a shapefile, then open the GDAL processing toolbox=>clip raster by mask layer.
Save the result (shaped the same as the mask) as a geotiff.
go to the vector creation processing tool box.  Choose the 'Random points in polygons' tool, another tool or make the points manually.
Then install the least-cost-path plugin, which is a processing tool.  It is important that you choose the point layer for each input layer, and that you iterate through each input layer.  Iteration caan be achieved by pressing on the light green arrow beside the input box, and iterating means that all points are joined with seperate lines.
Then, merge all the routeways together if you want, and it will probably be necessary to use the 'fix geometries' tool.
Create random placed settlements along the routeways using the 'random points along line' tool.
