import typing


def twoSum(nums: typing.List[int], target: int)-> typing.List[int]:
    """
    Problem - Given an array of integers and a target value, return the indices
    of the two numbers who sum to the target.  Assume exactly one solution.

    Solution - The basic idea is that we want to subtract the current value from the array
    and check if the complement (target minus current number) exist within the array.  The simplest
    way to do this is to store the values of the array and the index in a hash table and look them up.

    In essence, we find the complement, check the hash table for the balue.  If the value is in the hash table
    then return the index of the complemnt in the hash table along with the current index.

    If not then add the current value to the hash table and record the index.
    """
    hastable = dict()
    for i in range(len(nums)):
        complement = target - nums[i]
        if complement in hastable:
            return [hastable[complement], i]
        hastable[nums[i]] = i



