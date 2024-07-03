from flask import Flask, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)

CORS(app)
results = [
    {
          "group": "A",
          "team": "Netherlands",
          "points": 7,
          "matchesT":3,
          "matchesW":2,
          "matchesD":1,
          "matchesL":0,
          "goalsFor": 5,
          "goalsAgainst": 1,
          "goalDifference": 4,
      },
      {
          "group": "A",
          "team": "Senegal",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 5,
          "goalsAgainst": 4,
          "goalDifference": 1,
      },
      {
          "group": "A",
          "team": "Ecuador",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 3,
          "goalDifference": 1,
      },
      {
          "group": "A",
          "team": "Qatar",
          "points": 9,
          "matchesT":3,
          "matchesW":0,
          "matchesD":0,
          "matchesL":3,
          "goalsFor": 1,
          "goalsAgainst": 7,
          "goalDifference": -6,
      },
      
      {
          "group": "B",
          "team": "England",
          "points": 7,
          "matchesT":3,
          "matchesW":2,
          "matchesD":1,
          "matchesL":0,
          "goalsFor": 9,
          "goalsAgainst": 2,
          "goalDifference": 7,
      },
      {
          "group": "B",
          "team": "USA",
          "points": 5,
          "matchesT":3,
          "matchesW":1,
          "matchesD":2,
          "matchesL":0,
          "goalsFor": 2,
          "goalsAgainst": 1,
          "goalDifference": 1,
      },
      {
          "group": "B",
          "team": "Iran",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 4,
          "goalsAgainst": 7,
          "goalDifference": -3,
      },
      {
          "group": "B",
          "team": "Wales",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 1,
          "goalsAgainst": 6,
          "goalDifference": -5,
      },
      
      {
          "group": "C",
          "team": "Argentina",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":1,
          "matchesL":0,
          "goalsFor": 5,
          "goalsAgainst": 2,
          "goalDifference": 3,
      },
      {
          "group": "C",
          "team": "Poland",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 2,
          "goalsAgainst": 2,
          "goalDifference": 0,
      },
      
      {
          "group": "C",
          "team": "Mexico",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 2,
          "goalsAgainst": 3,
          "goalDifference": -1,
      },
      
      {
          "group": "C",
          "team": "Saudi Arabia",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 3,
          "goalsAgainst": 5,
          "goalDifference": -2,
      },

       {
          "group": "D",
          "team": "France",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":1,
          "matchesL":0,
          "goalsFor": 6,
          "goalsAgainst": 3,
          "goalDifference": 3,
      },
      {
          "group": "D",
          "team": "Australia",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 3,
          "goalsAgainst": 4,
          "goalDifference": -1,
      },
      {
          "group": "D",
          "team": "Tunisia",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 1,
          "goalsAgainst": 1,
          "goalDifference": 0,
      },
      {
          "group": "D",
          "team": "Denmark",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 1,
          "goalsAgainst": 3,
          "goalDifference": -2,
      },
      {
          "group": "E",
          "team": "Japan",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 3,
          "goalDifference": 1,
      },
      {
          "group": "E",
          "team": "Spain",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 9,
          "goalsAgainst": 3,
          "goalDifference": 6,
      },
      {
          "group": "E",
          "team": "Germany",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 6,
          "goalsAgainst": 5,
          "goalDifference": 1,
      },
      {
          "group": "E",
          "team": "Costa Rica",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 3,
          "goalsAgainst": 11,
          "goalDifference": -8,
      },
      {
          "group": "F",
          "team": "Morocco",
          "points": 7,
          "matchesT":3,
          "matchesW":2,
          "matchesD":1,
          "matchesL":0,
          "goalsFor": 4,
          "goalsAgainst": 1,
          "goalDifference": 3,
      },
      {
          "group": "F",
          "team": "Croatia",
          "points": 5,
          "matchesT":3,
          "matchesW":1,
          "matchesD":2,
          "matchesL":0,
          "goalsFor": 4,
          "goalsAgainst": 1,
          "goalDifference": 3,
      },
      {
          "group": "F",
          "team": "Belgium",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 1,
          "goalsAgainst": -2,
          "goalDifference": 3,
      },
      {
          "group": "F",
          "team": "Canada",
          "points": 0,
          "matchesT":3,
          "matchesW":0,
          "matchesD":0,
          "matchesL":3,
          "goalsFor": 2,
          "goalsAgainst": 7,
          "goalDifference": -5,
      },
      {
          "group": "G",
          "team": "Brazil",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 6,
          "goalsAgainst": 2,
          "goalDifference": 4,
      },
      {
          "group": "G",
          "team": "Switzerland",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 3,
          "goalDifference": 1,
      },
      
      {
          "group": "G",
          "team": "Cameroon",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 4,
          "goalDifference": 0,
      },

      {
          "group": "G",
          "team": "Serbia",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 8,
          "goalDifference": -3,
      },
      {
          "group": "H",
          "team": "Portugal",
          "points": 6,
          "matchesT":3,
          "matchesW":2,
          "matchesD":0,
          "matchesL":1,
          "goalsFor": 6,
          "goalsAgainst": 4,
          "goalDifference": 2,
      },
      {
          "group": "H",
          "team": "South Korea",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 4,
          "goalDifference": 0,
      },
      {
          "group": "H",
          "team": "Uruguay",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 2,
          "goalsAgainst": 2,
          "goalDifference": 0,
      },
      {
          "group": "H",
          "team": "Ghana",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 2,
          "goalsAgainst": 5,
          "goalDifference": -2,
      },
  
    ]


fino = {
  
          "resultados1": {"round": "Round of 16",
          "match": {
            "win":"Netherlands",
            "loser":"United States",
            "scoreW":3,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Depay","Blind","Dumfries" 
            ],
            "TimescoredW":[
             10,45,81 
            ],
            "scoreL":["Wright"],
            "TimescoredL":[76],

          },
        }
  
    ,"resultados2": {"round": "Round of 16",
          "match": {
            "win":"Argentina",
            "loser":"Australia",
            "scoreW":2,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Messi","Alvarez" 
            ],
            "TimescoredW":[
             35,57 
            ],
            "scoreL":["(OG)"],
            "TimescoredL":[77],

          },
        },


        "resultados3": {"round": "Round of 16",
          "match": {
            "win":"France",
            "loser":"Poland",
            "scoreW":3,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Giroud","Mbappe","Mbappe" 
            ],
            "TimescoredW":[
             44,74,91 
            ],
            "scoreL":["Lewandowski"],
            "TimescoredL":[99],

          },
        },


                "resultados4": {"round": "Round of 16",
          "match": {
            "win":"England",
            "loser":"Senegal",
            "scoreW":3,
            "scoreL":0,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Henderson","Kane","Saka" 
            ],
            "TimescoredW":[
             38,45,57 
            ],
            "scoreL":[],
            "TimescoredL":[],

          },
        },


        "resultados5": {"round": "Round of 16",
          "match": {
            "win":"Croatia",
            "loser":"Japan",
            "scoreW":1,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Perisic" 
            ],
            "TimescoredW":[
             55 
            ],
            "scoreL":["Maeda"],
            "TimescoredL":[43],
          },
        },

        "resultados6": {"round": "Round of 16",
          "match": {
            "win":"Brazil",
            "loser":"South Korea",
            "scoreW":4,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[
             "Vinicius Junior", "Neymar", "Richarlison", "Paqueta" 
            ],
            "TimescoredW":[
             7,13,29,36 
            ],
            "scoreL":["Paik Seung-ho"],
            "TimescoredL":[76],
          },
        },
        "resultados7": {"round": "Round of 16",
          "match": {
            "win":"Morocco",
            "loser":"Spain",
            "scoreW":0,
            "scoreL":0,
            "flagW":"url",
            "flagL":"url",
            "scoredW":[],
            "TimescoredW":[],
            "scoreL":[],
            "TimescoredL":[],
          },
        },
        

        "resultados8": {"round": "Round of 16",
          "match": {
            "win":"Portugal",
            "loser":"Switzerland",
            "scoreW":6,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Ramos","Ramos","Ramos", "Pepe","Guerreiro", "Leao"],
            "TimescoredW":[17,51,67,33,55,92],
            "scoreL":["Akanji"],
            "TimescoredL":[58],
          },
        },

        "resultados9": {"round": "Quarter-finals",
          "match": {
            "win":"Argentina",
            "loser":"Netherlands",
            "scoreW":2,
            "scoreL":2,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Molina","Messi"],
            "TimescoredW":[35,73],
            "scoreL":["Weghorst"],
            "TimescoredL":[83,101],
          },
        },

        "resultados10": {"round": "Quarter-finals",
          "match": {
            "win":"Morocco",
            "loser":"Portugal",
            "scoreW":1,
            "scoreL":0,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["En-Nesyri"],
            "TimescoredW":[42],
            "scoreL":[],
            "TimescoredL":[],
          },
        },

        "resultados11": {"round": "Quarter-finals",
          "match": {
            "win":"Croatia",
            "loser":"Brazil",
            "scoreW":1,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Kramaric"],
            "TimescoredW":[42],
            "scoreL":["Neymar"],
            "TimescoredL":[78],
          },
        },

        "resultados12": {"round": "Quarter-finals",
          "match": {
            "win":"France",
            "loser":"England",
            "scoreW":2,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Tchouaméni","Giroud"],
            "TimescoredW":[17,78],
            "scoreL":["Kane"],
            "TimescoredL":[54],
          },
        },

        "resultados13": {"round": "Semi-finals",
          "match": {
            "win":"Argentina",
            "loser":"Croatia",
            "scoreW":3,
            "scoreL":0,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Messi","Alvarez","Alvarez"],
            "TimescoredW":[34,39,69],
            "scoreL":[],
            "TimescoredL":[],
          },
        },

        "resultados14": {"round": "Semi-finals",
          "match": {
            "win":"France",
            "loser":"Morocco",
            "scoreW":2,
            "scoreL":0,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Hernandez","Kolo Muani"],
            "TimescoredW":[5,79],
            "scoreL":[],
            "TimescoredL":[],
          },
        },
        
        "resultados15": {"round": "Third place play-off",
          "match": {
            "win":"Croatia",
            "loser":"Morocco",
            "scoreW":2,
            "scoreL":1,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Gvardiol","Orsic"],
            "TimescoredW":[34,39,69],
            "scoreL":["Dari"],
            "TimescoredL":[9],
        },
          },
        

        "resultados16": {"round": "Final",
          "match": {
            "win":"Argentina",
            "loser":"France",
            "scoreW":3,
            "scoreL":3,
            "flagW":"url",
            "flagL":"url",
            "scoredW":["Messi","Di Maria","Messi"],
            "TimescoredW":[23,36,108],
            "scoreL":["Mbappe","Mbappe","Mbappe"],
            "TimescoredL":[80,81,118],
        },
          },
        },


topscorers = [
        {"name": "Kylian Mbappé", "goals": 8},
        {"name": "Lionel Messi", "goals": 7},
        {"name": "Julián Álvarez", "goals": 4},
        {"name": "Olivier Giroud", "goals": 4},
        {"name": "Neymar", "goals": 3},
    ]

top_assistants = [
        {"name": "Lionel Messi", "assists": 3},
        {"name": "Bruno Fernandes", "assists": 3},
        {"name": "Antoine Griezmann", "assists": 3},
        {"name": "Harry Kane", "assists": 3},
        {"name": "Ivan Perišić", "assists": 3},
    ]

#general results

final_results = [
    {
          "team": "Argentina",
          "points": 14,
          "matchesT":7,
          "matchesW":4,
          "matchesD":2,
          "matchesL":1,
          "goalsFor": 15,
          "goalsAgainst": 8,
          "goalDifference": 7,
      },
      
      {
          "team": "France",
          "points": 16,
          "matchesT":7,
          "matchesW":5,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 16,
          "goalsAgainst": 8,
          "goalDifference": 8,
      },

      {
          "team": "Croatia",
          "points": 10,
          "matchesT":7,
          "matchesW":2,
          "matchesD":4,
          "matchesL":1,
          "goalsFor": 8,
          "goalsAgainst": 7,
          "goalDifference": 1,
      },
      
      {
          "team": "Morocco",
          "points": 11,
          "matchesT":7,
          "matchesW":3,
          "matchesD":2,
          "matchesL":2,
          "goalsFor": 6,
          "goalsAgainst": 5,
          "goalDifference": 1,
      },

      {
          "team": "Netherlands",
          "points": 11,
          "matchesT":5,
          "matchesW":3,
          "matchesD":2,
          "matchesL":0,
          "goalsFor": 10,
          "goalsAgainst": 4,
          "goalDifference": 6,
      },
      {
          "team": "England",
          "points": 10,
          "matchesT":5,
          "matchesW":3,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 13,
          "goalsAgainst": 4,
          "goalDifference": 9,
      },

      {
          "team": "Brazil",
          "points": 10,
          "matchesT":5,
          "matchesW":3,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 8,
          "goalsAgainst": 3,
          "goalDifference": 5,
      },

      {
          "team": "Portugal",
          "points": 9,
          "matchesT":5,
          "matchesW":3,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 12,
          "goalsAgainst": 6,
          "goalDifference": 6,
      },

      {
          "team": "Japan",
          "points": 7,
          "matchesT":4,
          "matchesW":2,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 5,
          "goalsAgainst": 4,
          "goalDifference": 1,
      },

      {
          "team": "Senegal",
          "points": 6,
          "matchesT":4,
          "matchesW":2,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 7,
          "goalDifference": -2,
      },

      {
          "team": "Australia",
          "points": 6,
          "matchesT":4,
          "matchesW":2,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 4,
          "goalsAgainst": 6,
          "goalDifference": -2,
      },

      {
          "team": "Switzerland",
          "points": 6,
          "matchesT":4,
          "matchesW":2,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 9,
          "goalDifference": -4,
      },

      {
          "team": "Spain",
          "points": 5,
          "matchesT":4,
          "matchesW":1,
          "matchesD":2,
          "matchesL":1,
          "goalsFor": 9,
          "goalsAgainst": 3,
          "goalDifference": 6,
      },
      
      {
          "team": "United States",
          "points": 5,
          "matchesT":4,
          "matchesW":1,
          "matchesD":2,
          "matchesL":1,
          "goalsFor": 3,
          "goalsAgainst": 4,
          "goalDifference": -1,
      },

      {
          "team": "Poland",
          "points": 4,
          "matchesT":4,
          "matchesW":1,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 3,
          "goalsAgainst": 5,
          "goalDifference": -2,
      },

      {
          "team": "South Korea",
          "points": 4,
          "matchesT":4,
          "matchesW":1,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 8,
          "goalDifference": -3,
      },

      {
          "team": "Germany",
          "points": 4,
          "matchesT":1,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 6,
          "goalsAgainst": 5,
          "goalDifference": 1,
      },

      {
          "team": "Ecuador",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 3,
          "goalDifference": 1,
      },

      {
          "team": "Cameroon",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 4,
          "goalsAgainst": 4,
          "goalDifference": 0,
      },

      {
          "team": "Uruguay",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 2,
          "goalsAgainst": 2,
          "goalDifference": 0,
      },

      {
          "team": "Tunisia",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 1,
          "goalsAgainst": 1,
          "goalDifference": 0,
      },

      {
          "team": "Mexico",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 2,
          "goalsAgainst": 3,
          "goalDifference": -1,
      },

      {
          "team": "Belgium",
          "points": 4,
          "matchesT":3,
          "matchesW":1,
          "matchesD":1,
          "matchesL":1,
          "goalsFor": 1,
          "goalsAgainst": 2,
          "goalDifference": -1,
      },

      {
          "team": "Ghana",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 7,
          "goalDifference": -2,
      },

      {
          "team": "Saudi Arabia",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 3,
          "goalsAgainst": 5,
          "goalDifference": -2,
      },

      {
          "team": "Iran",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 4,
          "goalsAgainst": 7,
          "goalDifference": -3,
      },

      {
          "team": "Costa Rica",
          "points": 3,
          "matchesT":3,
          "matchesW":1,
          "matchesD":0,
          "matchesL":2,
          "goalsFor": 3,
          "goalsAgainst": 11,
          "goalDifference": -8,
      },

      {
          "team": "Denmark",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 1,
          "goalsAgainst": 3,
          "goalDifference": -2,
      },

      {
          "team": "Serbia",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 5,
          "goalsAgainst": 8,
          "goalDifference": -3,
      },

      {
          "team": "Wales",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 1,
          "goalsAgainst": 6,
          "goalDifference": -5,
      },

      {
          "team": "Canada",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 2,
          "goalsAgainst": 7,
          "goalDifference": -5,
      },

      {
          "team": "Qatar",
          "points": 1,
          "matchesT":3,
          "matchesW":0,
          "matchesD":1,
          "matchesL":2,
          "goalsFor": 1,
          "goalsAgainst": 7,
          "goalDifference": -6,
      },

      ]

#get results of group A
@app.route("/group-A")
def get_group_A():
  return jsonify([result for result in results if result["group"] == "A"])

#get results of group B
@app.route("/group-B")
def get_group_B():
  return jsonify([result for result in results if result["group"] == "B"])

#get results of group C
@app.route("/group-C")
def get_group_C():
  return jsonify([result for result in results if result["group"] == "C"])

#get results of group D
@app.route("/group-D")
def get_group_D():
  return jsonify([result for result in results if result["group"] == "D"])

#get results of group E
@app.route("/group-E")
def get_group_E():
  return jsonify([result for result in results if result["group"] == "E"])

#get results of group F
@app.route("/group-F")
def get_group_F():
  return jsonify([result for result in results if result["group"] == "F"])

#get results of group G
@app.route("/group-G")
def get_group_G():
  return jsonify([result for result in results if result["group"] == "G"])

#get results of group H
@app.route("/group-H")
def get_group_H():
  return jsonify([result for result in results if result["group"] == "H"])

#get all groups
@app.route("/results")
def get_results():
  return jsonify(results)

#get all topscorers
@app.route("/topscorers")
def get_topscorers():
  return jsonify(topscorers)

#get top assistants
@app.route("/top-assistants")
def get_top_assistants():
  return jsonify(top_assistants)

#get general statistics of all teams 
@app.route("/resultado-final")
def get_finalresults():
  return jsonify(final_results)

#get all data
@cross_origin 
@app.route("/main")
def apop():
  return jsonify(fino, results, topscorers, top_assistants, final_results)

if __name__ == "__main__":
  app.run(debug=True, port=4040)
