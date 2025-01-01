addresses = QgsVectorLayer("E:/brunswick_network_data/brunswick_addresses.shp", "bruns_addresses", "ogr")
roads = QgsVectorLayer("E:/brunswick_network_data/brunswick_roads.shp", "bruns_roads", "ogr")
northwalls = QgsVectorLayer("E:/brunswick_network_data/northwalls_climbing.shp", "northwalls_climbing", "ogr")
boulders = QgsVectorLayer("E:/brunswick_network_data/northside_boulders.shp", "northside_boulders", "ogr")
guests = QgsVectorLayer("E:/brunswick_network_data/guests_martial_arts.shp", "guests_martial", "ogr")
guardian = QgsVectorLayer("E:/brunswick_network_data/guardian_martial_arts.shp", "guardian_martial", "ogr")
baths = QgsVectorLayer("E:/brunswick_network_data/brunswick_baths.shp", "bruns_baths", "ogr")
garden = QgsVectorLayer("E:/brunswick_network_data/community_garden.shp", "community_garden", "ogr")

# these are the weightings for the different recreational facilities
northwalls_weight = 6.00
boulders_weight = 5.00
guests_weight = 0.00
guardian_weight = 1.00
baths_weight = 8.00
garden_weight = 10.00

weight_sum = sum([northwalls_weight, boulders_weight, guests_weight, guardian_weight, baths_weight, baths_weight, garden_weight])
weight_max = max([northwalls_weight, boulders_weight, guests_weight, guardian_weight, baths_weight, baths_weight, garden_weight])
weight_min = min([northwalls_weight, boulders_weight, guests_weight, guardian_weight, baths_weight, baths_weight, garden_weight])

northwalls_normalize_weight = (northwalls_weight-weight_min)/(weight_max-weight_min)
boulders_normalize_weight = (boulders_weight-weight_min)/(weight_max-weight_min)
guests_normalize_weight = (guests_weight-weight_min)/(weight_max-weight_min)
guardian_normalize_weight = (guardian_weight-weight_min)/(weight_max-weight_min)
baths_normalize_weight = (baths_weight-weight_min)/(weight_max-weight_min)
garden_normalize_weight = (garden_weight-weight_min)/(weight_max-weight_min)

northwalls_standard_weight = northwalls_weight/weight_sum
boulders_standard_weight = boulders_weight/weight_sum
guests_standard_weight = guests_weight/weight_sum
guardian_standard_weight = guardian_weight/weight_sum
baths_standard_weight = baths_weight/weight_sum
garden_standard_weight = garden_weight/weight_sum

print('The sum of weights is: {}.'.format(weight_sum))
print('The max of weights is: {}.'.format(weight_max))
print('The min of weights is: {}.'.format(weight_min))

print('The max - min normalized weight of Northwalls climbing gym is: {}.'.format(northwalls_normalize_weight))
print('The max - min normalized weight of Northside bouldering gym is: {}.'.format(boulders_normalize_weight))
print('The max - min normalized weight of Guests Martial Arts is: {}.'.format(guests_normalize_weight))
print('The max - min normalized weight of Guardian Martial Arts is: {}.'.format(guardian_normalize_weight))
print('The max - min normalized weight of Brunswick Baths is: {}.'.format(baths_normalize_weight))
print('The max - min normalized weight of Luscombe Street Community Garden is: {}.'.format(garden_normalize_weight))

print('The standardized weight of Northwalls climbing gym is: {}.'.format(northwalls_standard_weight))
print('The standardized weight of Northside bouldering gym is: {}.'.format(boulders_standard_weight))
print('The standardized weight of Guests Martial Arrts is: {}.'.format(guests_standard_weight))
print('The standardized weight of Guardian Martial Arts is: {}.'.format(guardian_standard_weight))
print('The standardized weight of Brunswick Baths is: {}.'.format(baths_standard_weight))
print('The standardized weight of Luscombe Street Community Garden is: {}.'.format(garden_standard_weight))

def funct_weighting_calculator(feature, weight):
    
    return feature * weight
    
def funct_classify_calculator(feature):
    
    if (1.00 < feature <= 500.00):
        return 5
    elif ( 500.00 < feature <= 1000.00):
        return 4
    elif (1000.00 < feature <= 1500.00):
        return 3
    elif (1500.00 < feature <= 2000.00):
        return 2
    elif (feature > 2000.00):
        return 1
    else:
        return 0

# these next four lines purge the layers panel to stop it becoming clutered

legendLayers = [] # create an empty array
for layer in QgsProject.instance().layerTreeRoot().findLayers(): # iterate through the layer panel
    legendLayers.append(layer.layerId()) # append the ID of each layer into the array


QgsProject.instance().removeMapLayers( list( legendLayers ) ) # remove all of the layers in the array from the active map

# these groups of code check each vector layer individually and return an error message if any of them do not load properly

if not addresses.isValid():
    print("Address layer failed to load!")

QgsProject.instance().addMapLayer(addresses)

if not roads.isValid():
    print("Roads layer failed to load!")

QgsProject.instance().addMapLayer(roads)

if not northwalls.isValid():
    print("Northwalls layer failed to load!")

QgsProject.instance().addMapLayer(northwalls)

if not boulders.isValid():
    print("Northside boulders layer failed to load!")

QgsProject.instance().addMapLayer(boulders)

if not guests.isValid():
    print("Guests martial arts layer failed to load!")

QgsProject.instance().addMapLayer(guests)

if not guardian.isValid():
    print("Guardian martial arts layer failed to load!")

QgsProject.instance().addMapLayer(guardian)

if not baths.isValid():
    print("Brunswick baths layer failed to load!")

QgsProject.instance().addMapLayer(baths)

if not garden.isValid():
    print("Community garden layer failed to load!")

QgsProject.instance().addMapLayer(garden)


# this code block adds 13 new fields to the brunswick_addresses attribute table
# 6 for distance between each recreational facility and that address
# six for standardized weightings and one for the final suitability score for that address

addresses.dataProvider().addAttributes([QgsField("addressid", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("walls_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("boulder_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("guests_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("guardian_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("baths_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("garden_d", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("walls_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("boulder_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("guests_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("guardian_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("baths_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("garden_w", QVariant.Double)]) # creates a new field
addresses.dataProvider().addAttributes([QgsField("suitabil", QVariant.Double)]) # creates a new field
addresses.updateFields()

print('Address layer fields appended')

context = QgsExpressionContext()
context.appendScopes(\
#does need a backslash
QgsExpressionContextUtils.globalProjectLayerScopes(addresses))

with edit(addresses):
    for feature in addresses.getFeatures():
        
        addresses.updateFields()
        feature.setAttribute(feature.fieldNameIndex('addressid'), feature['OBJECTID']) # fieldnameindex is the  field to be written into
        # second parameter is the expression to be writen into that field
        
        addresses.updateFeature(feature)
        
#############################
#boulders
############################
        
network_brunswick_boulders = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': addresses,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': boulders,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Northside boulders network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_boulders)

address_net_result1 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result1.shp'
address_net1 = processing.run('qgis:joinattributestable', {
                        'INPUT': addresses,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_boulders,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

# transfer the distances from each address to the facility to the address attribute table
# this block of code accesses the field calculator from within the console script

with edit(address_net1):
    for feature in address_net1.getFeatures():
        
        address_net1.updateFields()
        # the first field name is the field being written to, the second field name is the field that the values are being gathered from, there can be only two parameters
        feature.setAttribute(feature.fieldNameIndex('boulder_d'), feature['network_cost'])
        
        address_net1.updateFeature(feature)
        
    print('Northside boulders network distances transfered to address attribute table')
    
QgsProject.instance().addMapLayer(address_net1)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net1.getFeatures()

caps = address_net1.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net1.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net1.updateFields()
        
QgsProject.instance().addMapLayer(address_net1)

#################################
#northwalls
##############################

network_brunswick_northwalls = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': address_net1,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': northwalls,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Northwalls climbing gym network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_northwalls)

address_net_result2 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result2.shp'
address_net2 = processing.run('qgis:joinattributestable', {
                        'INPUT': address_net1,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_boulders,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

with edit(address_net2):
    for feature in address_net2.getFeatures():
        
        address_net2.updateFields()
        feature.setAttribute(feature.fieldNameIndex('walls_d'), feature['network_cost'])
        
        address_net2.updateFeature(feature)
        
    print('Northwalls climbing gym network distances transfered')
    
QgsProject.instance().addMapLayer(address_net2)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net2.getFeatures()

caps = address_net2.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net2.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net2.updateFields()
        
QgsProject.instance().addMapLayer(address_net2)

###########################################
#guests
##########################################

network_brunswick_guests = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': address_net2,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': guests,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Guests Martial Arts network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_guests)

address_net_result3 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result3.shp'
address_net3 = processing.run('qgis:joinattributestable', {
                        'INPUT': address_net2,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_guests,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

with edit(address_net3):
    for feature in address_net3.getFeatures():
        
        address_net3.updateFields()
        feature.setAttribute(feature.fieldNameIndex('guests_d'), feature['network_cost'])
        
        address_net3.updateFeature(feature)
        
    print('Guests Martial Arts network distances transfered')
    
QgsProject.instance().addMapLayer(address_net3)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net3.getFeatures()

caps = address_net3.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net3.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net3.updateFields()
        
QgsProject.instance().addMapLayer(address_net3)

########################################
#guardian
#####################################

network_brunswick_guardian = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': address_net3,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': guardian,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Guardian Martial Arts network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_guardian)

address_net_result4 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result4.shp'
address_net4 = processing.run('qgis:joinattributestable', {
                        'INPUT': address_net3,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_guardian,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

with edit(address_net4):
    for feature in address_net4.getFeatures():
        
        address_net4.updateFields()
        feature.setAttribute(feature.fieldNameIndex('guardian_d'), feature['network_cost'])
        
        address_net4.updateFeature(feature)
        
    print('Guardian Martial Arts network distances transfered')
    
QgsProject.instance().addMapLayer(address_net4)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net4.getFeatures()

caps = address_net4.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net4.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net4.updateFields()
        
QgsProject.instance().addMapLayer(address_net4)

###########################################
#baths
##########################################

network_brunswick_baths = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': address_net4,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': baths,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Brunswick Baths network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_baths)

address_net_result5 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result5.shp'
address_net5 = processing.run('qgis:joinattributestable', {
                        'INPUT': address_net4,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_baths,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

with edit(address_net5):
    for feature in address_net5.getFeatures():
        
        address_net5.updateFields()
        feature.setAttribute(feature.fieldNameIndex('baths_d'), feature['network_cost'])
        
        address_net5.updateFeature(feature)
        
    print('Brunswick Baths network distances transfered')
    
QgsProject.instance().addMapLayer(address_net5)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net5.getFeatures()

caps = address_net5.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net5.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net5.updateFields()
        
QgsProject.instance().addMapLayer(address_net5)

########################################
#garden
#####################################

network_brunswick_garden = processing.run("qneat3:OdMatrixFromLayersAsTable", 
                        {'INPUT': roads,
                        'FROM_POINT_LAYER': address_net5,
                        'FROM_ID_FIELD': 'addressid',
                        'TO_POINT_LAYER': garden,
                        'TO_ID_FIELD': 'OBJECTID',
                        'STRATEGY': 0,
                        'OUTPUT': 'memory:'})['OUTPUT']
                        
print('Community Garden network analysis completed')
                        
QgsProject.instance().addMapLayer(network_brunswick_garden)

address_net_result6 = 'C:/Users/ADMIN/Desktop/Data/brunswick_network_data/address_net_result6.shp'
address_net6 = processing.run('qgis:joinattributestable', {
                        'INPUT': address_net5,
                        'FIELD': 'addressid',
                        'INPUT_2': network_brunswick_garden,
                        'FIELD_2': 'origin_id',
                        'OUTPUT': 'memory:'})['OUTPUT']

with edit(address_net6):
    for feature in address_net6.getFeatures():
        
        address_net6.updateFields()
        feature.setAttribute(feature.fieldNameIndex('garden_d'), feature['network_cost'])
        
        address_net6.updateFeature(feature)
        
    print('Community Garden network distances transfered')
    
QgsProject.instance().addMapLayer(address_net6)

#delete the fields that were added
#so that another operation can be performed

# Delete the fields in the attribute table through their corresponding index 
# working from back of table using negative numbers
features = address_net6.getFeatures()

caps = address_net6.dataProvider().capabilities()

if caps & QgsVectorDataProvider.DeleteAttributes:
    res = address_net6.dataProvider().deleteAttributes([74, 75, 76, 77, 78, 79])
    address_net6.updateFields()
        
QgsProject.instance().addMapLayer(address_net6)

# these two functions reclassify the distances that were added from the network analysis
# and multiply the reclassified distance by the standardized weight derived from the weightings
# put through the standardization python script

# these two functions reclassify the distances that were added from the network analysis
# and multiply the reclassified distance by the standardized weight derived from the weightings
# put through the standardization python script

# this block of code accesses the field calculator; however, the second parameter is a function
# this allows the same function to be reused, just change which field (s) is/are being passed into the function as a parameter(s)
# the function returns a value, and that returned value is what is entered into the field nominated in the first parameter of the field calculator function

def classify_distances():
    with edit(address_net6):
        for feature in address_net6.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('boulder_w'), funct_classify_calculator(feature['boulder_d']))
            feature.setAttribute(feature.fieldNameIndex('walls_w'), funct_classify_calculator(feature['walls_d']))
            feature.setAttribute(feature.fieldNameIndex('guests_w'), funct_classify_calculator(feature['guests_d']))
            feature.setAttribute(feature.fieldNameIndex('guardian_w'), funct_classify_calculator(feature['guardian_d']))
            feature.setAttribute(feature.fieldNameIndex('baths_w'), funct_classify_calculator(feature['baths_d']))
            feature.setAttribute(feature.fieldNameIndex('garden_w'), funct_classify_calculator(feature['garden_d']))
            address_net6.updateFeature(feature)
    print("Distances classified")

classify_distances()

def weightings():
    with edit(address_net6):
        for feature in address_net6.getFeatures():
            feature.setAttribute(feature.fieldNameIndex('boulder_w'), funct_weighting_calculator(feature['boulder_w'], boulders_standard_weight))            
            feature.setAttribute(feature.fieldNameIndex('walls_w'), funct_weighting_calculator(feature['walls_w'], northwalls_standard_weight))
            feature.setAttribute(feature.fieldNameIndex('guests_w'), funct_weighting_calculator(feature['guests_w'], guests_standard_weight))
            feature.setAttribute(feature.fieldNameIndex('guardian_w'), funct_weighting_calculator(feature['guardian_w'], guardian_standard_weight))
            feature.setAttribute(feature.fieldNameIndex('baths_w'), funct_weighting_calculator(feature['baths_w'], baths_standard_weight))
            feature.setAttribute(feature.fieldNameIndex('garden_w'), funct_weighting_calculator(feature['garden_w'], garden_standard_weight))
            address_net6.updateFeature(feature)
    print("Distances weighted")

weightings()