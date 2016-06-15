# This file auto-generated by `generate_schema_interface.py`.
# Do not modify this file directly.

import traitlets as T
from ..baseobject import BaseObject
from .axisconfig import AxisConfig
from .cellconfig import CellConfig
from .facetconfig import FacetConfig
from .legendconfig import LegendConfig
from .markconfig import MarkConfig
from .scaleconfig import ScaleConfig


class Config(BaseObject):
    """Wrapper for Vega-Lite Config definition.
    
    Attributes
    ----------
    axis: AxisConfig
        Axis Config.
    background: Unicode
        CSS color property to use as background of visualization.
    cell: CellConfig
        Cell Config.
    facet: FacetConfig
        Facet Config.
    legend: LegendConfig
        Legend Config.
    mark: MarkConfig
        Mark Config.
    numberFormat: Unicode
        D3 Number format for axis labels and text tables.
    scale: ScaleConfig
        Scale Config.
    timeFormat: Unicode
        Default datetime format for axis and legend labels.
    viewport: CFloat
        The width and height of the on-screen viewport, in pixels.
    """
    axis = T.Instance(AxisConfig, allow_none=True, default_value=None, help="""Axis Config.""")
    background = T.Unicode(allow_none=True, default_value=None, help="""CSS color property to use as background of visualization.""")
    cell = T.Instance(CellConfig, allow_none=True, default_value=None, help="""Cell Config.""")
    facet = T.Instance(FacetConfig, allow_none=True, default_value=None, help="""Facet Config.""")
    legend = T.Instance(LegendConfig, allow_none=True, default_value=None, help="""Legend Config.""")
    mark = T.Instance(MarkConfig, allow_none=True, default_value=None, help="""Mark Config.""")
    numberFormat = T.Unicode(allow_none=True, default_value=None, help="""D3 Number format for axis labels and text tables.""")
    scale = T.Instance(ScaleConfig, allow_none=True, default_value=None, help="""Scale Config.""")
    timeFormat = T.Unicode(allow_none=True, default_value=None, help="""Default datetime format for axis and legend labels.""")
    viewport = T.CFloat(allow_none=True, default_value=None, help="""The width and height of the on-screen viewport, in pixels.""")
    
    def __init__(self, axis=None, background=None, cell=None, facet=None, legend=None, mark=None, numberFormat=None, scale=None, timeFormat=None, viewport=None, **kwargs):
        kwds = dict(axis=axis, background=background, cell=cell, facet=facet, legend=legend, mark=mark, numberFormat=numberFormat, scale=scale, timeFormat=timeFormat, viewport=viewport)
        kwargs.update({k:v for k, v in kwds.items() if v is not None})
        super(Config, self).__init__(**kwargs)