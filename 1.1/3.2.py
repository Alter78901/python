
def main():
    print("欢迎使用10086自助查询系统")
    while True:
        choice = input("请输入查询选项（1:余额，2:流量，3:通话时长，0:退出）：\n")
        if choice == '1':
            print("当前余额：¥200.00")
        elif choice == '2':
            print("当前剩余流量：1000G")
        elif choice == '3':
            print("当前剩余通话时长：1000分钟")
        elif choice == '0':
            print("感谢使用，再见！")
            break
        else:
            print("无效的选择，请重新输入。")

if __name__ == "__main__":
    main()