import pandas as pd
import matplotlib.pyplot as plt

pokemon = pd.read_csv('Pokemon Database.csv')

Pokemon_Primary_Type = pokemon['Primary Type']
Grass_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Grass']
Poison_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Poison']
Water_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Water']
Fire_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Fire']
Normal_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Normal']
Fighting_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Fighting']
Flying_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Flying']
Ground_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Ground']
Rock_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Rock']
Bug_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Bug']
Ghost_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Ghost']
Steel_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Steel']
Electric_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Electric']
Psychic_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Psychic']
Ice_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Ice']
Dark_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Dark']
Fairy_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Fairy']
Dragon_Pokemon = Pokemon_Primary_Type.loc[pokemon['Primary Type'] == 'Dragon']
Number_Of_Grass_Pokemon = Grass_Pokemon.size
Number_Of_Poison_Pokemon = Poison_Pokemon.size
Number_Of_Water_Pokemon = Water_Pokemon.size
Number_Of_Fire_Pokemon = Fire_Pokemon.size
Number_Of_Normal_Pokemon = Normal_Pokemon.size
Number_Of_Fighting_Pokemon = Fighting_Pokemon.size
Number_Of_Flying_Pokemon = Flying_Pokemon.size
Number_Of_Ground_Pokemon = Ground_Pokemon.size
Number_Of_Rock_Pokemon = Rock_Pokemon.size
Number_Of_Bug_Pokemon = Bug_Pokemon.size
Number_Of_Ghost_Pokemon = Ghost_Pokemon.size
Number_Of_Steel_Pokemon = Steel_Pokemon.size
Number_Of_Electric_Pokemon = Electric_Pokemon.size
Number_Of_Psychic_Pokemon = Psychic_Pokemon.size
Number_Of_Ice_Pokemon = Ice_Pokemon.size
Number_Of_Dark_Pokemon = Dark_Pokemon.size
Number_Of_Fairy_Pokemon = Fairy_Pokemon.size
Number_Of_Dragon_Pokemon = Dragon_Pokemon.size
sizes = [Number_Of_Dragon_Pokemon, Number_Of_Fairy_Pokemon, Number_Of_Dark_Pokemon, Number_Of_Ice_Pokemon,
         Number_Of_Psychic_Pokemon, Number_Of_Steel_Pokemon, Number_Of_Electric_Pokemon, Number_Of_Ghost_Pokemon,
         Number_Of_Grass_Pokemon, Number_Of_Bug_Pokemon, Number_Of_Rock_Pokemon, Number_Of_Ground_Pokemon,
         Number_Of_Fighting_Pokemon, Number_Of_Fire_Pokemon, Number_Of_Flying_Pokemon, Number_Of_Water_Pokemon,
         Number_Of_Normal_Pokemon, Number_Of_Poison_Pokemon]
labels = ['Dragon', 'Fairy', 'Dark', 'Ice', 'Psychic', 'Steel', 'Electric', 'Ghost', 'Grass', 'Bug', 'Rock',
          'Ground', 'Fighting', 'Fire', 'Flying', 'Water', 'Normal', 'Poison']
cores = ['Indigo', 'LightPink', 'DarkSlateGray', 'Turquoise', 'Violet', 'DimGrey', 'Gold', 'MediumPurple', 'Green',
         'DarkOliveGreen', 'SaddleBrown', 'SandyBrown', 'Chocolate', 'Red', 'Plum', 'DodgerBlue', 'MintCream',
         'Purple']

if __name__ == '__main__':

    xD, Pizza = plt.subplots()
    Pizza.set_title('''Porcentagem de Pokemons de Cada Tipo
    (Levando em consideração apenas o tipo primário)''')
    Pizza.pie(sizes, colors=cores, autopct='%.1f')
    Pizza.legend(labels, title='Tipos De Pokemon', bbox_to_anchor=(1, 0, 0, 1))
    plt.show()