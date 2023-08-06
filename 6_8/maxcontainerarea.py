# def maxArea(height) -> int:
        
#         l = 0
#         r = len(height) -1
#         areas = []
#         while l<r:
#             area = 0
#             if height[l] > height[r]:
#                 print(f"{height[r]} * {(r-l)} = {height[r] * (r-l)}")
#                 area = height[r] * (r-l)
#                 r-=1
#             elif height[l] < height[r]:
#                 area = height[l] * (r-l)
#                 l+=1
#             else:
#                 area = height[l] * (r-l)
#                 r-=1
#             areas.append(area)
#         return max(areas)

# print(maxArea([1,1])
# )
def maxArea(height) -> int:
    l = 0
    r = len(height) -1
    areas = []
    while l<r:
        area = 0
        area = height[r] * (r-l)

        if height[l] < height[r]:
            r-=1
        else:
            l+=1

        areas.append(area)
    print(areas)
    return max(areas)

result = maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7])
print(result)  # Output: 49
