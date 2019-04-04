from datetime import datetime

def changetime(time):
    time = time.split(":")
    temp=''
    for i in time:
        temp+=i+"_"
    time = temp
    time = time.split(" ")
    temp = ''
    count = 0
    for i in time:
        temp+=i
        if count==0:
            temp+='T'
            count=1
    time = temp
    time = time.split(".")
    temp = ''
    for i in time:
        temp+=i+'_'
    time = temp
    return time

if __name__ == "__main__":
    print(changetime(str(datetime.now())))