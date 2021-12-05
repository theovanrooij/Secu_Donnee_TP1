# Veuillez trouver un README contenant le manuel et des exemples d'utilisation sur le répo github suivant :
# https://github.com/theovanrooij/Secu_Donnee_TP1


# Q1 : A partir d'une lettre à encodée et d'une lettre issue de la clé, on réalise un décalage
# afin de changer la valeur de la lettre

from collections import deque
import string


# ALPHABETS POSSIBLE
ALPHABET_TXT = deque(string.printable[:-5] + "éèùàç" + "éèùàç".upper())
ALPHABET_HEXA = deque(["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f"])


# ALPHABET choisi. La valeur sera attribué en fonction des arguments de l'utilisateur
ALPHABET = deque()

# Liste contenant les alphabets décalés
ALPHABETS_LIST = list()

# Cette fonction permet de créée la liste de tous les alphabets décalés.
# Elle est utile pour construire les matrices de codage/décodage
def create_alphabet_list() : 
    global ALPHABETS_LIST
    ALPHABETS_LIST = [ALPHABET]
    last_alphabet = ALPHABET.copy()

    #Pour chaque lettre, on crée une copie du dernier alphabet décalé et on décale tous les caractères d'un cran vers la droite
    for i,letter in enumerate(ALPHABET) :
            last_alphabet = last_alphabet.copy()
            # On crée le décalage en supprimant le premier élément de l'alphabet (popLeft), puis en l'insérant en dernière position
            last_alphabet.insert(len(ALPHABET)-1, last_alphabet.popleft())
            ALPHABETS_LIST.append(last_alphabet)
            
# Cette fontion permet de créer le dictionnaire de codage
def create_encoder_dict():
    # On commence par créer la liste des alphabets décalés
    create_alphabet_list()
    encoder=dict()
    # Pour chaque lettre de l'alphabet choisi
    for i,letter in enumerate(ALPHABET) :
        # On fait correspondre l'alphabet de base avec le ième alphabet décalé où i correspond au numéro de la lettre dans l'alphabet
        zip_iterator = zip(ALPHABET, ALPHABETS_LIST[i])
        
        # On traduit ensuite cela en dictionnaire et on obtient finalement notre matrice de codage.
        key_to_code = dict(zip_iterator) 
        encoder[letter] = key_to_code
        # On accède donc à la lettre codé avec l'appelle suivant encoder[lettre_originale][lettre_clé]
    return encoder

# Cette fontion permet de créer le dictionnaire de décodage. Elle fonctionne dans le sens inverse de la matrice de codage
def create_decoder_dict():
    # On commence par créer la liste des alphabets décalés
    create_alphabet_list()
    decoder=dict()
    # Pour chaque lettre de l'alphabet choisi
    for i,letter in enumerate(ALPHABET) :
        # On fait correspondre  le ième alphabet décalé où i correspond au numéro de la lettre dans l'alphabet avec l'alphabet de base (sens inverse que la fonction précédente)
        zip_iterator = zip(ALPHABETS_LIST[i], ALPHABET)

        key_to_code = dict(zip_iterator) 
        decoder[letter] = key_to_code
        # On accède finalement à la lettre décodé avec l'appelle suivant encoder[lettre_clé][lettre_codé]
    return decoder

# Cette fonction permet de générer la clé de codage
# La longueur de la clé peut etre fixé dans le code
def generateKey(lengthKey=100):
    key =""
    from random import randint
    # On va venir choisir une lettre de l'alphabet au hasard autant de fois que la clé est longue
    for i in range (0,lengthKey) :
        randomIndex = randint(0,len(ALPHABET)-1)
        
        key+= ALPHABET[randomIndex]
    return key

# Permet de coder un message
def getEncodedMessage(message) : 
    key = generateKey(len(message))
    #  On fixe la taille de la clé à la taille du message
    key_len = len(key)
    mess=""

    message_len = len(message)
    affiche = False

    for i,letter in enumerate(message):
        # Pour chaque lettre a coder, on vient trouver la correspondance dans la table de codage comme expliqué dans la fonction associé
        # On rajoute un modulo pour le cas où la clé est plus courte que le message
        mess += ENCODER_DICT[letter][key[i % key_len ]]

        #Permet simplement d'afficher l'avancement tout les 10%
        # Permet de s'assurer que le programme tourne correctement
        avancement = i / message_len *100
        if  round(avancement) %10 == 0 :
            if (not affiche) :
                affiche = True
                print(round(avancement), " %")
        else : 
            affiche = False

    return mess,key



# Permet de coder un message
def getDecodedMessage(messageEncoded,key) : 
    key_len = len(key)
    mess=""
    message_len = len(messageEncoded)
    affiche = False

    for i,letter in enumerate(messageEncoded):
        # Pour chaque lettre a décoder, on vient trouver la correspondance dans la table de décodage comme expliqué dans la fonction associé
        # On rajoute un modulo pour le cas où la clé est plus courte que le message
        mess += DECODER_DICT[key[i % key_len ]][letter]

        #Permet simplement d'afficher l'avancement tout les 10%
        # Permet de s'assurer que le programme tourne correctement
        avancement = i / message_len *100
        if  round(avancement) %10 == 0 :
            if (not affiche) :
                affiche = True
                print(round(avancement), " %")
        else : 
            affiche = False

    return mess

# Cette fonction permet de s'assurer que tous les arguments nécessaire sont indiqués. Dans le cas contraire un message de rappel est affiché
def check_arguments(arguments, mode="e",type="cl") : 
    error_message = "Nombre d'arguments incorrect. Veuillez précisez : \n- Le mode d'interrection souhaité (cl pour message dans la ligne de commande OU f pour encoder un fichier)"
    error_message += "\n- Le mode souhaité (e pour encoder OU d pour décoder)\n- Le contenu à encoder/décoder (le message à encoder/décoder ou bien le nom du fichier original) "

    if mode == "e" : 
        if (not len(arguments) == 4 ):
            print(error_message)
            quit()
    elif mode =="d" :
        if (type == "f"):
            if (not len(arguments) == 7 ):
                error_message += "\n- La clé de chiffrement ou le nom du fichier la contenant si le contenu est à décoder\n-le nom du fichier dans lequel stocker le contenu décodé\n-L'alphabet à utiliser"
                print(error_message)
                quit()
            return
        if (not len(arguments) == 5 ):
            error_message += "\n- La clé de chiffrement ou le nom du fichier la contenant si le contenu est à décoder"
            print(error_message)
            quit()
    else : 
         if (not len(arguments) in [4,5,7] ):
            error_message += "\n- La clé de chiffrement ou le nom du fichier la contenant si le contenu est à décoder"
            print(error_message)
            quit()

# Permet de sauvegarder les contenus codé/décodé dans des fichiers
def saveFile(fileName, content):
    handle = open(fileName, 'w',encoding='utf-8')
    handle.write(content)
    handle.close()

if __name__ == '__main__':
    import sys

    # On s'assure que les arguments minimum sont présents
    check_arguments(sys.argv,None)

    interraction = sys.argv[1]
    mode = sys.argv[2]
    
    # Si on souhiate un codage depuis la ligne de commande on lit le message et on définit l'alphabet associé
    if interraction == "cl":
        message = sys.argv[3]
        ALPHABET = ALPHABET_TXT
    elif interraction == "f" :
        # Dans le mode par fichier, on importe seulement la fonction de codage/décodage en hexadécimale

        import fonctionsConversionFichierHexa as conv
        # read file
        pass
        
    else : 
        print("Mode non reconnu")
        quit()

    # On crée la liste contenant le décalage des alphabets
    

    if mode == "e": # On souhaite encoder le message
        check_arguments(sys.argv,"e") # On vérifie le nombre d'arguments
        
        # Si le mode en ligne de commande
        if interraction == "cl":
            # On crée la matrice d'encodage puis on encode le message que l'on sauvegarde ensuite, ainsi que la clé
            ENCODER_DICT = create_encoder_dict()
            encoded, key = getEncodedMessage(message)
            # On affiche le résultat dans le terminal
            print("Message encodé : -"+encoded+"-")
            print("Key : -"+key+"-")

            # Copier coller le résultat depuis un terminal peut poser des soucis
            saveFile("encoded_data/message_cl_encoded.txt",encoded)
            saveFile("keys/message_cl_key.txt",key)

        elif interraction == "f" :
            # Si le mode est par fichier
            # L'alphabet est l'héxadécimal
            ALPHABET = ALPHABET_HEXA
            ENCODER_DICT = create_encoder_dict()
            # On récupère le nom du fichier à encoder
            fileName = sys.argv[3]
            message = conv.fichierVersChaineHexa(fileName)
            # On traduit le contenu du fichier en héxadécimal puis on encode le contenu avant de le sauvegarder
            encoded, key = getEncodedMessage(message)
            split_fileName = fileName.split("/")[1].split('.')
            saveFile("encoded_data/"+split_fileName[0]+"_"+split_fileName[1]+"_encoded.txt", encoded)

            saveFile("keys/"+split_fileName[0]+"_"+split_fileName[1]+"_key.txt", key)
            print("Contenu Sauvegardé.")

    elif mode =="d" : # On souhaite décoder

        if interraction == "cl":
            # On vérifie le nombre d'arguments
            check_arguments(sys.argv,"d","cl")

            DECODER_DICT = create_decoder_dict() 
            # On vient charger la clé puis on affiche le message décodé
            key =sys.argv[4]

            print("Message décodé : ",getDecodedMessage(message,key))
        elif interraction == "f" : # mode par fichier

            
            # On vérifie le nombre d'arguments
            check_arguments(sys.argv,"d","f")
            # On regarde quel alpahbet a été utlisé pour encoder le fichier
            if (sys.argv[5] == "HEXA"):
                ALPHABET = ALPHABET_HEXA
            else :
                ALPHABET = ALPHABET_TXT

            # On crée la matrice de décodage
            DECODER_DICT = create_decoder_dict()    
            #On récupère les chemins des fichiers dans lesquels sont stockés la clé et le ocntenu à décoder
            pathEncoded = sys.argv[3]
            pathKey = sys.argv[4]

            # On récupère le nom du fichier dans lequel sauvegarder le contenu décodé
            pathDecoded = sys.argv[6]

            pathDecoded = "decoded_data/"+pathDecoded

            # On vient lire les différents fichiers
            file = open(pathKey, 'r')
            key = file.read()   

            file = open(pathEncoded, 'r')
            encoded = file.read()  

            # On décode les fichiers lus précédemment
            decoded = getDecodedMessage(encoded,key)

            # On vient finalement sauvegardé le contenu décodé
            if (sys.argv[5] == "HEXA"):
                # Si on avait utilisé l'alphabet hexadécimal cela signifie qu'il faut reconvertir le fichier hexa vers son format initial
                conv.chaineHexaVersFichier(decoded,pathDecoded)
            else :
                saveFile(pathDecoded,decoded)
            
            print("Contenu Décodé.")
            pass
    else :
        print("Veuillez sélectionner un mode valide parmis e (encodage) et d (décodage)")