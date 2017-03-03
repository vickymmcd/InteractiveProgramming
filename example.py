from bokeh.plotting import output_file, figure, save
import shapefile

sf = shapefile.Reader("cb_2015_us_state_5m.shp")
shapes = sf.shapes()
print(len(shapes))
x_coords = []
y_coords = []
p = figure(title='My State', plot_width=1200, plot_height=700,
           x_range=(-130, -60), y_range=(24, 50))
for i, shape in enumerate(shapes):
    x_coords.append([])
    y_coords.append([])
    for point in shape.points:
        x_coords[i].append(point[0])
        y_coords[i].append(point[1])
p.patches(x_coords, y_coords, line_color='red')
outputpf = r"map.html"
save(obj=p, filename=outputpf)
