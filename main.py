fr=open("Followers.txt","r")
fg=open("Following.txt","r")

followers=list()
following=list()

with open("Followers.txt", 'r', encoding='utf-8') as fr:
    lines = fr.readlines()
    selected_lines = [lines[i] for i in range(1, len(lines), 3)]
    followers=selected_lines


with open("Following.txt", 'r', encoding='utf-8') as fg:
    lines = fg.readlines()
    selected_lines = [lines[i] for i in range(1, len(lines), 3)]
    following=selected_lines

def extra_followers():
    for x in followers:
        flag=False
        if x in following:
            flag=True
        if not flag:
            print(x,end="")

def imposter():
    for x in following:
        flag=False
        if x in followers:
            flag=True
        if not flag:
            print(x,end="")

choice=int(input("1. Extra Followers  2. Imposters\n"))

if choice == 1:
    extra_followers()

elif choice == 2:
    imposter()

input("\nPress any key to continue...")
