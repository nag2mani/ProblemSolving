def maximal_points_left_to_right(points):
	lst = points
	comparison = 0
	lst = sorted(lst, key=lambda x: x[0])
	maximal_Point = [lst[0]]
	for point in lst:
		comparison += 1
		if maximal_Point[-1][1] > point[1]:
			maximal_Point.append(point)
		else:
			maximal_Point.append(point)
			for i in range(len(maximal_Point)-2,-1, -1):
				comparison += 1
				if maximal_Point[i][1] <= point[1]:
					maximal_Point.remove(maximal_Point[i])
	return maximal_Point, comparison



def maximal_points_right_to_left(points):
    data = points
    sorted_points = sorted(data, key=lambda point: point[0], reverse=True)
    n = len(sorted_points)
    result = [sorted_points[0]]
    comparison = 0
    i = 1
    while i < n:
        comparison += 1
        # Extract the x and y coordinates of the current point
        x, y = sorted_points[i]

        # Check if the y-coordinate of the current point is greater than the last point in the result
        if y > result[-1][1]:
            # If true, add the current point to the result list
            result.append((x, y))
        i += 1
    print("The Number of comparison is: ", comparison)
    return result




def main():
    # Left to Right variant
    maximal_points_lr, comparisons_lr = maximal_points_left_to_right(points)
    print("\nLeft to Right Variant:")
    print("Input Points:", points)
    print("Number of Comparisons:", comparisons_lr)
    print("Maximal Points:", maximal_points_lr)

    # Right to Left variant
    print("\nRight to Left Variant:")
    print("Input Points:", points)
    maximal_points_rl = maximal_points_right_to_left(points)
    print("Maximal Points:", maximal_points_rl[::-1])

    # Plotting x and y coordinates for maximal Points.
    import matplotlib.pyplot as plt

    # Your existing code to create the scatter plot
    x_values = [point[0] for point in maximal_points_lr]
    y_values = [point[1] for point in maximal_points_lr]
    plt.scatter(x_values, y_values, color='red',label='maximal Points')
    plt.xlabel('X-axis')
    plt.ylabel('Y-axis')
    plt.title('Plotting all the maximal Points')

    # Add lines from each point to the x and y axes
    for x, y in zip(x_values, y_values):
        plt.plot([x, x], [0, y], 'r--', lw=0.5)  # Vertical line to x-axis
        plt.plot([0, x], [y, y], 'r--', lw=0.5)  # Horizontal line to y-axis

    x_values_additional = [point[0] for point in points]
    y_values_additional = [point[1] for point in points]
    plt.scatter(x_values_additional, y_values_additional, color='blue', label='Input Points')

    plt.legend()  # Show legend
    plt.show()

Input_list = [(1, 16), (3, 8), (5, 12), (7, 18), (8, 19), (9, 20), (11, 14), (13, 10), (15, 2), (17, 6), (19, 4), (90, 1)]

points = Input_list
if __name__ == "__main__":
    main()
