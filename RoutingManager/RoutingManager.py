import numpy as np
import random
from itertools import permutations
from math import *

class RoutingMngr(object):
    def __init__(self):
        return

    def GetRandomClusterArrangment(self, nb_clusters : int, nb_points : int) -> list[int]:
        return random.sample(range(nb_clusters), nb_points)

    def GetLoopCandidates(self,
                          coords_Array : np.array,
                          cluster_Array : np.array,
                          nb_Clusters : int,
                          nb_Points : int,
                          nb_Candidates : int) -> np.array:
        cluster_LookUpTable = list()

        # Building cluster lookup dict
        for i in np.arange(nb_Clusters):
            cluster_LookUpTable.append(list())
        for index, cluster in enumerate(cluster_Array):
            cluster_LookUpTable[cluster].append(index)

        # Generate loop candidate
        loopCandidates = []
        for i in range(nb_Candidates):
            group = [ coords_Array[random.choice(cluster_LookUpTable[i])] for i in self.GetRandomClusterArrangment(nb_Clusters, nb_Points) ]
            loopCandidates.append(group)

        return loopCandidates

    def _Haversine(self, coord1 : list[float], coord2 : list[float]) -> float:
        R = 6371  # Earth radius in km
        lat1, lon1 = map(radians, coord1)
        lat2, lon2 = map(radians, coord2)
        dlat = lat2 - lat1
        dlon = lon2 - lon1
        a = sin(dlat / 2) ** 2 + cos(lat1) * cos(lat2) * sin(dlon / 2) ** 2
        return 2 * R * atan2(sqrt(a), sqrt(1 - a))

    def _LoopHaversineDistance(self, path : list[list[float]]) -> float:
        dist = 0
        for i in range(len(path)):
            dist += self._Haversine(path[i], path[(i + 1) % len(path)])
        return dist

    def _GetLoopMinimalHaversineDistance(self, points : list[list[float]]) -> (list[list[float]], float):
        start = points[0]
        others = points[1:]

        min_path = None
        min_dist = float('inf')

        for perm in permutations(others):
            path = [start] + list(perm)
            dist = self._LoopHaversineDistance(path)
            print(dist)
            if dist < min_dist:
                min_dist = dist
                min_path = path

        return min_path, min_dist