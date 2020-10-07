import pandas as pd
import numpy as np
import xml.etree.ElementTree as ET
from pykalman import KalmanFilter


# Calculate distances function
def distance(df):
    
    # taken from https://stackoverflow.com/questions/27928/calculate-distance-between-two-latitude-longitude-points-haversine-formula/21623206
    p = np.pi/180
    a = 0.5 - np.cos((df['lat2']-df['lat'])*p)/2 + np.cos(df['lat']*p) * np.cos(df['lat2']*p) * (1-np.cos((df['lon2']-df['lon'])*p))/2
    df['distance'] = 12742000 * np.arcsin(np.sqrt(a))
    s = df['distance'].sum()
    return s

def output_gpx(points, output_filename):
    """
    Output a GPX file with latitude and longitude from the points DataFrame.
    """
    from xml.dom.minidom import getDOMImplementation
    def append_trkpt(pt, trkseg, doc):
        trkpt = doc.createElement('trkpt')
        trkpt.setAttribute('lat', '%.8f' % (pt['lat']))
        trkpt.setAttribute('lon', '%.8f' % (pt['lon']))
        trkseg.appendChild(trkpt)
    
    doc = getDOMImplementation().createDocument(None, 'gpx', None)
    trk = doc.createElement('trk')
    doc.documentElement.appendChild(trk)
    trkseg = doc.createElement('trkseg')
    trk.appendChild(trkseg)
    
    points.apply(append_trkpt, axis=1, trkseg=trkseg, doc=doc)
    
    with open(output_filename, 'w') as fh:
        doc.writexml(fh, indent=' ')


def main():
    
    
    ###### Read the XML ######
    
    filename1 = "walk1.gpx"

    parse_result = ET.parse(filename1)

    def element_to_data(elem):
        lat = float(elem.get('lat'))
        lon = float(elem.get('lon'))
        return lat, lon

    trkpt_elements = parse_result.iter('{http://www.topografix.com/GPX/1/0}trkpt')

    points = pd.DataFrame(list(map(element_to_data, trkpt_elements)),columns=['lat','lon'])

    # Make a copy of the data frame for later use
    copy = points.copy()
    
    
    ###### Calculate Distances ######
    
    # Shift to get adjacent points into the same rows
    shifted =(points.shift(periods=1,fill_value=0))
    points['lat2'] = shifted['lat']
    points['lon2'] = shifted['lon']
    points = points.drop(points.index[0])
    
    
    ###### Kalman Filtering ######
    
    initial_state = copy.iloc[0]
    observation_covariance = np.diag([18, 18]) ** 2 # TODO: shouldn't be zero
    transition_covariance = np.diag([10, 10]) ** 2 # TODO: shouldn't be zero
    transition = [[1,0], [0,1]] 
    
    kf = KalmanFilter(
        initial_state_mean=initial_state,
        observation_covariance=observation_covariance,
        transition_covariance=transition_covariance,
        transition_matrices=transition
    )
    
    smoothed_points, _ = kf.smooth(copy)
    true_points = pd.DataFrame({'lat': smoothed_points[:, 0], 'lon': smoothed_points[:, 1]})
    
    # Shift the dataset copy to get adjacent points into the same rows
    shifted =(true_points.shift(periods=1,fill_value=0))
    true_points['lat2'] = shifted['lat']
    true_points['lon2'] = shifted['lon']
    true_points = true_points.drop(true_points.index[0])
    
    # Call the distance function
    unfiltered_distance = distance(points)
    filtered_distance = distance(true_points)
    
    # Print the distances
    print('Unfiltered distance: %0.2f meters' % unfiltered_distance )
    print('Filtered distance: %0.2f meters' % filtered_distance )
 
    # Create .gpx file
    output_gpx(true_points, 'out.gpx')


if __name__ == '__main__':
    main()