# Link: https://leetcode.com/problems/group-the-people-given-the-group-size-they-belong-to/
# Date: 11-09-2023
# Brief: n people (0 -> n-1) need split into some groups
# Input: GroupSizes where groupSizes[i] is the size of the group that person i is in
# Output: list groups that person is in
# Constraints:
# groupSizes.length == n
# 1 <= n <= 500
# 1 <= groupSizes[i] <= n
# Example:
# Input: groupSizes = [3,3,3,3,3,1,3]
# Output: [[5],[0,1,2],[3,4,6]]

from typing import List


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        list_group_has_same_size = {}
        output = []
        for index_ in range(len(groupSizes)):
            list_group_has_same_size.setdefault(groupSizes[index_], []).append(index_)
            if len(list_group_has_same_size.get(groupSizes[index_])) == groupSizes[index_]:
                output.append(list_group_has_same_size.get(groupSizes[index_]))
                del list_group_has_same_size[groupSizes[index_]]
        return output


if __name__ == '__main__':
    intput = Solution()
    print(intput.groupThePeople(groupSizes=[2, 1, 3, 3, 3, 2]))
