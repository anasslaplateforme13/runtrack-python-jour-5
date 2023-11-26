def draw_rectangle(width, height):
    horizontal = '|' + '-' * (width - 2) + '|'
    vertical = '|' + ' ' * (width - 2) + '|'
    
    for i in range(height):
        if i == 0 or i == height - 1:
            print(horizontal)
        else:
            print(vertical)

draw_rectangle(10, 3)