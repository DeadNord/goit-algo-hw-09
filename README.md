Amount: 113, Greedy Result: {50: 2, 10: 1, 2: 1, 1: 1}, Dynamic Result: {50: 2, 10: 1, 2: 1, 1: 1}
+----------+-----------------------------+------------------------------+
| Amount | Greedy Algorithm Time (s) | Dynamic Algorithm Time (s) |
+==========+=============================+==============================+
| 113 | 5.00679e-06 | 0.000103712 |
+----------+-----------------------------+------------------------------+
![Alt text](image.png)

Amount: 87, Greedy Result: {50: 1, 25: 1, 10: 1, 2: 1}, Dynamic Result: {50: 1, 25: 1, 10: 1, 2: 1}
Amount: 143, Greedy Result: {50: 2, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1}, Dynamic Result: {50: 2, 25: 1, 10: 1, 5: 1, 2: 1, 1: 1}
Amount: 289, Greedy Result: {50: 5, 25: 1, 10: 1, 2: 2}, Dynamic Result: {50: 5, 25: 1, 10: 1, 2: 2}
Amount: 498, Greedy Result: {50: 9, 25: 1, 10: 2, 2: 1, 1: 1}, Dynamic Result: {50: 9, 25: 1, 10: 2, 2: 1, 1: 1}
Amount: 1023, Greedy Result: {50: 20, 10: 2, 2: 1, 1: 1}, Dynamic Result: {50: 20, 10: 2, 2: 1, 1: 1}
Amount: 3764, Greedy Result: {50: 75, 10: 1, 2: 2}, Dynamic Result: {50: 75, 10: 1, 2: 2}
+----------+-----------------------------+------------------------------+
| Amount | Greedy Algorithm Time (s) | Dynamic Algorithm Time (s) |
+==========+=============================+==============================+
| 87 | 1.85966e-05 | 0.000177622 |
+----------+-----------------------------+------------------------------+
| 143 | 9.77516e-06 | 0.000303268 |
+----------+-----------------------------+------------------------------+
| 289 | 5.48363e-06 | 0.00058198 |
+----------+-----------------------------+------------------------------+
| 498 | 7.86781e-06 | 0.00105095 |
+----------+-----------------------------+------------------------------+
| 1023 | 1.12057e-05 | 0.00180268 |
+----------+-----------------------------+------------------------------+
| 3764 | 4.52995e-06 | 0.00714874 |
+----------+-----------------------------+------------------------------+
![Alt text](image-1.png)

As can be seen, the execution time of the greedy algorithm is significantly lower compared to the dynamic programming algorithm, especially when the sum is increased. This shows that the greedy algorithm is more efficient in execution time, especially for large sums.
A graph illustrating the execution time of both algorithms is also provided. The graph clearly shows that as the amount increases, the execution time of the dynamic programming algorithm increases significantly, while the execution time of the greedy algorithm remains almost unchanged.
