from matplotlib import pyplot as plt

products = ['A', 'B', 'C', 'D', 'E']
sales = [30, 25, 15, 20, 10]

plt.pie(sales, labels=products, autopct='%1.1f%%')
plt.title('Phần Trăm Doanh Số Của 5 Sản Phẩm')
plt.show()