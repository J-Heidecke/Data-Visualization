'''
This file contains various classes that create maps. These range in complexity.
'''

# Import libraries.

import altair as alt
alt.data_transformers.disable_max_rows() # Disable max rows for Altair.
from vega_datasets import data

'''
The simple_map function maps a plot that displays the distribution of terrorist activity 
in a certain region, the region has to be manually adjusted.
'''

def simple_map(df, x_translation, y_translation, map_scale):

    map_data = alt.topo_feature(data.world_110m.url, 'countries') # Get a world map from vega datasets.
    # Set background as the map imported.
    background = alt.Chart(map_data).mark_geoshape(
        color='grey', # Set colour as grey.
        fill='black', # The countries themselves as black.
        stroke='grey' # The borders as grey
    ).project(
        type='stereographic', # Set type of projection.
        scale=map_scale, # Apply scaling.
        translate=[x_translation, y_translation] # Apply translation.
    ).properties(
        width=850, # Set width.
        height=520, # Set height.
    )

    # Plot circles according to longitude and lattitude.
    points = alt.Chart(df).mark_circle(opacity=0.7).encode(
        longitude='longitude',
        latitude='latitude',
        color=alt.Color('count()', scale=alt.Scale(scheme='reds'), legend=None), # Set colour according to counts in a place.
        size=alt.Size('count()', scale=alt.Scale(range=[4, 1600]), legend=None) # Set colour according to counts in a place.
    ).project(
        type='stereographic', # Set type of projection.
        scale=map_scale, # Apply translation.
        translate=[x_translation, y_translation] # Apply translation.
    ).properties(
        width=850, # Set width.
        height=520 # Set height.
    )
    
    map_projection = (background + points) # Combine both plots.
    
    return map_projection # Return plot.