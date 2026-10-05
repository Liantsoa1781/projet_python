from rich.console import Console

console = Console()

console.print("Bienvenue dans mon projet de ticketing !")

console.print("1. Créer un ticket!")
console.print("2. Afficher un ticket!")
console.print("3. Modifier un ticket!")
console.print("4. Suprimer un ticket!")
console.print("5. Quitter")

choix = int(input("Votre choix: "))
print(choix)

def creation_ticket():
    print("Créer un nouveau ticket! ")
    description = input("Description: ")
    priorite = input("Priorite: ")

    console.print(description)
    console.print(priorite)

if choix == 1:
    creation_ticket()

    


