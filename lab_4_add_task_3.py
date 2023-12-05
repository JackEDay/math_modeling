def ai(lens_type, d, f):
    if lens_type == 'Собирающая':
        if d < f:
            image_type = 'Мнимое, увеличенное, прямое.'
        elif d > 2 * f:
            image_type = 'Действительное, '
        else:
            image_type = 'Нет изображения'
    
        