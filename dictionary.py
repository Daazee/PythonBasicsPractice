# Enter your code here. Read input from STDIN. Print output to STDOUT
n = input()
dic = {}
for i in range(int(n)):
    phone_details = input()
    phone_details_split = phone_details.split(' ')
    dic[phone_details_split[0]]= phone_details_split[1]

for i in range(int(n)):
    key = input()
    check_if_key_exist = key in dic
    if(check_if_key_exist == True):
        value = dic[key]
        print(key + "=" + value)
    else:
        print("Not found")
    # value = dic[key]
    # print(key + "=" + value)
