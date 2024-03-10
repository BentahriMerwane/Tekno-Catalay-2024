import csv


# Initialize lists to store the data
khw = []


with open('C:/Users/gomez/Downloads/Load_profile_10 (1).xlsx - Load Profiles.csv', 'r') as file:
    # Create a CSV reader object
    reader = csv.DictReader(file)

    for row in reader:
        chiffre_sans_virgule = (row['kWh'].replace(',', '.'))
        khw.append(float(chiffre_sans_virgule))





def function(liste):
    new_liste = []
    for i in range(int(len(liste)/4)):
        new_liste.append((liste[i] + liste[i + 1] + liste[i + 3] + liste[i + 4])/4)
    return new_liste


new_KWH = function(khw)