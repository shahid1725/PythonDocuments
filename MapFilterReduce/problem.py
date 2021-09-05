products=[
    {"name":"complan","rate":5200,"qty":20},
    {"name":"horlicks","rate":6200,"qty":30},
    {"name":"boost","rate":4200,"qty":0},
    {"name":"chaya","rate":3100,"qty":0},
    {"name":"milk","rate":3000,"qty":22}

]

# #Q... print all product name in shop
#
# namepro=list(map(lambda nam:nam["name"],products))
# print(namepro)


# #Q... print available products in shop based on quantity
#
# qty=list(filter(lambda pro:pro["qty"]>0,products))
# print(qty)


# #Q...Print out of stock products
# stock=list(filter(lambda item:item["qty"]==0,products))
# print(stock)

#Q..print costly product
# from functools import reduce
#
# prices=list(map(lambda price:price["rate"],products))
# # print(prices)
# costly=reduce(lambda price1,price2:price1 if price1>price2 else price2,prices)
# print(costly)

#easy method
# prices=list(map(lambda price:price["rate"],products))
# z=max(prices)
# print(z)


#Q...LOW COST PRODUCT

# prices=list(map(lambda price:price["rate"],products))
# z=min(prices)
# print(z)

# m=[]
# lst=[2,4,6]   #op- [10,8,6]
# z=print(sum(lst))
# for i in lst:
#     k=z-i
#     m.append(k)
# print(m)



# sum of pairs
lst=[2,3,4,5]  # 6 (2,4) 7(5,2) (4,3)
total=int(input("enter num"))
for i in lst:
    for j in lst:
        if (i!=j):
            if (total==i+j):
                print(i,j)


