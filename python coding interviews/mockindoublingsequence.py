# For this mock interview, you will go through four phases: Prompt, Plan, Code, & Test.

# Prompt: Understand the problem.

# Plan: Outline your approach.

# Code: Implement your solution.

# Test: Verify your solution works.

# Here is the problem that you will be solving:

# In this task, you are required to generate a new array that is twice the length of an initial integer array 'nums' with a length of 'n'.

# The new array, dubbed 'ans', should be constructed such that the first half of 'ans' directly replicates the 'nums' array, and the second half is a repetition of the first, thereby doubling the sequence.

# Essentially, for each element with index 'i' in 'nums', 'ans[i] = nums[i]' and 'ans[i + n] = nums[i]', with 'i' ranging from 0 to 'n-1'.

# Your objective is to return the array 'ans' thus obtained.

# Example 1:

# Input: nums = [1,2,1]

# Output: [1,2,1,1,2,1]

# Explanation: The resulting 'ans' array combines 'nums' with itself, yielding [1,2,1,1,2,1].

# Example 2:

# Input: nums = [1,3,2,1]

# Output: [1,3,2,1,1,3,2,1]

# Explanation: Similarly, the 'ans' array is formed by concatenating 'nums' with itself, resulting in [1,3,2,1,1,3,2,1].

# Constraints:

# - The length of 'nums' ('n') is guaranteed to be between 1 and 1000, inclusive.

# - Each element in 'nums' can be any integer between 1 and 1000, inclusive.

#defgenerateDoubleSequence(nums):

    
# Write your plan below

    
#

    
# make arr2 the output list

    
# a = len(nums)*2

    
# arr2 = [].append(a)

    
# append nums to arr2 twice by adding 

    
# for i < len(nums)

    
# arr2[i] = nums[i] 

    
# arr2[len(nums)+i] = nums[i]

    
# 

    
# 

    
# 

    
# Write your code below

# In this task, you are required to generate a new array that is twice the length of an initial integer array 'nums' with a length of 'n'.

# The new array, dubbed 'ans', should be constructed such that the first half of 'ans' directly replicates the 'nums' array, and the second half is a repetition of the first, thereby doubling the sequence.

# Essentially, for each element with index 'i' in 'nums', 'ans[i] = nums[i]' and 'ans[i + n] = nums[i]', with 'i' ranging from 0 to 'n-1'.

# Your objective is to return the array 'ans' thus obtained.

# Example 1:

# Input: nums = [1,2,1]

# Output: [1,2,1,1,2,1]

# Explanation: The resulting 'ans' array combines 'nums' with itself, yielding [1,2,1,1,2,1].

# Example 2:

# Input: nums = [1,3,2,1]

# Output: [1,3,2,1,1,3,2,1]

# Explanation: Similarly, the 'ans' array is formed by concatenating 'nums' with itself, resulting in [1,3,2,1,1,3,2,1].

# Constraints:

# - The length of 'nums' ('n') is guaranteed to be between 1 and 1000, inclusive.

# - Each element in 'nums' can be any integer between 1 and 1000, inclusive.
nums = [1,3,2,1]
def generateDoubleSequence(nums):
   
# Initialize an empty list of size 2 * length of nums 
    ans = [0]*(2*len(nums))

    
# Fill the first half of ans with the elements of nums

    for i in range(len(nums)):
        ans[i]= nums[i]    
# Fill the second half of ans with the same elements
        ans[i+len(nums)]= nums[i]

    
# Return the concatenated list
    return ans