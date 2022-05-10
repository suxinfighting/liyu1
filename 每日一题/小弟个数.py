'''

 给定一个数字列表，请编写一个函数，找出其中每个索引位置上的数字的右侧存在多少个比它小的数字，返回个数组成的列表。

【示例】
输入：[1, 2, 0]
输出：[1, 1, 0]
解释：索引0对应数字1，右边是2和0，只有0比它小，所以个数是1。以此类推，结果得到[1, 1, 0]

题目难度：简单
题目来源：CodeWars-How many are smaller than me? 1
'''


def solution(list_a):
    list_b = list()
    for i in range(len(list_a)):
        temp = 0
        for j in range(i + 1, len(list_a)):
            if list_a[i] > list_a[j]:
                temp += 1
        list_b.append(temp)

    return list_b


def test_solution():
    assert solution([1, 2, 0]) == [1, 1, 0]
    assert solution([1, 2, 3]) == [0, 0, 0]
    assert solution([5, 4, 7, 9, 2, 4, 4, 5, 6]) == [4, 1, 5, 5, 0, 0, 0, 0, 0]

# if __name__ == '__main__':
#     print(solution([5, 4, 7, 9, 2, 4, 4, 5, 6]))

'''
知识点提取

'''