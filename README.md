
# Sécurité des données - TP 1 - Chiffre de Vigenère

  

## 1. Mode d'emploi

Le programme vigener.py possède deux modes différents : codage et décodage. Le mode souhaité est précisé dans les arguments.

  

En plus de ces deux modes, vous pouvez choisir de coder/décoder un contenu passé directement dans les arguments du programme ou bien un fichier, auquel cas vous précisez le nom du fichier en question. La syntaxe, sous windows, est donc la suivante :

  

> python vigener.py typeContenu mode contenu potentielleClé alphabet

potentielFichierStockage

  

- typeContenu prend les valeurs suivantes :

	--'cl' pour un contenu passé dans les arguments de la ligne de commande

	--'f' si le contenu est un fichier

- mode prend les valeurs suivantes :

	-- 'd' pour décoder

	-- 'e' pour coder

- potentielleClé contient soit la clé permettant de décoder le précédent message ou le chemin du fichier la contenant. Ce paramètre n'est nécessaire que si le mode est 'd' (décodage)

- alphabet précise avec quel alphabet le contenu a été codé prend les valeurs suivantes :
-- 'HEXA' pour un contenu encodé uniquement en hexadecimal
-- 'ALL' pour décoder tous type de caractère- contenu contient soit le message à coder/décoder ou le chemin du fichier le contenant


- potentielFichierStockage contient le chemin dans lequel stocké le message décodé


  

## 2. Exemples d'utilisation

  

### 2.1 Coder un message depuis le terminal

Nous souhaitons coder le message " Sécurité des données "

> python .\vigener.py cl e "Sécurité des données"

>  > Message encodé : -TB9%y#aq}(L{>- i>!e-

>  > Key : -1LÙA7K]AÀUx!}Z)*É|M|-

  

Il faut supprimer les deux tirets à la fin de la clé et du message afin d'obtenir la vraie valeur. Les tirets sont utilisés comme délimiteur afin de ne pas louper un espace qui serait placé au début ou à la fin de la chaîne de caractère.

En plus de l'affichage dans le terminal, le contenu codé est sauvegardé à l'adresse suivante :

> ./encoded_data\message_cl_encoded.txt

  

La clé est sauvegardé dans le fichier suivant :

> ./keys\message_cl_key.txt

  

### 2.2 Décoder un message depuis le terminal

  
  

Nous souhaitons décoder le message précédent depuis le terminal, avec les valeurs de clés et de contenu codé retourné par la partie précédente

  

>python .\vigener.py cl d "TB9%y#aq}(L{>- i>!e" "1LÙA7K]AÀUx!}Z)*É|M|"

>>Message décodé : Sécurité des données

  

Malheureusement certains caractères sont mal interprétés par un terminal et sont mal transmis au code python. Nous préférons ainsi utiliser le décodage depuis un fichier, d'où la sauvegarde à la fin d'un codage.

  

### 2.3 Coder un fichier

  

- **Lorsque vous précisez le chemin, veuillez à remplacer les potentiels " \ " généré par Windows par des " / " afin d'éviter des soucis de sauvegarde ou lecture de fichier.**

  
  

Le fichier que je souhaite coder se trouve à l'adresse suivante :

- "original_data/Flaubert - Bouvard et Pecuchet.txt"

  

La commande pour coder ce fichier est donc :

> python .\vigener.py f e "original_data/Flaubert - Bouvard et Pecuchet.txt"

  

Le contenu codé et la clé sont ensuite sauvegardés dans les fichiers suivants :

  

- encoded_data\nomFichier_extension_encoded.txt

-- Dans notre cas : encoded_data\Flaubert - Bouvard et Pecuchet_txt_encoded.txt

  

- keys\nomFichier_extension_key.txt

-- Dans notre cas : keys\Flaubert - Bouvard et Pecuchet_txt_key.txt

  

### 2.4 Décoder un fichier

  

#### 2.4.1. Message codé dans la partie 2.1

Comme expliqué précédemment, nous avons sauvegardé le message codé depuis le terminal dans un fichier afin d'éviter des pertes de caractère entre le terminal et le programme python. Pour le décoder, la commande est la suivante :
On précise que l'alphabet vaut ALL car c'est l'alphabet utilisé par la partie 2.1

> python .\vigener.py f d "encoded_data\message_cl_encoded.txt" "keys\message_cl_key.txt" ALL "message_cl_decoded.txt"

  

Le fichier décodé est placé dans le dossier " decoded_data "

####  2.4.2. Fichier codé dans la partie 2.3

  

Nous allons maintenant décodé un le fichier "original_data/Flaubert - Bouvard et Pecuchet.txt" qui a été codé précédemment. L'alphabet à utiliser est l'hexadécimal, on le précise donc dans les arguments.

  

> python .\vigener.py f d "encoded_data\Flaubert - Bouvard et Pecuchet_txt_encoded.txt" "keys\Flaubert - Bouvard et Pecuchet_txt_key.txt" HEXA "Flaubert - Bouvard et Pecuchet.txt"

  

Comme précédemment, le fichier décodé est placé dans le dossier " decoded_data "
