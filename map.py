'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
from bokeh.plotting import figure
import shapefile


class Map:
    def __init__(self):
        self.figure = figure(title='Your Location', plot_width=1200,
                             plot_height=700, x_range=(-130, -60),
                             y_range=(24, 50))
        self.x_coords = []
        self.y_coords = []
        self.sf = shapefile.Reader("StateBorders/cb_2015_us_state_5m.shp")
        self.shapes = self.sf.shapes()
        for i, shape in enumerate(self.shapes):
            self.x_coords.append([])
            self.y_coords.append([])
            for point in shape.points:
                self.x_coords[i].append(point[0])
                self.y_coords[i].append(point[1])

    def update_map(self):
        self.figure.patches(self.x_coords, self.y_coords, line_color='red')
