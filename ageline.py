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
        self.mapper = CategoricalColorMapper(factors=[0, .01, .02, .03, .04,
                                                      .05, .06, .07, .08, .09,
                                                      .1, .11, .12, .13, .14,
                                                      .15, .16, .17, .18, .19,
                                                      .2, .21, .22, .23, .24,
                                                      .25, .26, .27, .28, .29,
                                                      .3, .31, .32, .33, .34,
                                                      .35, .36, .37, .38, .39,
                                                      .4, .41, .42, .43, .44,
                                                      .45, .46, .47, .48, .49,
                                                      .5, .51, .52, .53, .54,
                                                      .55, .56, .57, .58, .59,
                                                      .6, .61, .62, .63, .64,
                                                      .65, .66, .67, .68, .69,
                                                      .7, .71, .72, .73, .74,
                                                      .75, .76, .77, .78, .79,
                                                      .8, .81, .82, .83, .84,
                                                      .85, .86, .87, .88, .89,
                                                      .9, .91, .92, .93, .94,
                                                      .95, .96, .97, .98, .99,
                                                      1],
                                             palette=bokeh.palettes.
                                             magma(101))
        self.hover = HoverTool(tooltips=[('Age', '@age'),
                                         ('Probability', '@probs')])
        self.figure = figure(title='Your Age', plot_height=200, plot_width=700,
                             tools=[self.hover, 'pan', 'wheel_zoom'],
                             x_axis_label='Age')

    def get_fig(self, probs):
        self.update_ageline(probs)
        return self.figure

    def update_ageline(self, probs=[]):
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'probs': probs,
                                             'age': ['18-29', '30-44', '45-59',
                                                     '60+']})
        self.figure.patches(self.x_coords, self.y_coords, source=self.source,
                            line_color='red', color={'field': 'probs',
                                                     'transform': self.mapper})

    def show_the_ageline(self):
        self.update_ageline([.25, .25, .25, .25])
        output_file('ageline.html')
        show(self.figure)


if __name__ == '__main__':
    age_line = AgeLine()
    age_line.show_the_ageline()
