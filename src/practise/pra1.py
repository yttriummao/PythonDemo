# coding=utf-8

''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
##### 题目：有四个数字：1、2、3、4，能组成多少个互不相同且无重复数字的三位数？各是多少？
# 程序分析：可填在百位、十位、个位的数字都是1、2、3、4。组成所有的排列后再去 掉不满足条件的排列。
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# 个位
singleDigit = ['1', '2', '3', '4']
# 十位
tensDigit = ['1', '2', '3', '4']
# 百位
hundredDigit = ['1', '2', '3', '4']

# 结果
result = []


def main():
    for hD in range(4):
        hundred = hundredDigit[hD]
        
        for tD in range(4):
            if tensDigit[tD] != hundred:
                tens = tensDigit[tD]
                for sD in range(4):
                    if singleDigit[sD] != tens and singleDigit[sD] != hundred:
                        single = singleDigit[sD]
                        res = hundred + tens + single
                        result.append(res)
    
    
    print(result)



if __name__ == "__main__":
    main()