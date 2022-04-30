from fridge import Fridge


def main() -> None:
    includes = ['tomatoes', 'eggs', 'pasta']
    excludes = ['plums']
    f = Fridge(includes, excludes)
    f.search_for_meals()


if __name__ == '__main__':
    main()
