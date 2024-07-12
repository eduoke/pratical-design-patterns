from singleton import SingletonObject 

def main():
    obj1 = SingletonObject()
    obj1.value = 'this is a SingletonObject:1'
    
    print(obj1)
    obj2 = SingletonObject()
    obj2.value = 'this is a SingletonObject:2'
    print(obj2)
    
if __name__ == '__main__':
    main()