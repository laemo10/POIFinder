import numpy as np
from ClusteringManager import ClusteringMngr
from OverpassWrapper import OverpassWrapper
from RoutingManager import RoutingMngr
import matplotlib.pyplot as plt

overpassWrapper = OverpassWrapper()
clusterMngr = ClusteringMngr()
routingMngr = RoutingMngr()

# Mes coordonnées : 46.787485,-71.277272
# Distance/nb_pts semble être la bonne valeur
poisDict = overpassWrapper.Request(46.787485,-71.277272, 1000, ["restaurant", "cafe", "pub"] ,100)

poisArray = clusterMngr.ConvertDictToNumpyArray(poisDict)
clusters_array = clusterMngr.Cluster(poisDict, 6)

# Display
plt.scatter(poisArray[:,0], poisArray[:,1], c=clusters_array)
plt.scatter(46.787485, -71.277272, color = "red")
plt.show()

loopCandidates = routingMngr.GetLoopCandidates(poisArray, clusters_array, 6, 5, 3)
properpath, minDist = routingMngr.GetLoopMinimalHaversineDistance(loopCandidates[0])
print(properpath)
print(minDist)

# Display
plt.scatter(np.array(properpath)[:,0], np.array(properpath)[:,1], c=range(len(properpath)))
plt.scatter(46.787485, -71.277272, color = "red")
plt.colorbar()
plt.show()