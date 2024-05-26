def add_person_info(people_list):
    name = input("请输入名字：")
    position = input("请输入职位：")
    address = input("请输入住址：")
    # 将个人信息作为一个字典存储在列表中
    people_list.append({'Name': name, 'Position': position, 'Address': address})


def query_person_info(people_list):
    name_to_query = input("你想查询哪个人的信息？请输入名字：")
    for person in people_list:
        if person['Name'] == name_to_query:
            print(f"{name_to_query} 的信息如下：")
            print(f"职位：{person['Position']}, 住址：{person['Address']}")
            return
    print("未找到此人的信息。")


def display_all_info(people_list):
    print("\n所有输入的个人信息如下：")
    for person in people_list:
        print(f"名字: {person['Name']}, 职位: {person['Position']}, 住址: {person['Address']}")


def main():
    people_list = []
    while True:
        print("\n欢迎使用个人信息管理系统")
        print("1. 添加个人信息")
        print("2. 查询个人信息")
        print("3. 显示所有信息")
        print("4. 退出程序")
        choice = input("请输入选项（1-4）：")

        if choice == '1':
            add_person_info(people_list)
        elif choice == '2':
            query_person_info(people_list)
        elif choice == '3':
            display_all_info(people_list)
        elif choice == '4':
            print("感谢使用本程序，再见！")
            break
        else:
            print("无效的输入，请重新输入！")


if __name__ == "__main__":
    main()