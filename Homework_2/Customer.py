from Productcheck import products
from Productcheck import check


def buy(product, num, price):
    if checker.check(product, num) == True:
        print('You bought %product and spent %num*%price' % product %num %price)
    else:
        print('Sorry! We are out of this product.')



def main():
    buy('candy',10,3)



if __name__ == "__main__":
    main()
