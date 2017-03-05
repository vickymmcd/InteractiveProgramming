'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, ColumnDataSource


class AgeLine:
    def __init__(self):
        self.figure = figure(title='Your Age', plot_height=200, plot_width=700)
        self.x_coords = [[18, 18, 30, 30], [30, 30, 45, 45], [45, 45, 60, 60],
                         [60, 60, 75, 75]]
        self.y_coords = [[0, 5, 5, 0], [0, 5, 5, 0], [0, 5, 5, 0],
                         [0, 5, 5, 0]]
        self.mapper = CategoricalColorMapper(factors=[40, 50, 60, 70],
                                             palette=['red', 'green',
                                                      'blue', 'yellow'])
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'probs': [40, 50, 60, 70]})

    def get_fig(self):
        self.update_ageline()
        return self.figure

    def update_ageline(self, probs=[40, 50, 60, 70]):
        self.figure.patches(self.x_coords, self.y_coords, source=self.source,
                            line_color='red', color={'field': 'probs',
                                                     'transform': self.mapper})
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'probs': probs})

    def show_the_ageline(self):
        self.update_ageline()
        output_file('ageline.html')
        show(self.figure)


if __name__ == '__main__':
    age_line = AgeLine()
    age_line.show_the_ageline()
