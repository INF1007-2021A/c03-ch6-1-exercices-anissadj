#!/usr/bin/env python
# -*- coding: utf-8 -*-


def order(values: list = None) -> list:
    if values is None:
        # TODO: demander les valeurs ici
        list1 = []
        for i in range(0,10) : 
            list1.append(input('Entrez 1 valeur : '))
            i+=1
      
    return sorted(list1)


def anagrams(words: list = None) -> bool:
    if words is None:
        # TODO: demander les mots ici
        mot1 = input('entrez le premier mot : ')
        mot2 = input('entrez le deuxieme mot : ')
        return(sorted(mot1) == sorted(mot2)) 



def contains_doubles(items: list) -> bool:
  return (len(items) == len(set(items)))




def best_grades(student_grades: dict) -> dict:
    # TODO: Retourner un dictionnaire contenant le nom de l'étudiant ayant la meilleure moyenne ainsi que sa moyenne
    best_grades2 = []
    names2 = []

    for names in student_grades : 
        grades = student_grades[names]
        moyenne = sum(grades)/len(grades)
        best_grades2.append(moyenne)
        names2.append(names)
    best_grade = max(best_grades2)
    return {names2[best_grades2.index(best_grade)] : best_grade}



def frequence(sentence: str) -> dict:
    # TODO: Afficher les lettres les plus fréquentes
    #       Retourner le tableau de lettres

    return {}


def get_recipes():
    # TODO: Demander le nom d'une recette, puis ses ingredients et enregistrer dans une structure de données
    pass


def print_recipe(ingredients) -> None:
    # TODO: Demander le nom d'une recette, puis l'afficher si elle existe
    pass


def main() -> None:
    print(f"On essaie d'ordonner les valeurs...")
    print(order())


    print(f"On vérifie les anagrammes...")
    print(anagrams())

    my_list = [3, 3, 5, 6, 1, 1]
    print(f"Ma liste contient-elle des doublons? {contains_doubles(my_list)}")

    grades = {"Bob": [90, 65, 20], "Alice": [85, 75, 83]}
    best_student = best_grades(grades)
    print(f"{list(best_student.keys())[0]} a la meilleure moyenne: {list(best_student.values())[0]}")

    sentence = "bonjour, je suis une phrase. je suis compose de beaucoup de lettre. oui oui"
    frequence(sentence)

    print("On enregistre les recettes...")
    recipes = get_recipes()

    print("On affiche une recette au choix...")
    print_recipe(recipes)


if __name__ == '__main__':
    main()
