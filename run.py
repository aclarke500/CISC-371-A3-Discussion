import math
import random

def main():
  for i in range(2, 100):
    tangent = run_test(i, 100, step=0.00001)[1]
    magnitude = get_magnitude(tangent)
    print(f"In {i} dimensions the magnitude of the tangents in the unit directions are {magnitude}")

# function to be minimized
def objective_function(point, points):
  score = 0
  for p in points:
    score+= get_dist(point, p)
  return score/len(points)

# HELPER FUNCTIONS
def generate_random_points(n, dim):
  points = []
  for i in range(n):
    point = []
    for j in range(dim):
      point.append(random.randint(-100, 100))
    points.append(point)
  return points


def run_test(dimensions, number_points, step=0.01):
  points = generate_random_points(number_points, dimensions)
  est = get_avg_vector(points)
  tans = get_tangents(est, points, step=step)
  return est, tans



# get tangent in all unit directions
def get_tangents(point, points, step=0.01):
  tangents=[]
  for i in range(len(point)):
    # for each dimension in the point, create a tangent vector
    point_i = []
    # dynamically copy points over
    for dimension in point:
      point_i.append(dimension)
    point_i[i] += step # take small step in ith dimension

    tangents.append((objective_function(point_i, points) - objective_function(point, points)) / step)
  
  
  return tangents

# VECTOR RELATED FUNCTIONS
def get_dist(p1, p2):
  norm = subtract_vectors(p1, p2)
  if not norm:
    return None
  return get_magnitude(norm)

def get_avg_vector(points):
  sum = [0] * len(points[0])
  for p in points:
    for i in range(len(p)):
      sum[i] += p[i]
  
  avg = []
  for i in range(len(sum)):
    avg.append(sum[i] / len(points))
  
  return avg

def get_magnitude(vector):
  sum = 0
  for v in vector:
    sum += v**2
  
  return math.sqrt(sum)

def subtract_vectors(v1, v2):
  if len(v1) != len(v2):
    print("Error, vectors not same length")
    return None
  result = []
  for i in range(len(v1)):
    result.append(v1[i] - v2[i])
  
  return result



main()

