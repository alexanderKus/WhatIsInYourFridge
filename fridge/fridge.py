from .meal import MealsProvider
from .html import CreateHtmlFile


class Fridge():
    '''Class Fridge'''

    create_html = CreateHtmlFile()
    MealsProvider.set_number_of_meals(5)
    MealsProvider.set_number_of_meals_in_api(100)

    def __init__(self, include_ingredients: list, exclude_ingredients: list) -> None:
        self.include_ingredients = include_ingredients
        self.exclude_ingredients = exclude_ingredients
        self.meals_provider = MealsProvider(
            include_ingredients, exclude_ingredients)

    def __repr__(self) -> str:
        return "Class Searcher, create list of meals, \
            and top 5 meals based on given included and excluded ingredients"

    def search_for_meals(self):
        print("Using API...")
        self.meals_provider.get_meals_with_api()
        top_5_meals = self.meals_provider.get_top_5_meals()
        print("Creating output file...")
        Fridge.create_html.create_html_file(
            top_5_meals.get_list_of_meals(), self.include_ingredients)
        print("Check out: html_pages/output_file")
