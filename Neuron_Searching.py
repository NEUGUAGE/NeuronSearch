#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 22 14:32:06 2023

@author: xiaozihang
"""

import numpy as np
import pandas as pd

import bokeh
import hvplot.pandas
import holoviews as hv

import bokeh.palettes
from bokeh.plotting import figure, show, output_notebook
output_notebook()

from neuprint import Client
from neuprint import fetch_roi_hierarchy
from neuprint import fetch_adjacencies, NeuronCriteria as NC
from neuprint import fetch_neurons
from neuprint import merge_neuron_properties
from neuprint.utils import connection_table_to_matrix


c = Client('neuprint.janelia.org', dataset='hemibrain:v1.2.1', token='eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJlbWFpbCI6IjUxMzI1MDY2eHpoQGdtYWlsLmNvbSIsImxldmVsIjoibm9hdXRoIiwiaW1hZ2UtdXJsIjoiaHR0cHM6Ly9saDMuZ29vZ2xldXNlcmNvbnRlbnQuY29tL2EvQUdObXl4WXNXeVlkNGg4Q2htNXA1Q1lpZW1sRE9lRHpBazdJY3BTQXhyMEM9czk2LWM_c3o9NTA_c3o9NTAiLCJleHAiOjE4NTkzNTc2MDh9.x84EVN6HTsW-KZKIFAKfljI0V7DooPON_YMKz4t6Aak')
c.fetch_version()

# query upstream information
neuron_df, conn_df = fetch_adjacencies(None, NC(type='PFN.*'))

#query downstream information
neuron_df1, conn_df1 = fetch_adjacencies(NC(type='PFN.*'),None)

conn_df = merge_neuron_properties(neuron_df, conn_df, ['type', 'instance'])

conn_df1 = merge_neuron_properties(neuron_df1, conn_df1, ['type', 'instance'])

matrix_upstream = connection_table_to_matrix(conn_df, ('type_pre', 'type_post'))

matrix_downstream = connection_table_to_matrix(conn_df1, ('type_post', 'type_pre'))


