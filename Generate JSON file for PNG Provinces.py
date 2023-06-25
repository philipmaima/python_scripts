"""
Author: Philip Maima
Date Created: Sunday 25 June 2023
Title: Generate JSON file for PNG Provinces & Districts

This python script generates a JSON file for provinces and districts in Papua New Guinea.
In this script,the data structure is defined using nested dictionaries and lists to represent the provinces and their respective districts. 
The script then writes the data to a JSON file named "papua_new_guinea_provinces_and_districts.json" with an indentation level of 4 for better readability.

"""

import json

data = {
    "provinces": [
        {
            "name": "Simbu",
            "districts": [
                "Chuave",
                "Gumine",
                "Kerowagi",
				"Kundiawa-Gembogl",
				"Salt-Nomane-Karimui",
				"Sinasina-Yonggomugl"
            ]
        },
        {
            "name": "Eastern Highlands",
            "districts": [
                "Daulo",
                "Goroka",
                "Henganofi",   
				"Kainantu",
				"Lufa",
				"Obura-Wonenara",
				"Okapa",				
				"Unggai-Bena"
            ]
        },
        {
            "name": "Enga",
            "districts": [
                "Kandep",
				"Kompiam-Ambum",
				"Lagaip",
				"Porgera-Paiela",
				"Wabag",
				"Wapenamanda"
            ]
        },
        {
            "name": "Southern Highlands",
            "districts": [                
                "Ialibu-Pangia",
                "Imbonggu",
                "Kagua-Erave",
				"Mendi-Munihu",
				"Nipa-Kutubu"
            ]
        },
        {
            "name": "Western Highlands",
            "districts": [                
                "Dei",
				"Mt Hagen Central",
                "Mul-Baiyer",
				"Tambul-Nebilyer"
            ]
        },
        {
            "name": "Hela",
            "districts": [
				"Komo-Hulia",
				"Koroba-Kopiago",
                "Magarima",               
				"Tari-Pori"
            ]
        },
        {
            "name": "Jiwaka",
            "districts": [
                "Anglimp-South Waghi",
                "Jimi",
                "North Waghi"
            ]
        },
        {
            "name": "Manus",
            "districts": [
                "Manus"
            ]
        },
        {
            "name": "New Ireland",
            "districts": [
                "Kavieng",
                "Namatanai"
            ]
        },
		        {
            "name": "Bougainville",
            "districts": [
                "Central Bougainville",
                "North Bougainville",
                "South Bougainville"
            ]
        },
        {
            "name": "East New Britain",
            "districts": [
				"Gazelle",
                "Kokopo",            
                "Pomio",
				"Rabaul"
            ]
        },
        {
            "name": "West New Britain",
            "districts": [
                "Kandrian-Gloucester",
                "Nakani",
                "Talasea"
            ]
        },
        {
            "name": "West Sepik",
            "districts": [
                "Aitape-Lumi",
                "Nuku",
                "Telefomin",
                "Vanimo"
            ]
        },
        {
            "name": "East Sepik",
            "districts": [
                    "Ambunti-Dreikikier",
					"Angoram",
					"Maprik",
					"Wewak",
					"Wosera-Gawi",
					"Yangoru-Saussia"
            ]
        },
        {
            "name": "Madang",
            "districts": [
                "Manus"
				"Bogia",
				"Madang",
				"Middle Ramu",
				"Rai Coast",
				"Sumkar",
				"Usino Bundi"
            ]
        },
		{
            "name": "Morobe",
            "districts": [
				"Finschhafen",
				"Huon Gulf",
				"Kabwum",
				"Lae",
				"Markham",
				"Menyamya",
				"Nawae",
				"Tewae-Siassi",
				"Bulolo",
				"Wau-Waria"
            ]
        },
        {
            "name": "Central",
            "districts": [
				"Abau", 
				"Goilala",
				"Kairuku",
				"Hiri-Koiari",
				"Rigo"
            ]
        },
        {
            "name": "Gulf",
            "districts": [
                "Kerema",
				"Kikori"
            ]
        },
        {
            "name": "Milne Bay",
            "districts": [                
                "Alotau",
                "Esa'ala",
                "Kiriwina-Goodenough",
				"Samarai-Murua"
            ]
        },
        {
            "name": "Oro",
            "districts": [                
                "Ijivitari",
				"Popondetta",
                "Sohe"
            ]
        },
        {
            "name": "Western",
            "districts": [
				"Delta Fly",
				"Middle Fly",
                "North Fly",               
				"South Fly"
            ]
        },
        {
            "name": "National Capital District",
            "districts": [
                "Port Moresby North-East",
                "Port Moresby North-West",
                "Port Moresby South"
            ]
        }
    ]
}

# Writing the data to a JSON file
with open("papua_new_guinea_provinces_and_districts.json", "w") as file:
    json.dump(data, file, indent=4)
