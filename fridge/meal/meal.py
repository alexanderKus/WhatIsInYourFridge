from dataclasses import dataclass


@dataclass
class Meal:
    '''Class to represent a meal'''
    id: int
    title: str
    image: str
    used_ingredient_count: int 
    missed_ingredient_count: int 
    missed_ingredients: list[str]
    used_ingredients: list[str]
    unused_ingredients: list[str]
