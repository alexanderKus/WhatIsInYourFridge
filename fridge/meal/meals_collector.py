from .meal import Meal


class MealsCollector():
    '''Store a list of meals'''

    def __init__(self):
        self.list_of_meals = []

    def __repr__(self):
        return f"Meals Collector stores list of meals"

    def __str__(self):
        return 'MealsCollector, All meals'+', '.join(meal.title for meal in self.list_of_meals)

    def add_meal(self, meal: Meal) -> None:
        '''Add a meal'''
        self.list_of_meals.append(meal)

    def get_list_of_meals(self) -> list:
        '''Return list of all meals'''
        return self.list_of_meals
