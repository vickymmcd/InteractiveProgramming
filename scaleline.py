'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Scale Line object.
'''
from bokeh.plotting import figure, output_file, show
from bokeh.models import CategoricalColorMapper, ColumnDataSource
import bokeh.palettes


class ScaleLine:
    def __init__(self):
        self.x_coords = [[0, 0, .1, .1], [.1, .1, .2, .2], [.2, .2, .3, .3],
                         [.3, .3, .4, .4], [.4, .4, .5, .5], [.5, .5, .6, .6],
                         [.6, .6, .7, .7], [.7, .7, .8, .8], [.8, .8, .9, .9],
                         [.9, .9, 1, 1]]
        self.y_coords = [[0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0],
                         [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0],
                         [0, 1, 1, 0], [0, 1, 1, 0], [0, 1, 1, 0],
                         [0, 1, 1, 0]]
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
        self.figure = figure(title='Color Scale', plot_height=100, tools=[],
                             plot_width=700, x_axis_label='Probability')

    def get_fig(self):
        self.update_scaleline()
        return self.figure

    def update_scaleline(self, probs=[.1, .2, .3, .4, .5, .6, .7, .8, .9, 1]):
        self.source = ColumnDataSource(data={'x_coords': self.x_coords,
                                             'y_coords': self.y_coords,
                                             'probs': probs})
        self.figure.patches(self.x_coords, self.y_coords, source=self.source,
                            color={'field': 'probs', 'transform': self.mapper})

    def show_the_scaleline(self):
        self.update_scaleline()
        output_file('scaleline.html')
        show(self.figure)


if __name__ == '__main__':
    scale_line = ScaleLine()
    scale_line.show_the_scaleline()
