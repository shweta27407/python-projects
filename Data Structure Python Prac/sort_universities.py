"""
Notes  
    # sorted can used for anything that's iterable. if you want to keep the original list and print a sorted new list then use 'sorted'. The input remains unchanged for 'sorted'
    # sort is used for lists only. If we want to print and overwrite an input list then use 'sort'
    

"""

import random


class University:
    def __init__(self, name: str, founding_year: int, country: str) -> None:
        self.name = name
        self.founding_year = founding_year
        self.country = country
        
    def __repr__(self) -> str:
        return repr((self.name, self.founding_year, self.country))


if __name__ == "__main__":
    tmp_list = list(range(1000))
    random.shuffle(tmp_list)
   
    universities = [
        ("Otto-von-Guericke-Universität Magdeburg", 1993, "Germany"),
        ("Harvard University", 1636, "USA"),
        ("Technische Universität München", 1868, "Germany"),
        ("RWTH Aachen", 1870, "Germany")
    ]
    sorted_by_age = sorted(universities, key=lambda x: x[1])  # Sorted universities by age
    print(sorted_by_age)
    sorted_by_name = sorted(universities)  # Sorted universities by name
    print(sorted_by_name)

    university_objects = [University(name=u[0], founding_year=u[1], country=u[2]) for u in universities]
    sorted_by_age = sorted(universities, key=lambda x: x[1])  # Sorted universities by age
    print(sorted_by_age)
    sorted_by_name = sorted(universities)  # Sorted universities by name
    print(sorted_by_name)




  

   