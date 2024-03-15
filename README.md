# builder-catalog

Simple python webapp that fulfills the functions needed.

### How to deploy

Requires python3

- Install requirements listed in requirements.txt by using `pip3 install -r requirements.txt` (add -t if you want to specify a target folder)
- Go into the main project folder (builder-catalog) and run `python3 server.py `

The server will start on port 8080; each use case has a different endpoint:

- Main task: http://localhost:8080/buildable-by-user/brickfan35
- Stretch goal 1: http://localhost:8080/collaboration-set/landscape-artist?setName=tropical-island
- Stretch goal 2: http://localhost:8080/custom-set/megabuilder99
- Stretch goal 3: http://localhost:8080/mixed-colors-sets/dr_crocodile


### Solutions

- Main task: ["car-wash", "castaway", "undersea-monster"]
- Stretch goal 1: ["spaceman77"]
- Stretch goal 2: {
    "minimum_viable_collection": [
        {
            "pieceId": "3029",
            "variants": [
                {
                    "color": "4",
                    "count": 6
                },
                {
                    "color": "2",
                    "count": 7
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "1",
                    "count": 8
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 4
                }
            ]
        },
        {
            "pieceId": "78231",
            "variants": [
                {
                    "color": "2",
                    "count": 10
                },
                {
                    "color": "1",
                    "count": 8
                },
                {
                    "color": "8",
                    "count": 7
                },
                {
                    "color": "4",
                    "count": 6
                },
                {
                    "color": "3",
                    "count": 2
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "3001",
            "variants": [
                {
                    "color": "1",
                    "count": 13
                },
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "4",
                    "count": 9
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "152",
                    "count": 2
                },
                {
                    "color": "3",
                    "count": 4
                }
            ]
        },
        {
            "pieceId": "75523",
            "variants": [
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "2",
                    "count": 8
                },
                {
                    "color": "1",
                    "count": 8
                },
                {
                    "color": "4",
                    "count": 3
                },
                {
                    "color": "152",
                    "count": 2
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "22888",
            "variants": [
                {
                    "color": "4",
                    "count": 5
                },
                {
                    "color": "1",
                    "count": 10
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "3",
                    "count": 2
                },
                {
                    "color": "152",
                    "count": 4
                },
                {
                    "color": "34",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "78221",
            "variants": [
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "1",
                    "count": 14
                },
                {
                    "color": "4",
                    "count": 9
                },
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "3",
                    "count": 3
                },
                {
                    "color": "34",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "3024",
            "variants": [
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "1",
                    "count": 6
                },
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "4",
                    "count": 4
                },
                {
                    "color": "3",
                    "count": 3
                },
                {
                    "color": "152",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "3069b",
            "variants": [
                {
                    "color": "1",
                    "count": 12
                },
                {
                    "color": "8",
                    "count": 7
                },
                {
                    "color": "4",
                    "count": 8
                },
                {
                    "color": "2",
                    "count": 4
                },
                {
                    "color": "3",
                    "count": 5
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "54200",
            "variants": [
                {
                    "color": "1",
                    "count": 10
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "4",
                    "count": 11
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "34",
                    "count": 0
                },
                {
                    "color": "3",
                    "count": 1
                },
                {
                    "color": "152",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "3062b",
            "variants": [
                {
                    "color": "2",
                    "count": 6
                },
                {
                    "color": "4",
                    "count": 6
                },
                {
                    "color": "1",
                    "count": 6
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "152",
                    "count": 3
                },
                {
                    "color": "3",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "4286",
            "variants": [
                {
                    "color": "4",
                    "count": 10
                },
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "2",
                    "count": 11
                },
                {
                    "color": "1",
                    "count": 5
                },
                {
                    "color": "152",
                    "count": 3
                }
            ]
        },
        {
            "pieceId": "63864",
            "variants": [
                {
                    "color": "1",
                    "count": 10
                },
                {
                    "color": "4",
                    "count": 8
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "8",
                    "count": 4
                },
                {
                    "color": "152",
                    "count": 4
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "3005",
            "variants": [
                {
                    "color": "8",
                    "count": 7
                },
                {
                    "color": "4",
                    "count": 5
                },
                {
                    "color": "1",
                    "count": 8
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "3",
                    "count": 1
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "3710",
            "variants": [
                {
                    "color": "2",
                    "count": 8
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "1",
                    "count": 4
                },
                {
                    "color": "4",
                    "count": 8
                },
                {
                    "color": "3",
                    "count": 2
                },
                {
                    "color": "152",
                    "count": 4
                },
                {
                    "color": "34",
                    "count": 0
                }
            ]
        },
        {
            "pieceId": "11211",
            "variants": [
                {
                    "color": "1",
                    "count": 8
                },
                {
                    "color": "8",
                    "count": 8
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "4",
                    "count": 6
                },
                {
                    "color": "152",
                    "count": 4
                },
                {
                    "color": "3",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "3023",
            "variants": [
                {
                    "color": "4",
                    "count": 8
                },
                {
                    "color": "2",
                    "count": 8
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "1",
                    "count": 6
                },
                {
                    "color": "3",
                    "count": 3
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "14719",
            "variants": [
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "1",
                    "count": 14
                },
                {
                    "color": "4",
                    "count": 7
                },
                {
                    "color": "3",
                    "count": 4
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "3004",
            "variants": [
                {
                    "color": "8",
                    "count": 7
                },
                {
                    "color": "1",
                    "count": 6
                },
                {
                    "color": "4",
                    "count": 7
                },
                {
                    "color": "2",
                    "count": 4
                },
                {
                    "color": "3",
                    "count": 3
                },
                {
                    "color": "152",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "11477",
            "variants": [
                {
                    "color": "8",
                    "count": 5
                },
                {
                    "color": "4",
                    "count": 5
                },
                {
                    "color": "1",
                    "count": 11
                },
                {
                    "color": "2",
                    "count": 5
                },
                {
                    "color": "152",
                    "count": 3
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "3795",
            "variants": [
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "4",
                    "count": 10
                },
                {
                    "color": "1",
                    "count": 9
                },
                {
                    "color": "2",
                    "count": 11
                },
                {
                    "color": "3",
                    "count": 2
                },
                {
                    "color": "152",
                    "count": 2
                },
                {
                    "color": "34",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "2431",
            "variants": [
                {
                    "color": "4",
                    "count": 2
                },
                {
                    "color": "2",
                    "count": 5
                },
                {
                    "color": "8",
                    "count": 8
                },
                {
                    "color": "1",
                    "count": 7
                },
                {
                    "color": "34",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 3
                },
                {
                    "color": "152",
                    "count": 1
                }
            ]
        },
        {
            "pieceId": "77232",
            "variants": [
                {
                    "color": "1",
                    "count": 11
                },
                {
                    "color": "8",
                    "count": 7
                },
                {
                    "color": "4",
                    "count": 10
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "34",
                    "count": 0
                },
                {
                    "color": "152",
                    "count": 3
                },
                {
                    "color": "3",
                    "count": 2
                }
            ]
        },
        {
            "pieceId": "4070",
            "variants": [
                {
                    "color": "2",
                    "count": 11
                },
                {
                    "color": "4",
                    "count": 6
                },
                {
                    "color": "8",
                    "count": 4
                },
                {
                    "color": "1",
                    "count": 6
                },
                {
                    "color": "34",
                    "count": 0
                },
                {
                    "color": "152",
                    "count": 1
                },
                {
                    "color": "3",
                    "count": 3
                }
            ]
        },
        {
            "pieceId": "36840",
            "variants": [
                {
                    "color": "8",
                    "count": 6
                },
                {
                    "color": "4",
                    "count": 7
                },
                {
                    "color": "2",
                    "count": 9
                },
                {
                    "color": "1",
                    "count": 9
                },
                {
                    "color": "3",
                    "count": 6
                },
                {
                    "color": "34",
                    "count": 0
                },
                {
                    "color": "152",
                    "count": 4
                }
            ]
        }
    ]
}
- Stretch goal 3: ["coffee-bar"] (This is an answer based on the assumption that the first potential color substitute found is the only one present for each color in each set. Without this assumption, this is only a partial answer and the code would need to explore each substitution possibility recursively).