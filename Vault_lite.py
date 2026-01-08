def vault_lite():
    print("---VAULT LITE---")
    print("1.View Credential")
    print("2.Add First Credential")
    print("3.Add remaining Credential")
    print("4.Update Credential")
    print("5.Exit")
    def initial_credential():
        website=input("Website : ")
        username=input("Username : ")
        password=input("Password: ")
        st =f"1.{username}@{website}"
        file=open("vault_data.txt","w")
        file.write(st)
        file.close()
        print("credential saved successfully ")
        vault_lite()
    def add_credential():
        count=2
        website=input("Website : ")
        username=input("Username : ")
        password=input("Password: ")
        st =f"{count}.{username}@{website}\n"
        file=open("vault_data.txt","a")
        count+=1
        file=open("vault_data.txt","a")
        file.write(st)
        file.close()
        print("credentials saved successfully ")
        vault_lite()
    def view_credential():
        file =open("vault_data.txt","r")
        data=file.read()
        list_data=data.strip("\n")
        for i in list_data:
            print(i,end="")
        file.close()
        vault_lite()
    def update_credential():
        user_choice=int(input("Enter number to update : "))
        new_password=input("Enter new Password: ")+"\n"
        file=open("vault_data.txt","r")
        data=file.read()
        list_data=data.strip("\n")
        for i in list_data:
            if str(user_choice) in i:
                h=i.split("@")
                i.replace(h[-1],new_password)
                list_data.remove(i)
                list_data.insert([index(i)],i)
        data2="".join(list_data)
        with open("vault_data.txt","w") as file:
            file.write(data2)
        vault_data()
    def exit():
        print("exiting vault lite")
        print("thanks for choosing vault lite ")
    user_choice1=int(input("Enter choice"))
    if user_choice1==1:
        view_credential()
    if user_choice1==2:
        initial_credential()
    if user_choice1==3:
        add_credential()
    if user_choice1==4:
        update_credential()
    if user_choice1==5:
        exit()
vault_lite()
