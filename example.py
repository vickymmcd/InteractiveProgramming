from bokeh.plotting import output_file, figure, save
import shapefile


def getParts(shapeObj):

    points = []

    num_parts = len(shapeObj.parts)
    end = len(shapeObj.points) - 1
    segments = list(shapeObj.parts) + [end]

    for i in range(num_parts):
        points.append(shapeObj.points[segments[i]:segments[i+1]])

    return points


# Return a dict with three elements
#        - state_name
#        - total_area
#        - list of list representing latitudes
#        - list of list representing longitudes
#
#  Input: State Name & ShapeFile Object


def getDict(state_name, shapefile):

    stateDict = {state_name: {}}

    rec = []
    shp = []
    points = []

    # Select only the records representing the
    # "state_name" and discard all other
    for i in shapefile.shapeRecords():

        if i.record[2] == state_name:
            rec.append(i.record)
            shp.append(i.shape)

    # In a multi record state for calculating total area
    total_area = sum([float(i[0]) for i in rec]) / (1000*1000)

    # For each selected shape object get
    # list of points while considering the cases where there may be
    # multiple parts  in a single record
    for j in shp:
        for i in getParts(j):
            points.append(i)

    # Prepare the dictionary
    #      - one representing latitudes
    #      - second representing longitudes

    lat = []
    lng = []
    for i in points:
        lat.append([j[0] for j in i])
        lng.append([j[1] for j in i])

    stateDict[state_name]['lat_list'] = lat
    stateDict[state_name]['lng_list'] = lng
    stateDict[state_name]['total_area'] = total_area

    return stateDict


dat = shapefile.Reader("StateBorders/stateborders.shp")
states = set([i[2] for i in dat.iterRecords()])

'''p = figure(title="My first interactive plot")
x_coords = [0, 1, 2, 3, 4]
y_coords = [5, 4, 1, 2, 0]
p.circle(x=x_coords, y=y_coords, size=10, color="red")
outfp = r"map.html"
save(obj=p, filename=outfp)'''


outputpf = r"map.html"

TOOLS = "pan,wheel_zoom,box_zoom,reset,previewsave"
p = figure(title="Map of India", tools=TOOLS, plot_width=900, plot_height=800)


for state_name in states:
    data = getDict(state_name, dat)
    p.patches(data[state_name]['lat_list'], data[state_name]['lng_list'],
              line_color="black")

save(obj=p, filename=outputpf)
