# import turtle
# import random
#
# t = turtle.Turtle()
# t.speed(0)
# # Hide Turtle
# t._tracer(0, 0)
# t.ht()
# t.fillcolor('pink')
#
# def curve():
#     t.speed(0)
#     for i in range(200):
#         t.right(1)
#         t.forward(1)
#
#
#
# def heart1():
#     t.left(140)
#     t.forward(113)
#     curve()
#     t.left(120)
#     curve()
#     t.forward(112)
#     # t.forward(112)
#     # curve()
#
#
# def txt():
#     t.up()
#     t.setpos(-29, 80)
#     t.down()
#     t.color('red')
#
#     t.write("Lana", font=("Audrey", 20, "bold"))
#
#
#
# t.begin_fill()
# heart1()
# t.left(50)
# heart1()
# t.left(50)
# heart1()
# t.left(50)
# heart1()
# t.end_fill()
# txt()
# t._update()
# t.screen.mainloop()








nums = [1,23, 4, 24, 345, 456, 456, 4, 567, 5,2 ,345, 2345, 456, 3456, 3456, 345,2, 345, 4]


def even(nums):
    # return [num in nums if num % 2 == 0]
    return [num for num in nums if num % 2 == 0]

    # result = []
    #
    # for num in nums:
    #     if num % 2 == 0:
    #         result.append(num)
    # return result

print(even(nums))
