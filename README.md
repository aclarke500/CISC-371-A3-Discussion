# CISC-371-A3-Discussion
<h3>The average vector as a local minimum of the distance problem</h3>
<p>This script runs tests that illistrates the average vector for a set of points is a local minimum. The consequences are that this provides a terrible initial estimate for descent based algoriths.</p>

<h2>Methodology</h2>
<p> This script creates 100 points in an arbitrary number of dimensions, and computes the average vector. The average vector is the vector whose component in direction i is is the average value of every vector in the sets value of that component. A function is used to evaluate the distances from that vector and the other vectors in the set. From there, the tangent with respect to every unit direction was calculated. </p>

<h2>Results</h2>
<p> The average vector is a local minimum for any number of dimensions and any number of points, whether positive or negaitve. The results are stored in the results.txt if you do not wish to run this script on your machine.</p>

<h2>Usage:</h2>
<code>python3 run.py</code>