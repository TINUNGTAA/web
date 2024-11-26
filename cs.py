

# def main():
#     height=int(input("Enter the height :  "))
#     print (height)
#     cal(height)
    
    
    
# def cal(n):
#     for i in range(n):
#         print("#"*(i))





distance={
    "voyager 1":163,
    "voyager 2": "136",
    "pioneer 10":80 "AU",
    "new horizons":8,
    "pioneer 11": "44 AU"
    
}


def main():
    spacecraft=input("enter a spacecraft: ")
    au=float(distance[spacecraft])
    m=converter(au)
    print(f"{m} m away")
    
    
    
def converter(au):
    return au*149597870700
    
main()




