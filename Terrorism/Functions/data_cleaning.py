'''
The data_cleaner function was designed to cut the dataset
down to a single region and print the size of the region as a percentage
of total dataset size.

Next the function, determines the percentage of NaN values in each row,
and deletes those rows with a percentage above the threshold. 

Lastly, the function saves the cleaned dataset in the same folder as the original dataset.
'''

def data_cleaner(region, file_name, df, path, nan_threshold=20):
    
    # Cutting down to a single region.
    data = df.loc[df.region == region]
    
    # Dataset size comparison. 
    original_length = len(df) # Original length.
    region_length = len(data) # Regional length.
    print("Size of original dataset:", original_length) # Print original length.
    print("Size of remaining dataset:", region_length) # Print region length.
    print("Percentage of European attacks in the GTD:", (region_length / original_length) * 100, "%") # Print percentage.
    print("\n") # Print new line.
    
    # Determing size of NaN percentage per column.
    empty_rows = data.isna() # Get empty rows.
    aggregate_empty_rows = empty_rows.sum() # Sum empty rows.
    nan_percentage = (aggregate_empty_rows / region_length) * 100 # Determine percentage of NaN values.
    
    print("Columns and their NaN percentage:")
    print(nan_percentage) # Print percentage.
    print("\n") # Print new line.
    
    # Deleting high percentage columns.
    nan_columns = [] # Instantiate empty list to save high NaN columns into.
    
    # Iterate through columns.
    for i in range(len(nan_percentage)):
        # If the percentage of missing values is greater or equal to ten, add the index to the list.
        if nan_percentage[i] >= nan_threshold:
            nan_columns.append(i)
    
    # Drop high percentage NaN values.
    data.drop(data.columns[nan_columns], axis=1, inplace=True) 
    
    # Print update messages.
    print("Number of deleted columns:", len(nan_columns)) # Print number of deleted columns.
    print("Number of remaining columns:", len(data.columns)) # Print number of remaining columns.
    print("\n") # Print new line.
    
    # Delete other unecessary columns
    del data['eventid']
    del data['dbsource']
    del data['INT_LOG']
    del data['INT_IDEO']
    del data['INT_MISC']
    del data['INT_ANY']
    
    # Save the cleaned dataset.
    print("Saving cleaned dataset.") # Print update message.
    data.to_csv(path + file_name, index=False)