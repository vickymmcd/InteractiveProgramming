from bokeh.plotting import output_file, figure, save, show
from bokeh.layouts import column
from bokeh.models import CategoricalColorMapper, ColumnDataSource
import shapefile

sf = shapefile.Reader("StateBorders/cb_2015_us_state_5m.shp")
shapes = sf.shapes()
print(len(shapes))
x_coords = []
y_coords = []
mapper = CategoricalColorMapper(factors=[40, 50, 60, 70],
                                palette=['red', 'green', 'blue', 'yellow'])
p = figure(title='Your Location', plot_width=1200, plot_height=700,
           x_range=(-130, -60), y_range=(24, 50))
for i, shape in enumerate(shapes):
    x_coords.append([])
    y_coords.append([])
    for point in shape.points:
        x_coords[i].append(point[0])
        y_coords[i].append(point[1])
p.patches(x_coords, y_coords, line_color='red')
p2 = figure(title='Your Age', plot_height=200, plot_width=700)
x_coords = [[18, 18, 30, 30], [30, 30, 45, 45], [45, 45, 60, 60],
            [60, 60, 75, 75]]
y_coords = [[0, 5, 5, 0], [0, 5, 5, 0], [0, 5, 5, 0], [0, 5, 5, 0]]
source = ColumnDataSource(data={'x_coords': x_coords, 'y_coords': y_coords,
                                'probs': [40, 50, 60, 70]})
p2.patches(x_coords, y_coords, source=source, line_color='red',
           color={'field': 'probs', 'transform': mapper})
output_file('map.html')
layout = column(p, p2)
show(layout)
