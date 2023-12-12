def ai(lens_type, d, f):
    if lens_type == 'Собирающая':
        if d < f:
            image_type = 'Мнимое, увеличенное, прямое.'
        elif d > 2 * f:
            image_type = 'Действительное, уменьшенное, обратное'
        elif d < 2 * f and d > f:
            image_type = 'Действительное, увеличенное, обратное'
        else:
            image_type = 'Нет изображения'
    
    if lens_type == 'Рассеивающая':
        image_type = 'Мнимое, прямое'

    return image_type

print(ai('Собирающая', 12, 5))
        