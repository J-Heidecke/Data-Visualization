'''
The eda class carries out a basic exploratory data analysis
by plotting pre-defined plots which have been judged as imported from 
previous analyses. These are:
1. A time line of the overall terrorist activity.
2. A bar chart of the overall activity in each country.
3. An area chart of the groups active in the selected region 
'''
# Import libraries.
import altair as alt
alt.data_transformers.disable_max_rows() # Disable max rows for Altair.

class eda:
    def __init__(self, df, h=600, w=800):
        self.df = df
        self.h = h
        self.w = w
    
    # The simple_plots() function plots two of the three intended targets of
    # the EDA - the overall time line of terrorism and terrorist activity per country. 
    def simple_plots(self):
        
        # Time line of overall terrorist activity.
        time_line = alt.Chart(self.df).mark_bar().encode(
                x=alt.X('iyear', title='Year'),
                y=alt.Y('count()', title='Count')
            ).properties(
                height=self.h,
                width=self.w
            )

        # Terrorist activity per country.
        country_activity = alt.Chart(self.df).mark_bar().encode(
            x=alt.X('country_txt', title='Country', sort='-y'),
            y=alt.X('count()', title='Count')
        ).properties(
                height=self.h,
                width=self.w
        )

        # Return plots
        return time_line, country_activity  
    
    # This function plots the third intended plot of the EDA
    # - the group plot. It also calculates the percentage of 
    # terrorist acts committed and plots the groups activity across time. 
    def group_plot(self):
        
        # Calculate unknown incidents.
    
        df_no_unknown = self.df[self.df.gname != 'Unknown'] # Remove 'Unknown' from 'gname'.
        print('Percentage of attacks committed by known groups:', len(df_no_unknown) / len(self.df) * 100)
        print('\n') # Print new line.
        # Find the top 20 most active groups in the dataset.
        active_groups = df_no_unknown['gname'].value_counts().nlargest(20) 
        print('Percentage of the attacks committed by the top 20 most active groups: ',
              active_groups.sum() / len(df_no_unknown) * 100) # Print message.
        print('\n') # Print new line.
        print(active_groups) # Print most active groups.
        
        # Plot area graph.
        
        
        # Create a selection that chooses the nearest point & selects based on x-value
        nearest = alt.selection(type='single', nearest=True, on='mouseover',
                                fields=['iyear'], empty='none')

        groups = alt.Chart(df_no_unknown).mark_area(opacity=0.3).encode(
            x=alt.X('iyear', title='Year'),
            y=alt.Y('count():Q', title='Count', stack=None),
            color=alt.Color('gname:N', legend=None)
            ).properties(
                height=600,
                width=800
            )

        # Transparent selectors across the chart. This is what tells us
        # the x-value of the cursor
        selectors = alt.Chart(df_no_unknown).mark_point().encode(
            x=alt.X('iyear', title='Year'),
            opacity=alt.value(0),
        ).add_selection(
            nearest
        )

        # Draw points on the line, and highlight based on selection
        points = groups.mark_point().encode(
            opacity=alt.condition(nearest, alt.value(1), alt.value(0))
            )

        # Draw text labels near the points, and highlight based on selection
        text = groups.mark_text(align='left', dx=1, dy=-1).encode(
            text=alt.condition(nearest, 'gname', alt.value(' '))
            )

        # Put the layers into a chart and bind the data
        final = alt.layer(
            groups, selectors, points, text
        ).properties(
            width=900, height=350
        )
        
        return final # Return final chart.