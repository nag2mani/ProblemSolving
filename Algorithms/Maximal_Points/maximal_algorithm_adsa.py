def maximal_points_left_to_right(points):
    points.sort(key=lambda point: (-point[0], -point[1]))
    comparisons = 0
    maximal_points = [points[0]]
    for i in range(1, len(points)):
        comparisons += 1
        if points[i][1] > maximal_points[-1][1]:
            maximal_points.append(points[i])

    return maximal_points, comparisons



def maximal_points_right_to_left(points):
    points.sort(key=lambda point: (-point[0], -point[1]))
    maximal_points = [points[0]]
    comparisons = 0
    for i in range(1, len(points)):
        if points[i][1] > maximal_points[-1][1]:
            maximal_points.append(points[i])
        comparisons += 1

    return maximal_points, comparisons



def main():
#     # Read input
#     n = int(input("Enter the number of points: "))
#     points = []

#     for i in range(n):
#         x, y = map(int, input(f"Enter coordinates for point {i+1} (x y): ").split())
#         points.append((x, y))

    # Left to Right variant
    maximal_points_lr, comparisons_lr = maximal_points_left_to_right(points)
    print("\nLeft to Right Variant:")
    print("Input Points:", points)
    print("Maximal Points:", maximal_points_lr)
    print("Number of Comparisons:", comparisons_lr)

    # Right to Left variant
    maximal_points_rl, comparisons_rl = maximal_points_right_to_left(points)
    print("\nRight to Left Variant:")
    print("Input Points:", points)
    print("Maximal Points:", maximal_points_rl)
    print("Number of Comparisons:", comparisons_rl)


Input_list = [
    [1, 2], [3, 4], [5, 6], [7, 8], [9, 10],
    [11, 12], [13, 14], [15, 16], [17, 18], [19, 20],
    [21, 22], [23, 24], [25, 26], [27, 28], [29, 30],
    [31, 32], [33, 34], [35, 36], [37, 38], [39, 40],
    [41, 42], [43, 44]
]

points = Input_list
if __name__ == "__main__":
    main()