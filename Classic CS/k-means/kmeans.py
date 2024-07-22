from __future__ import annotations
from typing import TypeVar, Generic, List, Sequence, Iterator, Tuple
from copy import deepcopy
from functools import partial
from random import uniform
from statistics import mean, pstdev
from dataclasses import dataclass
from data_point import DataPoint
import pandas
import matplotlib.pyplot as plt
import numpy as np
from random import random

Point = TypeVar('Point', bound=DataPoint)


def zscores(original: Sequence[float]) -> List[float]:
    avg: float = mean(original)
    std: float = pstdev(original)
    if std == 0:            # if there are not changes, then return all 0
        return [0] * len(original)
    return [(x - avg) / std for x in original]

class KMeans(Generic[Point]):
    
    @dataclass
    class Cluster:
        points: List[Point]
        centroid: DataPoint
       
        
    def __init__(self, k: int, points: List[Point]) -> None:
        if k < 1:                       # number of clusters, creating via k-means method, 
                                        # number can't be negative or = 0
            raise ValueError('k must be >= 1')
        self._points: List[Point] = points
        self._zscore_normalize()
        # initialize empty clusters with randomly cetroids
        self._clusters: List[KMeans.Cluster] = []
        for _ in range(k):
            rand_point: DataPoint = self._random_point()
            cluster: KMeans.Cluster = KMeans.Cluster([], rand_point)
            self._clusters.append(cluster)
      
    @property
    def _centroids(self) -> List[DataPoint]:
        return [x.centroid for x in self._clusters]
    
    def _dimension_slice(self, dimension: int) -> List[float]:
        return [x.dimensions[dimension] for x in self._points]
    
    def _zscore_normalize(self) -> None:
        zscored: List[List[float]] = [[] for _ in range(len(self._points))]
        for dimension in range(self._points[0].num_dimensions):
            dimension_slice: List[float] = self._dimension_slice(dimension)
            for index, zscore in enumerate(zscores(dimension_slice)):
                zscored[index].append(zscore)
        for i in range(len(self._points)):
            self._points[i].dimensions = tuple(zscored[i])
            
    def _random_point(self) -> DataPoint:
        rand_dimensions: List[float] = []
        for dimension in range(self._points[0].num_dimensions):
            values: List[float] = self._dimension_slice(dimension)
            rand_value: float = uniform(min(values), max(values))
            rand_dimensions.append(rand_value)
        return DataPoint(rand_dimensions)
    
    # Find the closest centroid of the cluster for each unit of data and
    # assign unit of data to this cluster
    def _assign_clusters(self) -> None:
        for point in self._points:
            closest: DataPoint = min(self._centroids, key=partial(DataPoint.distance, point))
            idx: int = self._centroids.index(closest)
            cluster: KMeans.Cluster = self._clusters[idx]
            cluster.points.append(point)
            
    # Find the center of each clusters and move the centroid there
    def _generate_centroids(self) -> None:
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                # leave the same centroid if there are not points
                continue
            means: List[float] = []
            for dimension in range(cluster.points[0].num_dimensions):
                print('!!!!', dimension,  cluster.centroid, cluster.points[0])
                dimension_slice: List[float] = [p.dimensions[dimension] for p in cluster.points]
                means.append(mean(dimension_slice))
            print('mean   --',means)
            cluster.centroid = DataPoint(means)
            


    def _generate_centroids_kplus(self) -> None:
        for cluster in self._clusters:
            if len(cluster.points) == 0:
                continue    
            new_centroid = distance_2(cluster, cluster.points)
            cluster.centroid = new_centroid
                     
    def run(self, max_iterations: int = 100) -> List[KMeans.Cluster]:
        for iteration in range(max_iterations):         
            for cluster in self._clusters:                  # to clear all clusters
                cluster.points.clear()
            self._assign_clusters()
            # find the cluster, to which current the unit of data is closest
            old_centroids: List[DataPoint] = deepcopy(self._centroids)
            # write

            self._generate_centroids_kplus()                # find new centroids
  
            if old_centroids == self._centroids:            # have the centroid shifted?
                print(f'Converged after {iteration} iterations')
                return self._clusters
        return self._clusters



# for k-means ++
def distance_2(cluster: KMeans.Cluster, other: List[DataPoint]) -> DataPoint:
    for point in other:
        combined: Iterator[Tuple[float, float]] = zip(cluster.centroid.dimensions, point.dimensions)
        differences: List[float] = [(x - y) ** 2 for x, y in combined]
        sum_dif = sum(differences)
        rnd = random() * sum_dif
        index = 0
        for x, y in combined:
            differences.append(((x - y) ** 2))
            sum_dif = sum(differences)
            if sum_dif > rnd:
                break 
            index += 1
        return other[index]
    

# work with CSV-files
def import_csv(file):
    data_list = []
    data = pandas.read_csv(file)
    dict_data = data.to_dict()
    for index, key in enumerate(dict_data.keys()):
        data_list.append([])
        for value in dict_data[key].values():
            data_list[index].append(value)
    print(data_list)


# visual display of k-means algorithm with matplotlib and numpy from CSV-file(results of k-means)

def viz2():
    data = np.recfromcsv('file_new.csv', encoding=None, names=('time', 'packets', 'interface'))
    colors = 'blue', 'orange'
    ifaces = np.unique(data.interface)  # set of interfaces

    assert len(colors) == ifaces.size

    for color, iface in zip(colors, ifaces):
        # getting data related with the current interface
        items = data[data.interface == iface]
        plt.scatter(items.time, items.packets, marker='o', label=iface, color=color)

    plt.xlabel('Packets')
    plt.ylabel('Time')
    plt.title('TEST')
    plt.legend()
    plt.show()  



# manual input of starting centroids
""" def __init__(self, k: int, points: List[Point], clusters: List[List[float]]) -> None:
        if k < 1:                       # number of clusters, creating via k-means method, 
                                        # number can't be negative or = 0
            raise ValueError('k must be >= 1')
        self._points: List[Point] = points
        self._zscore_normalize()
        # initialize empty clusters with randomly cetroids
        self._clusters: List[KMeans.Cluster] = []
        for position in clusters:
            cluster: KMeans.Cluster = KMeans.Cluster([], position)
            self._clusters.append(cluster)
     """

if __name__ == '__main__':
    point1: DataPoint = DataPoint([2.0, 1.0, 1.0])
    point2: DataPoint = DataPoint([2.0, 2.0, 5.0])
    point3: DataPoint = DataPoint([3.0, 1.5, 2.5])
    kmeans_test: KMeans[DataPoint] = KMeans(2, [point1, point2, point3])
    test_clusters: List[KMeans.Cluster] = kmeans_test.run()
    for index, cluster in enumerate(test_clusters):
        print(f'Cluster {index}: {cluster.points}')
        
        