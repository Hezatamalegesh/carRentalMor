from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return render(request, 'index.html.jinja')

def cars(request):
    cars = Car.objects.all()
    cars_table = pd.DataFrame.from_records(cars.values())

    # Słownik mapujący kategorie na ich przyjazne użytkownikowi nazwy
    category_dict = dict(Car.CATEGORIES)

    # Tworzenie struktury danych dla szablonu
    cars_by_category = {}
    for car in cars:
        category_name = category_dict[car.category]
        if category_name not in cars_by_category:
            cars_by_category[category_name] = []
        cars_by_category[category_name].append(car)

    return render(request, 'cars.html.jinja', {'cars_by_category': cars_by_category, 'cars_table': cars_table.to_html(classes='table table-striped table-bordereds', index=False, table_id='cars_table')}, )

def index(request, car_id):
    return render(request, 'car.html.jinja')