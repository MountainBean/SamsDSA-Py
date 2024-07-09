class MaxHeap:
    """
    O(log n)
    Python implementation of a heap with the max value always at the root. Very similar to a 
    binary search tree. It is a binary tree but the values aren't arranged in the same
    manner. The highest values go at the root of the tree and remove() only ever takes the 
    root value.
    """

    def __init__(self) -> None:
        self.heap = []

    def __str__(self) -> str:
        return str(self.heap)

    def _left_child(self, index):
        return 2 * index + 1

    def _right_child(self, index):
        return 2 * index + 2

    def _parent(self, index):
        return (index - 1) // 2

    def _swap(self, index1, index2):
        self.heap[index1], self.heap[index2] = self.heap[index2], self.heap[index1]

    def insert(self, value):
        """
        appends value to the bottom of the heap, then bubbles that value up to its appropriate level in
        the heap.

        Args:
            value (_type_): _description_
        """
        self.heap.append(value)
        current = len(self.heap) - 1
        while current > 0 and self.heap[current] > self.heap[self._parent(current)]:
            self._swap(current, self._parent(current))
            current = self._parent(current)

    def remove(self):
        """
        O(log n)
        Removes the value at the root of the heap (the highest value).

        Returns:
            _type_: the removed root value
        """
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self._sink_down(0)
        return max_value

    def _sink_down(self, index):
        max_index = index
        while True:
            left_index = self._left_child(index)
            right_index = self._right_child(index)
            if left_index < len(self.heap) and self.heap[left_index] > self.heap[max_index]:
                max_index = left_index
            if right_index < len(self.heap) and self.heap[right_index] > self.heap[max_index]:
                max_index = right_index
            if max_index != index:
                self._swap(index, max_index)
                index = max_index
            else:
                return


def find_kth_smallest(nums: list[int], k: int) -> int:
    """
    O(len(nums))
    Finds the kth lowest value in the nums list.
    Iterates through the list, adding each item to a MaxHeap and trimming the MaxHeap if there
    are more than k items (every item greater than the kth smallest)

    Args:
        nums (list[int]): _description_
        k (int): _description_

    Returns:
        int: _description_
    """
    max_heap = MaxHeap()

    for num in nums:
        max_heap.insert(num)
        if len(max_heap.heap) > k:
            max_heap.remove()

    return max_heap.remove()
