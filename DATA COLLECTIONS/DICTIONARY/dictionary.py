# dict={'name':'zara','age':28,'class':'nineth'}
# print(dict)
# print(type(dict))
# #
# print(dict['name'])                   #1...keys are unique,values change
# print(dict['age'])                    #keys same type aakanam (eg;str,int)

#empty
# dic={}
# print(dic)
# print(type(dic))

#update values
#-------------
# dict={'name':'zara','age':28,'class':'nineth'}
# dict['age']=10                            #2.. mutable
# print(dict)                               #3...duplication allowed

#add new element
#-------------
# dict={'name':'zara','age':28,'class':'nineth'}
# dict['scool']='malappuram'
# print(dict)

# dict={'name':'zara','age':28,'class':'nineth'}
# dict.update({'location':'kochi','phone':9526646563})          #update--- can add element
# print(dict)

#remove elements
#--------------
# dict={'name':'zara','age':28,'class':'nineth'}
# del dict['name']                                                #del----delete a single element
# print(dict)
#
# dict.clear()                                                       #clear-- delete full
# print(dict)
#
# del dict                                                        #delete full dict
# print(dict)

#Q.check user dictionary present on given dictionary
# dict={1:10,2:56,5:55,9:100}
#
#
# def is_present(x):
#     if x in dict:
#         print(x,"is present in dictionary")
#     else:
#         print(x,"is not present in dictionary")
#
# is_present(5)

#SPLIT METHOD
#-----------
# a="nannayi,nee,padikkanam"
# b=a.split(',')                #split cheyyan word(by comma)
# print(b)
# for i in b:
#     print(i)
#
#nesting
#-------
# a={1:10,2:20,3:{5:50,6:60}}
# print(a)                            #4...nesting possible

#Q...COUNT THE GIVEN STRING WORD AND SHOW DICTIONARY COUNT KEY AND VALUES

count={}
user=input("enter")
words=user.split(" ")
#print(words)
for word in words:
    if word not in count:
        count.update({word:1})
    else:
        val=int=(count[word])
        val+=1
        count.update({word:val})
print(count)