import plotly.express as px
def maximal_points_left_to_right(points):
    points.sort(key=lambda x: x[0])
    comparisons = 0
    maximal_points = [points[0]]
    for i in range(1, len(points)):
        comparisons += 1
        if points[i][1] > maximal_points[-1][1]:
            maximal_points.append(points[i])

    return maximal_points, comparisons



def maximal_points_right_to_left(points):
    points.sort(key=lambda x: x[0])
    maximal_points = [points[0]]
    comparisons = 0
    for i in range(1, len(points)):
        if points[i][1] > maximal_points[-1][1]:
            maximal_points.append(points[i])
        comparisons += 1

    return maximal_points, comparisons



def main():
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

  # Separate x and y coordinates
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]

  # Create a scatter plot
    fig = px.scatter(x=x_values, y=y_values, labels={'x': 'X-axis', 'y': 'Y-axis'}, title='Plotting all the Points')

  # Show the plot
    fig.show()


Input_list = [(1, 16), (3, 8), (5, 12), (7, 18), (8, 19), (9, 20), (11, 14), (13, 10), (15, 2), (17, 6), (19, 4), (90, 1)]

points = Input_list
if __name__ == "__main__":
    main()
