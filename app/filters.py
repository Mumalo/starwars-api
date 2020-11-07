
def sort_by_hyperdrive_rating(starships):
    return sorted(starships,
                  key=lambda starship: float(starship.get('hyperdrive_rating'))
                  )
