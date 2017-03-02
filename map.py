'''
Authors: Vicky McDermott and Emily Lepert

This function represents the visual Map object.
'''
import geoplotlib
from geoplotlib.utils import read_csv, BoundingBox


class Map:
    def __init__(self):
        self.map = map

    if __name__ == '__main__':
        data = read_csv('us-state-capitals.csv')
        geoplotlib.hist(data, colorscale='sqrt', binsize=60)
        geoplotlib.set_bbox(BoundingBox.USA)
        geoplotlib.show()
