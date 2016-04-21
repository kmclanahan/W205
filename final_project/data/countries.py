import xml.etree.ElementTree as ET
from difflib import SequenceMatcher
import re

def similar(a, b):
    return SequenceMatcher(None, a, b).ratio()

# resolves a country name
def resolve(c):
    #remove punctuation
    c = re.sub("[,.]", "", c)
    
    # first see if any of the words in c match one of our countries
    for word in c.split():
        if word.strip() in Countries:
            return Countries[Countries.index(word)]
    
    #next see if there's a close match
    ratios = []
    for country in Countries:
        ratios.append(similar(c, country))

    return Countries[ratios.index(max(ratios))]

Countries=['Algeria','Angola','Benin','Botswana','Burkina Faso','Burundi','Cameroon',
           'Cabo Verde', 'Central African Republic','Chad','Comoros','Democratic Republic of the Congo',
           'Congo',"Cote d'Ivoire",'Djibouti','Egypt', 'Equatorial Guinea','Eritrea','Ethiopia','Gabon',
           'Gambia','Ghana','Guinea','Guinea-Bissau','Kenya','Lesotho', 'Liberia', 'Libya','Madagascar','Malawi', 
           'Mali','Mauritania','Mauritius','Morocco','Mozambique','Namibia','Niger','Nigeria',
           'Rwanda','Sao Tome and Principe','Senegal','Seychelles','Sierra Leone',
           'Somalia', 'South Africa','South Sudan','Sudan','Swaziland','Tanzania','Togo','Tunisia','Uganda','Zambia',
           'Zimbabwe']

Capitals=['Algiers','Luanda','Porto-Novo','Gaborone','Ouagadougou','Bujumbura','Yaounde','Praia','Bangui',
          'NDjamena','Moroni','Kinshasa','Brazzaville','Yamoussoukro','Djibouti','Cairo',
          'Malabo','Asmara','Addis Ababa','Libreville','Banjul','Accra','Conakry','Bissau','Nairobi','Maseru',
          'Monrovia','Tripoli','Antananarivo','Lilongwe','Bamako','Nouakchott','Port Louis','Rabat','Maputo',
          'Windhoek','Niamey','Abuja','Kigali','Sao Tome','Dakar','Victoria','Freetown','Mogadishu',
          'Cape Town','Juba','Khartoum','Lobamba','Dar es Salaam','Lome','Tunis','Kampala','Lusaka','Harare']

CountryCapitalPairs = zip(Countries, Capitals)

Misspellings = ['Sao Tome & Principe', 'So Tom and Principe', "Cte dIvoire", "Ivory Coast", 'NDjamena', 
                'Democratic Republic of Congo', 'Dar-es-Salaam', 'Mauretania', 'Maritania', 'Muaritania',
                'Burkina-Faso', 'Guinea Bissau', 'Lom', 'Arab Saharawi Democratic Republic', 'Egypt, Arab Rep.',
                'Congo, Dem. Rep.', 'Congo, Rep.', 'Congo (Republic)', 'Gambia, The', 'Congo (D. R.)', 'Egpyt',
                'Cape Verde']
Corrections = ['Sao Tome and Principe', 'Sao Tome and Principe', "Cote d'Ivoire", "Cote d'Ivoire",
               'NDjamena', 'Democratic Republic of the Congo',
               'Dar es Salaam', 'Mauritania', 'Mauritania', 'Mauritania', 'Burkina Faso', 'Guinea-Bissau', 'Lome',
               'Republic Arab Saharawi Democratic', 'Egpyt', 'Democratic Republic of the Congo', 'Congo',
               'Congo', 'Gambia', 'Democratic Republic of the Congo', 'Egypt', 'Cabo Verde']


