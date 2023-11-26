def draw_triangle(height):
    for i in range(height):
        if i == 0:

            spaces = '_' * (height - 1)
            print(spaces + '/')

        elif i == height - 1:
            print('/' + '_' * (2 * height - 1))
            
        else:
            spaces = ' ' * (height - i - 1)
            print(spaces + '/' + '_' * (2* i - 1) + '\\')

draw_triangle(5)


