"""
Unit tests for indicators from marketwizard.indicators.averages module.
"""

import unittest
from coverage.stream import testindicator
from market.stream.averages import *


#----------------------------------------------------------------------
EMA_Test = testindicator(__name__, "EMA_Test",
#----------------------------------------------------------------------
EMA, (
    ((58.90,), (58.90,)),
    ((51.53,), (55.95,)),
    ((50.23,), (53.66,)),
    ((56.43,), (54.77,)),
    ((64.48,), (58.65,)),
    ((51.82,), (55.92,)),
    ((36.13,), (48.00,)),
    ((47.64,), (47.86,)),
    ((57.88,), (51.87,)),
    ((52.50,), (52.12,)),
    ((53.62,), (52.72,)),
    ((61.95,), (56.41,)),
    ((77.86,), (64.99,)),
    ((71.11,), (67.44,)),
    ((81.03,), (72.88,)),
    ((95.18,), (81.80,)),
    ((96.38,), (87.63,)),
    ((121.58,), (101.21,)),
    ((138.58,), (116.16,)),
), period=4)


#----------------------------------------------------------------------
OWMA_Test = testindicator(__name__, "OWMA_Test",
#----------------------------------------------------------------------
OWMA, (
    ((51.56,), (None,)),
    ((50.21,), (None,)),
    ((47.93,), (None,)),
    ((45.92,), (None,)),
    ((44.90,), (None,)),
    ((41.55,), (45.39,)),
    ((37.70,), (42.73,)),
    ((33.45,), (39.52,)),
    ((38.97,), (38.68,)),
    ((37.13,), (37.74,)),
    ((36.13,), (36.93,)),
    ((40.91,), (37.91,)),
    ((43.07,), (39.54,)),
    ((44.21,), (41.23,)),
    ((46.19,), (42.98,)),
    ((48.46,), (45.03,)),
    ((50.85,), (47.23,)),
    ((47.52,), (47.77,)),
    ((46.29,), (47.65,)),
    ((44.49,), (46.86,)),
    ((47.05,), (46.79,)),
    ((48.24,), (47.02,)),
    ((47.64,), (47.09,)),
    ((53.55,), (48.99,)),
    ((53.35,), (50.56,)),
    ((54.80,), (52.20,)),
    ((54.11,), (53.15,)),
    ((53.31,), (53.54,)),
    ((55.71,), (54.38,)),
    ((55.26,), (54.70,)),
), period=6)


#----------------------------------------------------------------------
SMA_Test = testindicator(__name__, "SMA_Test",
#----------------------------------------------------------------------
SMA, (
    ((58.90,), (None,)),
    ((51.53,), (None,)),
    ((50.23,), (None,)),
    ((56.43,), (54.27,)),
    ((64.48,), (55.67,)),
    ((51.82,), (55.74,)),
    ((36.13,), (52.22,)),
    ((47.64,), (50.02,)),
    ((57.88,), (48.37,)),
    ((52.50,), (48.54,)),
    ((53.62,), (52.91,)),
    ((61.95,), (56.49,)),
    ((77.86,), (61.48,)),
    ((71.11,), (66.14,)),
    ((81.03,), (72.99,)),
    ((95.18,), (81.30,)),
    ((96.38,), (85.93,)),
    ((121.58,), (98.54,)),
    ((138.58,), (112.93,)),
), period=4)


#----------------------------------------------------------------------
WMA_Test = testindicator(__name__, "WMA_Test",
#----------------------------------------------------------------------
WMA, (
    ((51.56, 62), (None,)),
    ((50.21, 74), (None,)),
    ((47.93, 65), (None,)),
    ((45.92, 34), (None,)),
    ((44.90, 65), (None,)),
    ((41.55, 36), (47.63,)),
    ((37.70, 83), (44.64,)),
    ((33.45, 64), (41.39,)),
    ((38.97, 23), (39.81,)),
    ((37.13, 55), (38.72,)),
    ((36.13, 34), (37.06,)),
    ((40.91, 65), (37.33,)),
    ((43.07, 34), (37.93,)),
    ((44.21, 65), (40.45,)),
    ((46.19, 23), (41.05,)),
    ((48.46, 65), (43.49,)),
    ((50.85, 76), (45.96,)),
    ((47.52, 53), (47.26,)),
    ((46.29, 12), (47.70,)),
    ((44.49, 34), (48.15,)),
    ((47.05, 45), (48.13,)),
    ((48.24, 52), (48.08,)),
    ((47.64, 34), (47.10,)),
    ((53.55, 62), (48.68,)),
    ((53.35, 34), (49.40,)),
    ((54.80, 54), (51.03,)),
    ((54.11, 23), (51.99,)),
    ((53.31, 54), (53.01,)),
    ((55.71, 23), (53.99,)),
    ((55.26, 54), (54.39,)),
), period=6)


# TODO: Check tests coverage

if __name__ == '__main__':
    unittest.main()