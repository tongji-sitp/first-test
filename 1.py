def welcome_new_member(name, organization_name):  
    print(f"欢迎 {name} 加入 {organization_name}！")  
    print(f"我们很高兴您能成为我们团队的一员。")  
    print(f"请享受在这里的时光，一起努力，共同成长！")  
  
# 示例用法  
if __name__ == "__main__":  
    new_member_name = input("请输入新成员的名字: ")  
    organization_name = "Github协作组织"   
    welcome_new_member(new_member_name, organization_name)