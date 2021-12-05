#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 06 15:05:20 2020

@author: lacombea
"""
# Librairie nécessaire pour pouvoir utiliser les fonctions ci-dessous
import binascii


###############################################
def fichierVersChaineHexa(fichier):
    """
     
    Parameters
    ----------
    fichier : string
        Un nom de fichier valide et présent sur le disque dur

    Returns
    -------
    chaine_hexa : string
        Une chaîne de caractères contenant la suite des codes hexadécimaux
        correspondant au contenu du fichier "fichier" dont le nom est 
        fourni en paramètre

    """
    handle = open(fichier, 'rb')
    octets = handle.read() 
    hexa = binascii.hexlify(octets)
    handle.close()
    chaine_hexa = hexa.decode('ascii'); 
    return chaine_hexa


###############################################
def chaineHexaVersFichier(chaineHexa, fichier):
    """
 
    Parameters
    ----------
    chaineHexa : string
        Une chaîne de caractères contenant une suite de codes hexadécimaux
        
    fichier : string
        Un nom de fichier à créer sur le disque dur dans lequel sera
        enregistré le contenu binaire correspondant à la suite de codes
        hexadécimaux composant la chaîne "chaineHexa"

    Returns
    -------
    0

    """
    handle = open(fichier, 'wb')
    hexa = chaineHexa.encode()
    octets = binascii.unhexlify(hexa)
    handle.write(octets)
    handle.close()
    return 0







