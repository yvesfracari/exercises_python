# Maximum Subarray Sum

We define the following:

A subarray of array a of length n is a contiguous segment from a[i] through a[j] where i between 0 and n, j between i and n.
The sum of an array is the sum of its elements.
Given an n element array of integers, a, and an integer, m, determine the maximum value of the sum of any of its subarrays modulo m. For example, Assume a = [1, 2, 3]and m = 2. The following table lists all subarrays and their moduli:

		    sum	%2
[1]		    1	1
[2]		    2	0
[3]		    3	1
[1,2]		3	1
[2,3]		5	1
[1,2,3]		6	0
The maximum modulus is 1.

*Function Description*

Complete the maximumSum function in the editor below. It should return a long integer that represents the maximum value of subarray sum % m.

maximumSum has the following parameter(s):

a: an array of long integers, the array to analyze
m: a long integer, the modulo divisor

*Input Format*

The first line contains an integer q, the number of queries to perform.

The next q pairs of lines are as follows:

The first line contains two space-separated integers n and (long)m, the length of a and the modulo divisor.
The second line contains n space-separated long integers a[i].

*Constraints*

n between 2 and 10^5
m between 1 and 10^14
a[i] between 1 and 10^18
The sum of n over all test cases between 2 and 5 * 10^5 

*Output Format*

For each query, return the maximum value of subarray sum %m as a long integer.

*Sample Input*

1
5 7
3 3 9 9 5

*Sample Output*

6