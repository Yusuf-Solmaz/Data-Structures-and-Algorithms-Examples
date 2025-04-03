package problems_solutions.kotlin

/**
 * Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place such that each unique element appears only once. The relative order of the elements should be kept the same. Then return the number of unique elements in nums.
 *
 * Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:
 *
 * Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially. The remaining elements of nums are not important as well as the size of nums.
 * Return k.
 *
 * Example:
 *
 * Input: nums = [1,1,2]
 * Output: 2, nums = [1,2,_]
 * Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
 * It does not matter what you leave beyond the returned k (hence they are underscores).
 * */

fun removeDuplicates(nums: MutableList<Int>): Int {
    var index = 0

    while (index < nums.size - 1) {
        if (nums[index] == nums[index + 1]) {
            nums.removeAt(index)
        } else {
            index++
        }
    }
    return nums.size
}


fun main(){

    val nums = mutableListOf(1,1,2)
    println(removeDuplicates(nums))

}