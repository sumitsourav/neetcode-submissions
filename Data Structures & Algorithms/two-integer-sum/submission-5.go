func twoSum(nums []int, target int) []int {
    lookup := make(map[int]int)

    for i, num := range nums {
        complement := target - num
        idx, exists := lookup[complement]
        if exists {
            return []int{idx,i}
        }
        lookup[num] = i
    }
    return nil
}
