'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
from bokeh.plotting import figure
from bokeh.models import CategoricalColorMapper, ColumnDataSource, HoverTool
import bokeh.palettes
import shapefile


class Map:
    def __init__(self):
        '''
        This initializes the Map class and assigns the x
        coordinates, y coordinates, and color mapper. It also
        sets up the initial probability, hover tool, and sets
        up the figures and columndatasource for the map.

        '''
        self.x_coords = []
        self.y_coords = []
        # list of regions associated with each state
        self.regions = [8, 4, 0, 8, 6, 2, 1, 7, 1, 9, 3, 8, 9, 2, 7, 1, 8, 4,
                        1, 5, 8, 8, 0, 7, 5, 4, 4, 7, 4, 9, 5, 7, 0, 0, 5, 7,
                        7, 5, 5, 0, 0, 0, 0, 6, 6, 3, 4, 3, 9, 2, 4, 1, 2, 7,
                        4, 8]
        self.mapper = CategoricalColorMapper(factors=[0, 1, 2, 3, 4,
                                                      5, 6, 7, 8, 9,
                                                      10, 11, 12, 13, 14,
                                                      15, 16, 17, 18, 19,
                                                      20, 21, 22, 23, 24,
                                                      25, 26, 27, 28, 29,
                                                      30, 31, 32, 33, 34,
                                                      35, 36, 37, 38, 39,
                                                      40, 41, 42, 43, 44,
                                                      45, 46, 47, 48, 49,
                                                      50, 51, 52, 53, 54,
                                                      55, 56, 57, 58, 59,
                                                      60, 61, 62, 63, 64,
                                                      65, 66, 67, 68, 69,
                                                      70, 71, 72, 73, 74,
                                                      75, 76, 77, 78, 79,
                                                      80, 81, 82, 83, 84,
                                                      85, 86, 87, 88, 89,
                                                      90, 91, 92, 93, 94,
                                                      95, 96, 97, 98, 99,
                                                      100],
                                             palette=bokeh.palettes.
                                             viridis(101))
        # get the x and y coordinates of the states from the shapefile
        self.sf = shapefile.Reader("StateBorders/cb_2015_us_state_5m.shp")
        self.shapes = self.sf.shapes()
        for i, shape in enumerate(self.shapes):
            self.x_coords.append([])
            self.y_coords.append([])
            for point in shape.points:
                self.x_coords[i].append(point[0])
                self.y_coords[i].append(point[1])
        self.hover = HoverTool(tooltips=[('Region', '@region_name'),
                                         ('Probability', '@probability')])
        self.figure = figure(title='Your Location', plot_width=1200,
                             plot_height=700, x_range=(-130, -60),
                             y_range=(24, 50), tools=[self.hover, 'pan',
                                                      'wheel_zoom'])
        self.region_names = ['Unknown', 'East North Central',
                             'East South Central', 'Middle Atlantic',
                             'Mountain', 'New England', 'Pacific',
                             'South Atlantic', 'West North Central',
                             'West South Central']
        self.initial_probs = [0, 11, 11, 11, 11, 11, 11, 11, 11, 11]
        # goes through the probability and puts the probability for the
        # corresponding region with each state
        state_probs = []
        state_regions = []
        for region in self.regions:
            state_probs.append(self.initial_probs[region])
            state_regions.append(self.region_names[region])
        print(state_probs)
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'region_num': self.regions,
                                             'probability': state_probs,
                                             'region_name': state_regions})
        self.figure.patches(self.x_coords, self.y_coords, source=self.source,
                            line_color='red', color={'field': 'probability',
                                                     'transform': self.mapper})

    def get_fig(self, probs):
        '''
        Returns the map figure which can be used
        and shown in the layout

        probs: list containing 10 probabilities that
        a person is from each of the 10 regions
        '''
        return self.figure

    def update_map(self, probs=[]):
        '''
        Updates the colors and values of the probabilities
        in the map by changing the value of probability in
        the columnddatasource
        Each state is part of certain region,
        go through the region of each state and assign
        the probability for that region to that state.
        Probs list should be in region order so 1st element
        has probability for first region, etc.

        probs: list containing 10 probabilities that
        a person is from each of the 10 regions
        '''
        state_probs = []
        state_regions = []
        for region in self.regions:
            state_probs.append(probs[region])
            state_regions.append(self.region_names[region])
        self.source.data['probability'] = state_probs
        print('map updated')


if __name__ == '__main__':
    map = Map()
