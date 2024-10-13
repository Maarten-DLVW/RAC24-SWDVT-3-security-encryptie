# RAC24-SWDVT-3-security-encryptie
Voor dit project heb ik 2 verschillende encryptie methodes gemaakt, eentje is vrij simpel en is niet gebaseerd op een bestaande cryptographische library, de tweede is iets meer ingewikkeld.

## String encryption app
Om deze app te runnen voer je het volgende commando uit in je terminal:
```
python .\string_encryption.py
```
Je wordt dan gevraagd om het stuk tekst in te vullen wat je wil versleutelen, zodra je dit doet zal je een versleutelde string terugkrijgen.

![](/media/voorbeeld1.jpeg)

Hierna krijg je ook meteen een prompt om het versleutelde bericht weer te ontsleutelen, je kan het met de hand overtypen, of je kan het kopiëren met ctrl+c en plakken in de terminal met de rechtermuisknop.

![](/media/voorbeeld2.jpeg)

## Cryptography encryption app
Voor de tweede app zal je iets meer voorbereiding moeten doen voordat je het kan runnen, je zal eerst de benodigde libraries moeten installeren doormiddel van het volgende commando:
```
pip install -r requirements.txt
```
Zodra je dit hebt geïnstalleerd kan je de appr runnen met het volgende commando:
```
python .\cryptography_encryption.py
```
Je wordt dan gevraagd om het stuk tekst in te vullen wat je wil versleutelen, zodra je dit doet zal je een versleutelde string terugkrijgen, deze is een stuk langer dan degene die je zou krijgen bij de eerste app.

![](/media/voorbeeld3.jpeg)

Hierna krijg je ook meteen een prompt om het versleutelde bericht weer te ontsleutelen, je kan het met de hand overtypen, of je kan het kopiëren met ctrl+c en plakken in de terminal met de rechtermuisknop. Deze keer moet je wel opletten dat je **alleen** de tekst tussen de aanhalingstekens kopiëert.

![](/media/voorbeeld4.jpeg)