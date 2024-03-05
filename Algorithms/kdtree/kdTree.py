import math

class KDNode:
    def __init__(self, props):
        self.left = None
        self.right = None
        self.num_dims = len(props)
        self.point = props

class KDTree:
    def __init__(self, num_dims):
        self.root = None
        self.num_dims = num_dims

    def add(self, point):
        if self.root is None:
            self.root = KDNode(point)
        else:
            self._add(self.root, point)

    def _add(self, root, point, depth=0):
        k = depth % self.num_dims
        if point[k] < root.point[k]:
            if root.left is None:
                root.left = KDNode(point)
            else:
                self._add(root.left, point, depth + 1)
        else:
            if root.right is None:
                root.right = KDNode(point)
            else:
                self._add(root.right, point, depth + 1)

    def nearest_neighbor(self, target):
        return self._nearest_neighbor(self.root, target, 0)

    def _nearest_neighbor(self, root, target, depth):
        if root is None:
            return None

        next_branch = None
        other_branch = None

        if target[depth % self.num_dims] < root.point[depth % self.num_dims]:
            next_branch = root.left
            other_branch = root.right
        else:
            next_branch = root.right
            other_branch = root.left

        temp = self._nearest_neighbor(next_branch, target, depth + 1)
        best = self._closest(temp, root, target)

        radius_squared = self._dist_squared(target, best.point)
        dist = target[depth % self.num_dims] - root.point[depth % self.num_dims]

        if radius_squared >= dist * dist:
            temp = self._nearest_neighbor(other_branch, target, depth + 1)
            best = self._closest(temp, best, target)

        return best

    def _closest(self, n0, n1, target):
        if n0 is None:
            return n1
        if n1 is None:
            return n0

        d1 = self._dist_squared(n0.point, target)
        d2 = self._dist_squared(n1.point, target)

        if d1 < d2:
            return n0
        else:
            return n1

    def _dist(self, p0, p1):
        return math.sqrt(self._dist_squared(p0, p1))

    def _dist_squared(self, p0, p1):
        total = 0
        num_dims = len(p0)

        for i in range(num_dims):
            diff = abs(p0[i] - p1[i])
            total += diff ** 2

        return total

    def __str__(self):
        return self._print_tree(self.root)

    def _print_tree(self, root):
        if root is None:
            return ""

        result = ""
        queue = [root]

        while queue:
            size = len(queue)
            for _ in range(size):
                node = queue.pop(0)
                if node is not None:
                    result += str(node.point) + ", "
                    queue.append(node.left)
                    queue.append(node.right)
                else:
                    result += "None, "
            result += "\n"

        return result

if __name__ == "__main__":
    ar = [
        [50, 50],
        [80, 40],
        [10, 60],
        [51, 38],
        [48, 38]
    ]

    tree = KDTree(2)

    for coord in ar:
        tree.add(coord)

    print("tree=", tree)
    print(tree.nearest_neighbor([40, 40]).point)
