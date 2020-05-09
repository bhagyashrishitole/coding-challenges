"""
Problem Statement:
Check If It Is a Straight Line
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.





Example 1:



Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
Output: true
Example 2:



Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
Output: false


Constraints:

2 <= coordinates.length <= 1000
coordinates[i].length == 2
-10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
coordinates contains no duplicate point.
   Hide Hint #1
If there're only 2 points, return true.
   Hide Hint #2
Check if all other points lie on the line defined by the first 2 points.
   Hide Hint #3
Use cross product to check collinearity.
"""


class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        """Solution-1"""
        if len(coordinates) == 2:
            return True
        dx = coordinates[0][0] - coordinates[1][0]
        dy = coordinates[0][1] - coordinates[1][1]

        for i in range(0, len(coordinates)):
            if dx * (coordinates[1][1] - coordinates[i][1]) != dy * (coordinates[1][0] - coordinates[i][0]):
                return False
        return True

    """Solution-2"""
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     (x0, y0), (x1, y1) = coordinates[: 2]
    #     for x, y in coordinates:
    #         if (x1 - x0) * (y - y1) != (x - x1) * (y1 - y0):
    #             return False
    #     return True

    """Solution-3"""
    # def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
    #     (x0, y0), (x1, y1) = coordinates[: 2]
    #     return all((x1 - x0) * (y - y1) == (x - x1) * (y1 - y0) for x, y in coordinates)
