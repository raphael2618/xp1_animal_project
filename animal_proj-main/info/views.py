from django.shortcuts import render
import json
# Create your views here.
def get_data():
    with open('data.json') as f:
        return json.load(f)

def animal_view(request, animal_id):
    data = get_data()
    selected_animal = None
    for animal in data['animals']:
        if animal['id'] == animal_id:
            selected_animal = animal
    return render(request, 'animal.html', {'animal': selected_animal})


def family_view(request, family_id):
    data = get_data()
    selected_family = None
    for family in data['families']:
        if family['id'] == family_id:
            selected_family = family

    fam_animals = [animal for animal in data['animals'] if animal['family'] == family_id]
    return render(request, 'family.html', {'family': selected_family, 'animals': fam_animals})
