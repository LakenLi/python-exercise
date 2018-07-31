##生成优惠券
#
import random

def rand_gen(lenght = 8):
	string = 'abcdefghijkmnopqrstuvwxyzABCDEFGHIJKMNOPQRSTUVWXYZ1234567890';
	gen = []

	while(len(gen) < lenght):
		index = random.randint(0, len(string) - 1)
		
		rand = string[index]

		gen.append(rand)
	

	return ''.join(gen)


def create_discount(num):
	discount = [];
	for i in range(1, num):
		discount.append(rand_gen())

	return discount;


if __name__ == '__main__':
	discount = create_discount(200)
	print(discount)