__author__ = 'willy_000'
import arcpy
#feature_info = [[[0, 0], [1000, 0], [1000, 1000], [0, 1000]]]
#features = []
#for feature in feature_info:
#    features.append(
#        arcpy.Polygon(
#            arcpy.Array([arcpy.Point(*coords) for coords in feature])))
#arcpy.CopyFeatures_management(features, "C:/Users/willy_000/SpatPro/Exercise08/polygons.shp")

import arcpy
from arcpy import env
env.workspace = "C:/Users/willy_000/SpatPro/Exercise08"
fc = "Hawaii.shp"
for row in arcpy.da.SearchCursor(fc, ["OID@", "SHAPE@"]):
    print("Feature {0}: ".format(row[0]))
    partnum = 0
    partnuma = 0
    for part in row[1]:
        poly = arcpy.Polygon(part) # <--Create polygon object from part
        print("Part {0} area: {1}".format(partnum, poly.area))
        partnum += 1
        print("Part {0} perimeter: {1}".format(partnuma, poly.length))
        partnuma += 1

#Could not figure out challenge 3


