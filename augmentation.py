from PIL import Image, ImageEnhance
import os
import random
import shutil


def init_augmentation(path_from, path_to, multiplier=1, remove_old_augmentation_image=True, colors='rgb'):
    images_dir = 'images'
    labels_dir = 'labels'
    if remove_old_augmentation_image:
        remove_augmentation_image([f'{path_to}/{images_dir}/', f'{path_to}/{labels_dir}/'])

    for iteration in range(multiplier):
        for filename in sorted(os.listdir(f'{path_from}/{images_dir}/')):
            if 'augmentation' not in filename:
                image = Image.open(os.path.join(f'{path_from}/{images_dir}/', filename))
                # image.show()
                image = augment_image(image)
                image.save(os.path.join(f'{path_to}/{images_dir}/', f'augmentation{iteration + 1}_' + filename))

    for iteration in range(multiplier):
        for filename in sorted(os.listdir(f'{path_from}/{labels_dir}/')):
            if 'augmentation' not in filename:
                shutil.copyfile(f'{path_from}/{labels_dir}/' + filename,
                                f'{path_to}/{labels_dir}/augmentation{iteration + 1}_' + filename)


def remove_augmentation_image(paths=[]):
    for path in paths:
        for filename in sorted(os.listdir(f'{path}')):
            if 'augmentation' in filename:
                os.remove(os.path.join(f'{path}', filename))


def augment_image(image,  # Изображение для аугментации
                  level_contr=0.5,  # Максимальное отклонение коэффициента контраста от нормы
                  level_brght=0.5):  # Максимальное отклонение коэффициента яркости от нормы

    # Функция нахождения ширины и высоты прямоугольника наибольшей площади
    # после поворота заданного прямоугольника на угол в градусах

    # Функция случайного изменения контрастности

    def random_contrast(x,  # Подаваемое изображение
                        level=level_contr  # Максимальное отклонение коэффициента контраста от нормы - число от 0. до 1.
                        ):
        enh = ImageEnhance.Contrast(x)  # Создание экземпляра класса Contrast
        factor = random.uniform(1. - level,
                                1. + level)  # Cлучайный коэффициент контраста из указанного интервала
        return enh.enhance(factor)  # Изменение коэффициента контраста

    # Функция случайного изменения яркости

    def random_brightness(x,  # Подаваемое изображение
                          level=level_brght  # Максимальное отклонение коэффициента яркости от нормы - число от 0. до 1.
                          ):
        enh = ImageEnhance.Brightness(x)  # Создание экземпляра класса Brightness
        factor = random.uniform(1. - level,
                                1. + level)  # Cлучайный коэффициент контраста из указанного интервала

        return enh.enhance(factor)  # Изменение коэффициента яркости

    # Тело основной функции

    # Cоздание списка модификаций
    mod_oper = [random_contrast,
                random_brightness]

    # Cлучайное количество изменений из списка; минимум одно изменение
    # mod_count = random.randrange(len(mod_oper) + 1)

    # Случайный отбор индексов изменений в количестве mod_count без повторений
    # mod_list = random.sample(range(len(mod_oper)), mod_count)

    # Применение модификаций по индексам из mod_list
    # for mod_index in mod_list:
    for operation in mod_oper:
        # image = mod_oper[mod_index](image)
        image = operation(image)

    # Возврат результата
    return image
