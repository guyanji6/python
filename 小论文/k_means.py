import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def k_means(percetion) :
    s = KMeans(n_clusters=2,max_iter=500).fit(percetion)
    # print(s.cluster_centers_)
    return s.cluster_centers_

    # print(s)
