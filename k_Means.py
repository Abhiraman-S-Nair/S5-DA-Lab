import math

def euclidean_distance(point1, point2):
  return math.sqrt(sum((a-b)**2 for a, b in zip(point1, point2)))

def k_means_clustering(data, k, max_iterations = 100):
  centroids = data[ : k]
  for _ in range(max_iterations):
    labels = [min(range, key = lambda i : euclidean_distance(point, centroids[i]) for point in data)]
    new_centroids = [[sum(data[j][dim] for j in range(len(data)) if labels[j] == i) / labels.count(i) for dim in range(len(data[0]))]for i in range(k)]

  if new_centroids == centroids:
    break
  centroids = new_centroids
  return labels, centroids

num_points = int(input("Enter the no of data points : "))
data = [list(map(float, input(f"Enter the coordinates for point {i+1} : ").split())) for i in range (num_points)]
k = int(input("Enter the no of clusters required : "))
labels, centroids = k_means_clustering(data, k)
print("Final Clusters\n")
for i in range(k):
  cluster_points = [data[j] for j in range(len(data)) if labels[j] == i]
  print(f"Cluster {i + 1} : {cluster_points}")
print(f"Final Centroids {centroids}")




























































