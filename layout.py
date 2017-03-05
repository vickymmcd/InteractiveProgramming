'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
from bokeh.layouts import column
from ageline import AgeLine
from map import Map
from bokeh.plotting import output_file, show


class Layout:
    def __init__(self):
        self.map = Map()
        self.ageline = AgeLine()
        self.layout = column(self.map.get_fig(), self.ageline.get_fig())

    def show_layout(self):
        output_file('layout.html')
        show(self.layout)


if __name__ == '__main__':
    layout = Layout()
    layout.show_layout()
