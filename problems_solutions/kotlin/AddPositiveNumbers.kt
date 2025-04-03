package problems_solutions.kotlin

/**
 * Given a list of integers. Write a function that returns the sum of all positive numbers in the list. If there are no positive numbers in the list, return 0.
 * */

fun addPositiveNumbers(nums: MutableList<Int>): Int {
    var index =0
    var result =0

    while (index < nums.size) {
        if (nums[index]>0){
             result += nums[index]
        }
        index++
    }
    return result
}

fun main(){
    val result = addPositiveNumbers(mutableListOf(1,-2,3,-4,5,7,-3))
    println(result)
}