import os
import pandas as pd 
import numpy as np 
import seaborn as sns 
import matplotlib.pyplot as plt 
star_df=pd.read_csv('cleaned_star_data.csv')
print(star_df)
temperature=star_df['Temperature (K)'].values
print(temperature)

abs_mag=star_df['Absolute magnitude(Mv)'].values
print(abs_mag)

star_type=star_df['Star type'].values


# Python Dictionaries
star_types = {
    0: {'label': 'Brown Dwarf', 'color': 'brown', 'size': 30, 'marker': '.'},
    1: {'label': 'Red Dwarf', 'color': 'red', 'size': 35, 'marker': '.'},
    2: {'label': 'White Dwarf', 'color': 'white', 'size': 40, 'marker': '.'},
    3: {'label': 'Main Sequence', 'color': 'cyan', 'size': 30, 'marker': 'o'},
    4: {'label': 'Supergiants', 'color': 'orange', 'size': 100, 'marker': 'o'},
    5: {'label': 'Hypergiants', 'color': 'maroon', 'size': 150, 'marker': 'o'}
}



plt.scatter(temperature, abs_mag)

plt.show()
'''
It does not show the supergiants because in x-axis they goo from a higher to a lower value completly opposite to what we have done
so we will invert both of the axis by matplotlib
'''



plt.scatter(temperature, abs_mag)

plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.show()
axes=[]
labels=set()



for i in range(len(star_type)):
    properties=star_types[star_type[i]]
    
    if properties['label'] not in labels:
        ax = plt.scatter(temperature[i], abs_mag[i],
                         s=properties['size'],
                         c=properties['color'],
                         marker=properties['marker'],
                         label=properties['label'])
        
        axes.append(ax)
        labels.add(properties['label'])
    else:
        plt.scatter(temperature[i], abs_mag[i],
                    s=properties['size'],
                    c=properties['color'],
                    marker=properties['marker'],
                    label=properties['label'])
        

plt.legend(handles=axes)

plt.gca().invert_xaxis()
plt.gca().invert_yaxis()

plt.show()
