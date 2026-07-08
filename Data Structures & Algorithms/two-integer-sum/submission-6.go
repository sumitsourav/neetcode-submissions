func twoSum(nums []int, target int) []int {
    lookup := make(map[int]int)
    for i, num := range nums {
        complement := target - num
        if idx, ok := lookup[complement]; ok {
            return []int{idx, i}
        }
        lookup[num] = i
    }
    return nil
}
