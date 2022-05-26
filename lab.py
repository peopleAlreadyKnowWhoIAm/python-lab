from electricelements import *

def main():
    schema = [
        VoltageSource(12,0.01,50,1),
        BinarySummator((False,False,True,False), (True,False,True,False),  # type: ignore
                       3.8, 2.2, 10, 5),
        CurrentSource(0.1, 0.1, 25, 0),
        OperationalAmplifier(0.02, 150, 0.0001, 20, -12),
        BinaryToUnaryDecoder((False,True,False,True), 3.8, 2.0, 20, 4.5), #type: ignore
    ]
    for elem in schema:
        print(elem)

if __name__ == '__main__':
    main()
