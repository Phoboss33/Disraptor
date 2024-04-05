import os
import django

# Устанавливаем переменную окружения DJANGO_SETTINGS_MODULE для указания файла настроек Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')

# Загружаем настройки Django
django.setup()


from django.utils import timezone
from datetime import datetime, timedelta
import random
from lending.models import Respondent

def generate_random_respondent():
    """
    Генерирует случайные данные для модели Respondent.
    """
    first_names_male = ['John', 'Michael', 'William', 'James', 'David']
    first_names_female = ['Mary', 'Jennifer', 'Linda', 'Patricia', 'Elizabeth']
    surnames = ['Smith', 'Johnson', 'Williams', 'Jones', 'Brown']
    patronymics = ['Adamovich', 'Alexandrovich', 'Andreevich', 'Antonovich', 'Artemovich']
    sexes = ['male', 'female']
    suggestions = ['Good listener', 'Good communicator', 'Team player', 'Hard worker', 'Problem solver']

    first_name = random.choice(first_names_male + first_names_female)
    surname = random.choice(surnames)
    patronymic = random.choice(patronymics)
    birthdate = timezone.now() - timedelta(days=random.randint(18*365, 80*365))  # Случайная дата рождения от 18 до 80 лет назад
    sex = random.choice(sexes)
    suggestion = random.choice(suggestions)
    created_date = timezone.now()

    respondent = Respondent.objects.create(
        first_name=first_name,
        surname=surname,
        patronymic=patronymic,
        birthdate=birthdate,
        sex=sex,
        suggestions=suggestion,
        created_date=created_date
    )
    return respondent

def generate_random_data(num_entries):
    """
    Генерирует заданное количество случайных записей Respondent.
    """
    for _ in range(num_entries):
        generate_random_respondent()

if __name__ == "__main__":
    num_entries = 100  # Количество записей для генерации
    generate_random_data(num_entries)
