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

#Ссылка для решения
#https://www.google.ru/search?q=%D0%BC%D0%BD%D0%B8%D0%BC%D0%BE%D0%B5+%D0%B8%D0%BB%D0%B8+%D0%B4%D0%B5%D0%B9%D1%81%D1%82%D0%B2%D0%B8%D1%82%D0%B5%D0%BB%D1%8C%D0%BD%D0%BE%D0%B5+%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5&newwindow=1&safe=strict&sca_esv=588006686&rlz=1C1GCEU_ruRU999RU999&tbm=isch&source=lnms&sa=X&ved=2ahUKEwjb-YG6oviCAxUQHxAIHcRTBlQQ_AUoAXoECAEQAw&biw=1920&bih=963&dpr=1#imgrc=b1q6hIR_91mn-M
        