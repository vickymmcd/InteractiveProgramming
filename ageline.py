'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Age Line object.
'''
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, ColumnDataSource, HoverTool
import bokeh.palettes


class AgeLine:
    def __init__(self):
        self.x_coords = [[18, 18, 30, 30], [30, 30, 45, 45], [45, 45, 60, 60],
                         [60, 60, 75, 75]]
        self.y_coords = [[0, 5, 5, 0], [0, 5, 5, 0], [0, 5, 5, 0],
                         [0, 5, 5, 0]]
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
        self.initial_probs = [25, 25, 25, 25]
        self.hover = HoverTool(tooltips=[('Age', '@age'),
                                         ('Probability', '@probs')])
        self.figure1 = figure(title='Your Age', plot_height=200,
                              plot_width=700,
                              tools=[self.hover, 'pan', 'wheel_zoom'],
                              x_axis_label='Age')
        self.source1 = ColumnDataSource(data={'x_coords': self.x_coords,
                                              'y_coords': self.y_coords,
                                              'probs': self.initial_probs,
                                              'age': ['18-29', '30-44',
                                                      '45-59', '60+']})
        self.figure1.patches(self.x_coords, self.y_coords, source=self.source1,
                             line_color='red', color={'field': 'probs',
                                                      'transform':
                                                      self.mapper})

    def get_fig(self, probs):
        return self.figure1

    def update_ageline(self, probs=[]):
        self.source1.data['probs'] = probs
        print('ageline updated')

if __name__ == '__main__':
    age_line = AgeLine()
