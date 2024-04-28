/*
Problem: Median of Two Sorted Arrays
Source: https://leetcode.com/problems/median-of-two-sorted-arrays/
Author: Osama Abdul Ghafoor
GitHub: https://github.com/Osama-Abdul-Ghafoor
*/

public class Solution
{
    public double FindMedianSortedArrays(int[] nums1, int[] nums2)
    {
        decimal median = 0;
        int num1Value, num2Value;
        int countArray01 = nums1.Count();
        int countArray02 = nums2.Count();
        int numberOfTimesArrayToIterate = countArray01 + countArray02;
        int[] resultArray = new int[countArray01 + countArray02];
        int resultIterator = 0, iteratorArray01 = 0, iteratorArray02 = 0;

        while (numberOfTimesArrayToIterate != 0)
        {
            int value;

            num1Value = iteratorArray01 < countArray01 ? nums1[iteratorArray01] : int.MaxValue;
            num2Value = iteratorArray02 < countArray02 ? nums2[iteratorArray02] : int.MaxValue;

            if (num1Value > num2Value)
            {
                value = num2Value;
                iteratorArray02++;
            }
            else
            {
                value = num1Value;
                iteratorArray01++;
            }
            resultArray[resultIterator++] = value;
            numberOfTimesArrayToIterate--;
        }

        if (resultIterator % 2 != 0)
        {
            int mid = (resultIterator - 1) / 2;
            median = resultArray[mid];
        }
        else
        {
            int mid = resultIterator / 2;
            median = (resultArray[mid - 1] + resultArray[mid]) / 2m;
        }
        return decimal.ToDouble(median);
    }
}