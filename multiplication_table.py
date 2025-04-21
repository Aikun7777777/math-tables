"""99乘法表生成器

支持生成不同大小的乘法表，并可以控制输出格式
"""

def print_multiplication_table(size=9, separator="\t"):
    """打印乘法表
    
    Args:
        size (int): 乘法表的大小，默认为9
        separator (str): 列分隔符，默认为制表符
    """
    print(f"{'':<4}", end="")  # 对齐表头
    for i in range(1, size+1):
        print(f"{i:<8}", end="")
    print("\n" + "-" * (8*size + 4))
    
    for i in range(1, size+1):
        print(f"{i}:", end="   ")
        for j in range(1, i+1):
            print(f"{j}x{i}={i*j:<5}", end=separator)
        print()

if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description='生成乘法表')
    parser.add_argument('-s', '--size', type=int, default=9, 
                       help='乘法表的大小')
    parser.add_argument('-sep', '--separator', default="\t",
                       help='列分隔符')
    args = parser.parse_args()
    
    print_multiplication_table(args.size, args.separator)