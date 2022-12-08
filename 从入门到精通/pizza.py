# 形参为多个元素的列表 不确定有多少个元素时 难怪在def里引用时，需要跟（）里的变量名一致
def make_pizza (*toppings): #‼️注意‼️此处 *toppings创建了一个空的元组！！
    '''制作一个pizza'''
    
    for topping in toppings:
        print (f'准备加入披萨的原料有：{topping}')
    return(toppings)

def eat_pizza(pizza):
    print(f'我把 {pizza}吃了')

