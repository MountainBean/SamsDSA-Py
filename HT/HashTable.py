class HashTable:
    """
    O(1)
    Simple HashTable class used to illustrate the concept of using a hash to allocate a value
    to a place in memory (data_map) with a key. 
    This uses lists to handle collisions but we could have also used linked lists. The idea 
    is that the Hash function would sufficiently distribute keys accross the data_map so as 
    to minimise collisions. In this way, set/get would both be O(1) as regardlyess of the items
    in the HashTable, the hash function will spit out the location of the requested key in 
    constant time. (The number of letters in the key will affect the hash function
    only. When considering the time pomplexity of the HashTable with n as the size of the
    table, the number of operations used by the hash function to process the key is irrelevant)
    """

    def __init__(self, size=7) -> None:
        self.data_map = [None] * size

    def __hash(self, key) -> int:
        """
        Future me, don't get hung up on this. Hash functions just need to be one-way, and return 
        the same value for the key given, every time (deterministic)

        Args:
            key (_type_): _description_

        Returns:
            int: _description_
        """
        my_hash = 0
        for letter in key:
            my_hash = (my_hash + ord(letter) * 23) % len(self.data_map)
        return my_hash

    def print_table(self) -> None:
        for i, val in enumerate(self.data_map):
            print(i, ": ", val)

    def set_item(self, key, value) -> None:
        index = self.__hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key, value])

    def get_item(self, key):
        index = self.__hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None

    def keys(self):
        all_keys = []
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys


def item_in_common(list1: list, list2: list) -> bool:
    """
    O(n)
    Uses the native Python dict (HashTable) to check two lists for a common item
    popuates a dict with the items of list1 as keys and their values all True.
    Then uses the python 'in' operator to see if the items in list2 are keys in
    the dict. This does NOT iterate through the list1 for every item in list2. 
    Instead, it will hash each item in list 2 and see if the resulting address is 
    already populated in the dict.

    Args:
        list1 (list): A list
        list2 (list): Another list

    Returns:
        bool: True if there is a common item in the list
    """
    mydict = {}
    for i in list1:
        mydict[i] = True

    for j in list2:
        if j in mydict:
            return True
    return False


def find_duplicates(nums: list[int]) -> list[int]:
    """
    O(n)
    Very similar to the above function. Uses Python's native dict to record items
    in a given list as keys in a HashTable.
    If it encounters an item that is already in the hashtable, it appends the item
    to an output list and continues.

    Args:
        nums (list[int]): a list of ints

    Returns:
        list[int]: a list of ints that were duplicated in the input list. Empty list
        if no duplicates.
    """
    mydict = {}
    dupes = []
    for i in nums:
        if i in mydict:
            dupes.append(i)
        else:
            mydict[i] = True
    return dupes


def first_non_repeating_char(string):
    char_counts = {}
    for char in string:
        char_counts[char] = char_counts.get(char, 0) + 1
    for char in string:
        if char_counts[char] == 1:
            return char
    return None


def group_anagrams_sum_ord(strings: list[str]):
    """
    My answer. I use the sum of the ord values of the strings as the key in a dict
    instead of sorting the strings into their "canonical" form.
    This has time complexity of O(n * k) where n is the length of  the list and k 
    is the length of the longest string as we have to perform ord(char) for every
    char in a string.

    Args:
        strings (list[str]): _description_

    Returns:
        _type_: _description_
    """
    val_dict = {}
    out_list = []
    for string in strings:
        ord_val = sum(ord(char) for char in string)
        if ord_val in val_dict:
            val_dict[ord_val].append(string)
        else:
            val_dict[ord_val] = [string]
    for key in val_dict.keys():
        out_list.append(val_dict[key])
    return out_list


def group_anagrams(strings):
    """
    Uses the sorted ("canonical") form of the given strings to compare and determine
    if repeated in a dict.

    "It has a time complexity of O(n * k log k), where n is the length of the input 
    array and k is the maximum length of a string in the input array.  The time 
    complexity comes from sorting each string in the array, which takes O(k log k) time, 
    and the loop that goes through each string in the array, which takes O(n) time."

    Args:
        strings (_type_): _description_

    Returns:
        _type_: _description_
    """
    anagram_groups = {}
    for string in strings:
        canonical = ''.join(sorted(string))
        if canonical in anagram_groups:
            anagram_groups[canonical].append(string)
        else:
            anagram_groups[canonical] = [string]
    return list(anagram_groups.values())


def two_sum(nums: list[int], target: int) -> list[int]:
    """
    O(n)
    Takes a list of integers and a number and returns the two integers in the list that
    add up to make the target number. 
    Iterates through the list only once.

    Args:
        nums (list[int]): list of ints
        target (int): target int that can be reached by summing two items in nums

    Returns:
        list[int]: two ints from nums that add up to make target
    """
    compliments = {}
    out = []
    for i, num in enumerate(nums):
        if num in compliments:
            out = [compliments[num], i]
        compliments[target - num] = i
    return out
