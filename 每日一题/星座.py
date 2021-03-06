'''

:mage:‍ 给定一个包含3个数字的元组，依次代表年、月、日。请根据占星术清单，编写一个函数，按照输入日期判断它属于哪个星座。

水瓶座：1月21日至2月19日
双鱼座：2月20日至3月20日
白羊座：3月21日至4月20日
金牛座：4月21日至5月21日
双子座：5月22日至6月21日
巨蟹座：6月22日至7月22日
狮子座：7月23日至8月23日
处女座：8月24日至9月23日
天秤座：9月24日至10月23日
天蝎座：10月24日至11月22日
射手座：11月23日至12月21日
摩羯座：12月22日至1月20日
【示例】
输入：2000，2，15
输出：水瓶座
解释：2月15号处于1月21日～2月19日之间，所以是’水瓶座’

题目难度：简单
题目来源：CodeWars-It is written in the stars 4

'''




def solution(year: int, month: int, day: int)-> str:
    limits = [21, 20, 21, 21, 22, 22, 23, 24, 24, 24, 23, 22]
    signs = ["水瓶座", "双鱼座", "白羊座", "金牛座", "双子座", "巨蟹座", "狮子座", "处女座", "天秤座", "天蝎座", "射手座", "摩羯座"]

    if day >= limits[month - 1]:
        return signs[month - 1]
    else:
        return signs[month - 2]

def test_solution():
    assert solution(2000, 2, 15) == "水瓶座"
    assert solution(1970, 6, 5) == "双子座"
    assert solution(1987, 8, 23) == "狮子座"
    assert solution(2000, 12, 21) == "射手座"
    assert solution(2000, 1, 15) == "摩羯座"