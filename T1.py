"""九九乘法表"""
def main():
	for i in range(1,10):
		for j in range(1,i+1):
			print("{}x{}={}\t".format(j,i,i*j), end="")
		print("",end="\n")

if __name__ == '__main__':
	main()