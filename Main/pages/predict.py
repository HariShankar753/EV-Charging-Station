# Import required libraries
import pandas as pd
from sklearn.cluster import KMeans
import folium


m = folium.Map(location=[37.040539, -95.271387], zoom_start=5)
end=30000
# Load dataset
charging_stations = pd.read_csv("E:\\ev_station.csv")

# Extract latitude and longitude features
X = charging_stations[['Latitude', 'Longitude']]

# Implement K-Means clustering algorithm
kmeans = KMeans(n_clusters=end).fit(X)

df1=pd.read_csv("E:\\ev_station.csv",usecols=[5])
df2=pd.read_csv("E:\\ev_station.csv",usecols=[6])

x=[]
for data in df1:
    for d in df1[data]:
        x.append(d)    
        
y=[]
for data in df2:
    for d in df2[data]:
        y.append(d)    

a=0
k=0
for d in x:
    b=[x[a],y[a]]
    # Predict the cluster for a new location
    new_location = [b]  # Sample latitude and longitude
    predicted_cluster = kmeans.predict(new_location)
    
    # Get the centroid of the predicted cluster
    centroid = kmeans.cluster_centers_[predicted_cluster[0]]

    # Print the predicted latitude and longitude
    print('Predicted latitude:', centroid[0])
    print('Predicted longitude:', centroid[1])
    b=[centroid[0],centroid[1]]
    
    if b not in x:
        print(a)
        folium.CircleMarker(
            b,
            radius=2,
        ).add_to(m)
        k=k+1
        
    if a==end:
        break
    a=a+1
    

m.save(r"C:\Users\srcas\Desktop\Project\Main\pages\predict.html")
