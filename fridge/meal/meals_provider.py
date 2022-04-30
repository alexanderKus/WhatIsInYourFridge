from . import Meal, MealsCollector
import requests
import os


class MealsProvider:
    '''Create meals from api and store them in meal collector'''

    api_key: str = os.getenv('SPOONACULAR_API')
    number_of_meals: int = 5
    number_of_meals_in_api: int = 100

    def __init__(self, include_ingredients: list, exclude_ingredients: list) -> None:
        self.include_ingredients = include_ingredients
        self.exclude_ingredients = exclude_ingredients
        self.meals_collector = MealsCollector()

    def get_meals_with_api(self) -> None:
        '''makes api call and gets list ofmeals'''
        url = f'https://api.spoonacular.com/recipes/findByIngredients?apiKey={MealsProvider.api_key}{self.make_ingredients()}&number={str(MealsProvider.number_of_meals_in_api)}&ranking=1&ignorePantry=true'
        try:
            data = requests.get(url)
        except requests.exceptions.RequestException as e:
            print(e)
            exit(1)
        self.all_meals_json = data.json()
        self.make_meals()

    def make_ingredients(self) -> str:
        '''return a string that contains ingredients for apis url'''
        return '&ingredients=' + ',+'.join(self.include_ingredients)

    def make_meals(self) -> None:
        '''Add meal to meal collector'''
        for meal in self.all_meals_json:
            self.meals_collector.add_meal(
                Meal(
                    meal['id'], meal['title'], meal['image'],
                     meal['usedIngredientCount'],
                     meal['missedIngredientCount'],
                     self.get_list_of_names_of_ingredients(
                        meal['missedIngredients']
                    ),
                        self.get_list_of_names_of_ingredients(
                        meal['usedIngredients']
                    ),
                        self.get_list_of_names_of_ingredients(
                        meal['unusedIngredients']
                    )
                )
            )

    def get_list_of_names_of_ingredients(self, ingredients: list) -> list:
        '''Return list of names needed for meal form dictionary'''
        return [ingredient['name'] for ingredient in ingredients]

    def get_top_5_meals(self) -> MealsCollector:
        '''Generate 5 meals with the smallest number of missed ingredients,
        it does not mean that all of included ingredients had been used'''
        count = 0
        top_5_meals = MealsCollector()
        for meal in self.meals_collector.get_list_of_meals():
            if count > MealsProvider.number_of_meals - 1:
                break
            if not self.check_if_meal_is_allowed(meal):
                continue
            top_5_meals.add_meal(meal)
            count += 1
        return top_5_meals

    def check_if_meal_is_allowed(self, meal: Meal) -> bool:
        '''Check is meal does not contain excluded ingredients'''
        used_ingredients = meal.used_ingredients
        missed_ingredients = meal.missed_ingredients
        for ingredient in self.exclude_ingredients:
            if (ingredient in used_ingredients or
                    ingredient in missed_ingredients):
                return False
        return True

    def get_list_of_meals(self) -> MealsCollector:
        return self.meals_collector

    @classmethod
    def set_number_of_meals(cls, number: int) -> None:
        cls.number_of_meals = number

    @classmethod
    def set_api_key(cls, key: str) -> None:
        cls.api_key = key

    @classmethod
    def set_number_of_meals_in_api(cls, number: int) -> None:
        cls.number_of_meals_in_api = number
