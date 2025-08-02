import numpy as np
from sklearn.cluster import KMeans

class ClusteringMngr(object):
    def __init__(self):
        return

    def Cluster(self, poisDict : dict, n_clusters : int) -> np.array:
        latLonArray = self.ConvertDictToNumpyArray(poisDict)
        return KMeans(n_clusters=n_clusters, random_state=0).fit(latLonArray).predict(latLonArray)

    def ConvertDictToNumpyArray(self, poisDict: dict) -> np.array:
        returnedArray = np.zeros((len(poisDict["elements"]), 2), dtype=float)
        for i, element in enumerate(poisDict["elements"]):
            if(element["type"] == "node"):
                returnedArray[i, 0] = element["lat"]
                returnedArray[i, 1] = element["lon"]
            elif(element["type"] == "way"):
                returnedArray[i, 0] = element["center"]["lat"]
                returnedArray[i, 1] = element["center"]["lon"]
        return returnedArray

