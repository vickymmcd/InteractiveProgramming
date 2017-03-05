'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, ColumnDataSource
import bokeh.palettes
import shapefile


class Map:
    def __init__(self):
        self.figure = figure(title='Your Location', plot_width=1200,
                             plot_height=700, x_range=(-130, -60),
                             y_range=(24, 50))
        self.x_coords = []
        self.y_coords = []
        self.regions = [8, 4, 0, 8, 6, 2, 1, 7, 1, 9, 3, 8, 9, 2, 7, 1, 8, 4,
                        1, 5, 8, 8, 0, 7, 5, 4, 4, 7, 4, 9, 5, 7, 0, 0, 5, 7,
                        7, 5, 5, 0, 0, 0, 0, 6, 6, 3, 4, 3, 9, 2, 4, 1, 2, 7,
                        4, 8]
        self.mapper = CategoricalColorMapper(factors=[0, .1, .2, .3, .4, .5,
                                                      .6, .7, .8, .9, 1],
                                             palette=bokeh.palettes.
                                             magma(11))
        self.sf = shapefile.Reader("StateBorders/cb_2015_us_state_5m.shp")
        self.shapes = self.sf.shapes()
        for i, shape in enumerate(self.shapes):
            self.x_coords.append([])
            self.y_coords.append([])
            for point in shape.points:
                self.x_coords[i].append(point[0])
                self.y_coords[i].append(point[1])
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'region': self.regions})

    def get_fig(self, probs):
        self.update_map(probs)
        return self.figure

    def update_map(self, probs=[]):
        # each state is part of certain region
        # go through the region of each state and assigns
        # the probability for that region to that state
        # probs list should be in region order so 1st element
        # has probability for first region, etc.
        state_probs = []
        for region in self.regions:
            state_probs.append(probs[region])
        print(state_probs)
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'region': self.regions,
                                             'probability': state_probs})
        self.figure.patches(self.x_coords, self.y_coords, source=self.source,
                            line_color='red', color={'field': 'probability',
                                                     'transform': self.mapper})

    def show_the_map(self):
        self.update_map([1, 0, .4, .5, .7, .9, 1, 0, .3, .4])
        output_file('map.html')
        show(self.figure)


if __name__ == '__main__':
    map = Map()
    map.show_the_map()
