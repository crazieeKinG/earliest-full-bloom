from typing import List


class Solution:
    def earliestFullBloom(self, plantTime: List[int], growTime: List[int]) -> int:
        # Maintain sorted array based on plant time
        data = []

        # Count blooming days
        plant_days = 0
        bloom_days = 0

        length = len(plantTime)

        # Create tuple array for associated plant and grow time
        for i in range(length):
            data.append((plantTime[i], growTime[i]))

        # Arrange in descending order based on grow time
        data = sorted(data, key=lambda x: -x[1])

        # Calculate maximun grow time with total plant_days
        for i in range(length):
            plant, grow = data[i]

            plant_days += plant
            bloom_days = max(plant_days + grow, bloom_days)

        return bloom_days
