import math
import random

# function to be minimized
def objective_function(point, points):
  score = 0
  for p in points:
    score+= get_dist(point, p)
  return score/len(points)


def get_avg_dist(point, points):
  sum = 0
  for p in points:
    sum += get_dist(point, p)

  return sum / len(points)

def get_dist(p1, p2):
  if len(p1) == 2 and len(p2) == 2:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)
  elif len(p1) == 3 and len(p2) == 3:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2)
  elif len(p1) == 4 and len(p2) == 4:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2 + (p1[3] - p2[3])**2)
  elif len(p1) == 5 and len(p2) == 5:
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2 + (p1[2] - p2[2])**2 + (p1[3] - p2[3])**2 + (p1[4] - p2[4])**2)
  else:
    print("Error, point dimensions not supported")
    return None
  
def generate_random_points(n, dim):
  points = []
  for i in range(n):
    point = []
    for j in range(dim):
      point.append(random.randint(0, 10))
    points.append(point)
  return points

def get_avg_vector(points):
  sum = [0] * len(points[0])
  for p in points:
    for i in range(len(p)):
      sum[i] += p[i]
  
  avg = []
  for i in range(len(sum)):
    avg.append(sum[i] / len(points))
  
  return avg

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

def run_test(dimensions, number_points, step=0.01):
  points = generate_random_points(number_points, dimensions)
  est = get_avg_vector(points)
  tans = get_tangents(est, points, step=step)
  return est, tans

def get_magnitude(vector):
  sum = 0
  for v in vector:
    sum += v**2
  
  return math.sqrt(sum)


for i in range(2, 6):
  tangent = run_test(i, 500, step=0.00001)[1]
  magnitude = get_magnitude(tangent)
  print(f"In {i} dimensions the magnitude of the tangents in the unit direction is {magnitude}")

