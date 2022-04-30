from ..meal import Meal
from jinja2 import Environment, FileSystemLoader
import os


class CreateHtmlFile:
    '''Create html file with description of meals'''

    def __init__(self):
        root_path = os.path.dirname(os.path.abspath(__file__))
        template_dir = os.path.join(root_path, 'templates')
        self.env = Environment(loader=FileSystemLoader(template_dir))
        self.template = self.env.get_template('template.html')

    def __repr__(self):
        return 'Create html file'

    def create_html_file(self, meals: list[Meal], ingredients: list[str]) -> None:
        '''Create html file with all 5 meals'''
        filename = self.create_html_filename(ingredients)
        with open(f'html_pages/{filename}', 'w') as f:
            f.write(self.template.render(
                meals = meals
            ))
            
    @staticmethod 
    def create_html_filename(ingredients: list[str]) -> str:
        '''Return a output file made of names of ingredients'''
        return '_'.join(ingredients) + '.html'
