import os
import numpy as np
from keras.preprocessing.image import ImageDataGenerator, load_img, img_to_array
from keras.models import Sequential, load_model

img_width, img_height = 150,150
model_path = 'C:/Users/dell/Desktop/AIrizal/models/model.h5'
model_weights_path = 'C:/Users/dell/Desktop/AIrizal/models/weights.h5'
model = load_model(model_path)
model.load_weights(model_weights_path)

def predict(file):
  x = load_img(file, target_size=(img_width,img_height))
  x = img_to_array(x)
  x = np.expand_dims(x, axis=0)
  array = model.predict(x)
  result = array[0]
  answer = np.argmax(result)
  
  if answer == 0:
    print("Label: Antipolo Cathedral")
  elif answer == 1:
    print("Label: Bulawan Floating Restaurant")
  elif answer == 2:
    print("Label: Celossian Flower Farm")
  elif answer == 3:
    print("Label: Cloud 9")
  elif answer == 4:
    print("Label: Coffee Rush")
  elif answer == 5:
    print("Label: Daraitan")
  elif answer == 6:
    print("Label: Daranak")
  elif answer == 7:
    print("Label: Dinasaur Park")
  elif answer == 8:
    print("Label: Diocesan Shrine of Our Lady of Arazanzu")
  elif answer == 9:
    print("Label: Jardin De Miramar")
  elif answer == 10:
    print("Label: Kasarinlan Park")
  elif answer == 11:
    print("Label: Lakeside Park")
  elif answer == 12:
    print("Label: Marian Hill")
  elif answer == 13:
    print("Label: Masungi Georeserve")
  elif answer == 14:
    print("Label: Mount Calvary")
  elif answer == 15:
    print("Label: Our Lady of Light")
  elif answer == 16:
    print("Label: Our Lady of the Holy Rosary")
  elif answer == 17:
    print("Label: Our Lady of the Most Holy Rosary")
  elif answer == 18:
    print("Label: Light House (Parola)")
  elif answer == 19:
    print("Label: Petroglyphs")
  elif answer == 20:
    print("Label: Pinto Art Museum")
  elif answer == 21:
    print("Label: Puente Del Diablo")
  elif answer == 22:
    print("Label: Rambulls Bakahan")
  elif answer == 23:
    print("Label: Regina Rica")
  elif answer == 24:
    print("Label: Rock Garden")
  elif answer == 25:
    print("Label: Saint Joseph Parish Church")
  elif answer == 26:
    print("Label: Saint Clement Parish Church")
  elif answer == 27:
    print("Label: Saint Jerome Parish Church")
  elif answer == 28:
    print("Label: Saint Mary Magdalene Parish Church")
  elif answer == 29:
    print("Label: Saint Rose of Lima Parish Church")
  elif answer == 30:
    print("Label: San Idelfonso Parish Church")
  elif answer == 31:
    print("Label: Saint John Parish Church")
  elif answer == 32:
    print("Label: Sta Ursula Parish Church")
  elif answer == 33:
    print("Label: Tungtong Falls")
  elif answer == 34:
    print("Label: Wawa Dam")
  elif answer == 35:
    print("Label: Pililia Windmill")

  return answer

AntipoloCathedral_t = 0
AntipoloCathedral_f = 0

BulawanFloating_t = 0
BulawanFloating_f = 0

CelossianFlowerFarm_t = 0
CelossianFlowerFarm_f = 0

Cloud9_t = 0
Cloud9_f = 0

CoffeeRush_t = 0
CoffeeRush_f = 0

Daraitan_t = 0
Daraitan_f = 0

Daranak_t = 0
Daranak_f = 0

DinasaurPark_t = 0
DinasaurPark_f = 0

Arazanzu_t = 0
Arazanzu_f = 0

Jardin_t = 0
Jardin_f = 0

KasarinlanPark_t = 0
KasarinlanPark_f = 0

Lakeside_t = 0
Lakeside_f = 0

Marianhill_t = 0
Marianhill_f = 0

MasungiGeoreserve_t = 0
MasungiGeoreserve_f = 0

MtCalvary_t = 0
MtCalvary_f = 0

OurLadyOfLight_t = 0
OurLadyOfLight_f = 0

OurLadyOfTheHolyRosary_t = 0
OurLadyOfTheHolyRosary_f = 0

OurLadyOfTheMostHolyRosary_t = 0
OurLadyOfTheMostHolyRosary_f = 0

Parola_t = 0
Parola_f = 0

Petroglyphs_t = 0
Petroglyphs_f = 0

Pintoart_t = 0
Pintoart_f = 0

PuenteDelDiablo_t = 0
PuenteDelDiablo_f = 0

Rambulls_t = 0
Rambulls_f = 0

ReginaRica_t = 0
ReginaRica_f = 0

RockGarden_t = 0
RockGarden_f = 0

StJoseph_t = 0
StJoseph_f = 0

StClement_t = 0
StClement_f = 0

StJerome_t = 0
StJerome_f = 0

StMary_t = 0
StMary_f = 0

StRose_t = 0
StRose_f = 0

SanIdelfonso_t = 0
SanIdelfonso_f = 0

StJohn_t = 0
StJohn_f = 0

StaUrsula_t = 0
StaUrsula_f = 0

TungtongFalls_t = 0
TungtongFalls_f = 0

WawaDam_t = 0
WawaDam_f = 0

Windmill_t = 0
Windmill_f = 0



for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/AntipoloCathedral')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 0:
      AntipoloCathedral_t += 1
    else:
      AntipoloCathedral_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/BulawanFloating')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 1:
      BulawanFloating_t += 1
    else:
      BulawanFloating_f += 1
      
for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/CelossianFlowerFarm')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 2:
      CelossianFlowerFarm_t += 1
    else:
      CelossianFlowerFarm_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Cloud9')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 3:
      print(ret[0] + '/' + filename)
      Cloud9_t += 1
    else:
      Cloud9_f += 1
     
for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/CoffeeRush')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 4:
      print(ret[0] + '/' + filename)
      CoffeeRush_t += 1
    else:
      CoffeeRush_f += 1

      
for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Daraitan')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 5:
      print(ret[0] + '/' + filename)
      Daraitan_t += 1
    else:
      Daraitan_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Daranak')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 6:
      print(ret[0] + '/' + filename)
      Daranak_t += 1
    else:
      Daranak_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/DinasaurPark')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 7:
      print(ret[0] + '/' + filename)
      DinasaurPark_t += 1
    else:
      DinasaurPark_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Arazanzu')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    result = predict(ret[0] + '/' + filename)
    if result == 8:
      print(ret[0] + '/' + filename)
      Arazanzu_t += 1
    else:
      Arazanzu_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Jardin')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 9:
      print(ret[0] + '/' + filename)
      Jardin_t += 1
    else:
      Jardin_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/KasarinlanPark')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 10:
      print(ret[0] + '/' + filename)
      KasarinlanPark_t += 1
    else:
      KasarinlanPark_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Lakeside')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 11:
      print(ret[0] + '/' + filename)
      Lakeside_t += 1
    else:
      Lakeside_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/MarianHill')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 12:
      print(ret[0] + '/' + filename)
      Marianhill_t += 1
    else:
      Marianhill_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/MasungiGeoreserve')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 13:
      print(ret[0] + '/' + filename)
      MasungiGeoreserve_t += 1
    else:
      MasungiGeoreserve_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/MtCalvary')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 14:
      print(ret[0] + '/' + filename)
      MtCalvary_t += 1
    else:
      MtCalvary_f += 1
      
for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/OurLadyOfLight')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 15:
      print(ret[0] + '/' + filename)
      OurLadyOfLight_t += 1
    else:
      OurLadyOfLight_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/OurLadyOfTheHolyRosary')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 16:
      print(ret[0] + '/' + filename)
      OurLadyOfTheHolyRosary_t  += 1
    else:
      OurLadyOfTheHolyRosary_f += 1      

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/OurLadyOfTheMOSTHolyRosary')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 17:
      print(ret[0] + '/' + filename)
      OurLadyOfTheMostHolyRosary_t += 1
    else:
      OurLadyOfTheMostHolyRosary_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Parola')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 18:
      print(ret[0] + '/' + filename)
      Parola_t  += 1
    else:
      Parola_f += 1   

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Petroglyphs')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 19:
      print(ret[0] + '/' + filename)
      Petroglyphs_t += 1
    else:
      Petroglyphs_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Pintoart')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 20:
      print(ret[0] + '/' + filename)
      Pintoart_t  += 1
    else:
      Pintoart_f += 1 

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/PUENTEDELDIABLO')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 21:
      print(ret[0] + '/' + filename)
      PuenteDelDiablo_t += 1
    else:
      PuenteDelDiablo_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Rambulls')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 22:
      print(ret[0] + '/' + filename)
      Rambulls_t  += 1
    else:
      Rambulls_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/ReginaRica')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 23:
      print(ret[0] + '/' + filename)
      ReginaRica_t += 1
    else:
      ReginaRica_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/RockGarden')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 24:
      print(ret[0] + '/' + filename)
      RockGarden_t  += 1
    else:
      RockGarden_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StJoseph')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 25:
      print(ret[0] + '/' + filename)
      StJoseph_t += 1
    else:
      StJoseph_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StClement')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 26:
      print(ret[0] + '/' + filename)
      StClement_t  += 1
    else:
      StClement_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StJerome')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 27:
      print(ret[0] + '/' + filename)
      StJerome_t += 1
    else:
      StJerome_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StMary')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 28:
      print(ret[0] + '/' + filename)
      StMary_t  += 1
    else:
      StMary_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StRose')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 29:
      print(ret[0] + '/' + filename)
      StRose_t += 1
    else:
      StRose_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/SanIdelfonso')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 30:
      print(ret[0] + '/' + filename)
      SanIdelfonso_t  += 1
    else:
      SanIdelfonso_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StJohn')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 31:
      print(ret[0] + '/' + filename)
      StJohn_t += 1
    else:
      StJohn_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/StaUrsula')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 32:
      print(ret[0] + '/' + filename)
      StaUrsula_t  += 1
    else:
      StaUrsula_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/TungtongFalls')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue
    #print("Label: Sunflower")
    result = predict(ret[0] + '/' + filename)
    if result == 33:
      print(ret[0] + '/' + filename)
      TungtongFalls_t += 1
    else:
      TungtongFalls_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/WawaDam')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 34:
      print(ret[0] + '/' + filename)
      WawaDam_t  += 1
    else:
      WawaDam_f += 1

for i, ret in enumerate(os.walk('C:/Users/dell/desktop/AIrizal/test-data/Windmill')):
  for i, filename in enumerate(ret[2]):
    if filename.startswith("."):
      continue

    result = predict(ret[0] + '/' + filename)
    if result == 35:
      print(ret[0] + '/' + filename)
      Windmill_t  += 1
    else:
      Windmill_f += 1   
      
"""
Check metrics
"""
print("True AntipoloCathedral: ", AntipoloCathedral_t)
print("False AntipoloCathedral: ", AntipoloCathedral_f)

print("True BulawanFloating: ", BulawanFloating_t)
print("False BulawanFloating: ", BulawanFloating_f)

print("True CelossianFlowerFarm: ", CelossianFlowerFarm_t)
print("False CelossianFlowerFarm: ",CelossianFlowerFarm_f)

print("True Cloud9: ",  Cloud9_t)
print("False Cloud9: ",  Cloud9_f)

print("True CoffeeRush: ",  CoffeeRush_t)
print("False CoffeeRush: ",  CoffeeRush_f)

print("True Daraitan: ", Daraitan_t)
print("False Daraitan: ", Daraitan_f)

print("True Daranak: ", Daranak_t)
print("False Daranak: ", Daranak_f)

print("True DinasaurPark: ",  DinasaurPark_t)
print("False DinasaurPark: ",  DinasaurPark_f)

print("True Arazanzu: ",  Arazanzu_t)
print("False Arazanzu: ", Arazanzu_f)

print("True Jardin: ", Jardin_t)
print("False Jardin: ",Jardin_f)

print("True KasarinlanPark: ",  KasarinlanPark_t)
print("False KasarinlanPark: ",  KasarinlanPark_f)

print("True Lakeside: ", Lakeside_t)
print("False Lakeside: ", Lakeside_f)

print("True Marianhill: ", Marianhill_t)
print("False Marianhil: ", Marianhill_f)

print("True MasungiGeoreserve: ",  MasungiGeoreserve_t)
print("False MasungiGeoreserve: ", MasungiGeoreserve_f)

print("True MtCalvary: ", MtCalvary_t)
print("False MtCalvary: ",MtCalvary_f)

print("True OurLadyOfLight: ",  OurLadyOfLight_t)
print("False OurLadyOfLight: ",  OurLadyOfLight_f)

print("True OurLadyOfTheHolyRosary: ", OurLadyOfTheHolyRosary_t)
print("False OurLadyOfTheHolyRosary: ", OurLadyOfTheHolyRosary_f)

print("True OurLadyOfTheMostHolyRosary: ", OurLadyOfTheMostHolyRosary_t)
print("False OurLadyOfTheMostHolyRosary: ", OurLadyOfTheMostHolyRosary_f)

print("True Parola: ", Parola_t)
print("False Parola: ",Parola_f)

print("True Petroglyphs: ",  Petroglyphs_t)
print("False Petroglyphs: ",  Petroglyphs_f)

print("True Pintoart: ", Pintoart_t)
print("False Pintoart: ", Pintoart_f)

print("True PuenteDelDiablo: ", PuenteDelDiablo_t)
print("False PuenteDelDiablo: ", PuenteDelDiablo_f)

print("True Rambulls: ",  Rambulls_t)
print("False Rambulls: ", Rambulls_f)

print("True ReginaRica: ", ReginaRica_t)
print("False ReginaRica: ",ReginaRica_f)

print("True RockGarden: ",  RockGarden_t)
print("False RockGarden: ",  RockGarden_f)

print("True StJoseph: ", StJoseph_t)
print("False StJoseph: ", StJoseph_f)

print("True StJerome: ", StJerome_t)
print("False StJerome: ", StJerome_f)

print("True StMary: ",  StMary_t)
print("False StMary: ",  StMary_f)

print("True StRose: ", StRose_t)
print("False StRose: ", StRose_f)

print("True SanIdelfonso: ", SanIdelfonso_t)
print("False SanIdelfonso: ", SanIdelfonso_f)

print("True StJohn: ",  StJohn_t)
print("False StJohn: ", StJohn_f)

print("True StaUrsula: ", StaUrsula_t)
print("False StaUrsula: ",StaUrsula_f)

print("True TungtongFalls: ",  TungtongFalls_t)
print("False TungtongFalls: ",  TungtongFalls_f)

print("True Wawa dam: ",  WawaDam_t)
print("False Wawa dam: ",  WawaDam_f)

print("True Windmill: ", Windmill_t)
print("False Windmill: ", Windmill_f)
