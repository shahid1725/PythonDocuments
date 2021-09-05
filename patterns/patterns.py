        # pattern 1

# *...
# *...*...
# *...*...*...
# *...*...*...*...
# for i in range(0,6):    #for setting row  #i=0,1,2,3,4..
#     for j in range(i):  #j=0,1,2,3...
#         print("*",end="  ")
#     print("\r")

        # pattern 2
# * * * * *
# * * * *
# * * *
# * *
# *
# for i in range(6,0,-1):  #startin with 6th row to zeroth row by reducing 1
#     for j in range(i):
#         print("*",end="  ")
#     print("\r")

        #pattern 3
#1
#2 3
#4 5 6
# num=1
# for i in range(0,5):
#     for j in range(i):
#         print(num,end="  ")
#         num+=1
#     print("\r")

     #or

# def pattern(n):
#     num=1
#     for i in range(n):
#         for j in range(i):
#             print(num,end="  ")
#             num+=1
#         print("\r")
# pattern(5)

        #pattern 3

#1
#1 2
#1 2 3
#1 2 3 4

# def pattern(n):
#     for i in  range(n):
#         num=1
#         for j in range(i):
#             print(num,end="  ")
#             num+=1
#         print("\r")
# pattern(6)

            #pattern 4
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *
# * * * * * *

# for i in range(6):
#     for j in range(6):
#         print("*",end=" ")
#     print("\r")

         #or
# def pattern(n):
#     for i in range(n):
#         for j in range(n):
#             print("*",end="  ")
#         print("\r")
# pattern(6)

            #pattern 5
#           *
#          * *
#         * * *
#       * * * * *
#      * * * * * *
#     * * * * * * *

# s=6 #spacing
# for i in range(6):
#     for r in range(s):
#         print(end=" ")
#     s=s-1
#
#     for j in range(i):
#         print("*",end=" ")
#     print("\r")

            #pattern 6

# * * * * * *
#  * * * * * *
#   * * * * * *
#    * * * * * *
#     * * * * * *

# k=1
# for i in range(6):
#     for r in range(k):
#         print(end=" ")
#     k+=1
#
#     for j in range(6):
#         print("*",end=" ")
#     print("\r")

                #or

# def pattern(n):
#     k=6
#     for i in range(n):
#         for r in range(k):
#             print(end=" ")
#         k+=1
#
#         for j in range(n):
#             print("*",end=" ")
#         print("\r")
# pattern(5)


          #     * * * * *
          #    * * * * *
          #   * * * * *
          #  * * * * *
          # * * * * *
# k=6
# for i in range(5):
#     for r in range(k):
#         print(end=" ")
#     k=k-1
#
#     for j in range(5):
#         print("*",end=" ")
#     print("\r")




