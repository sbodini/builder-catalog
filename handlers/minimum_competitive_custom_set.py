import copy
from collections import defaultdict

import common


def calculate_max_amount_of_bricks_per_color(specific_user_collection_dict, users_collections_dict):
    union_dict = defaultdict(list)
    result = {}
    for key in specific_user_collection_dict.keys():
        for collection_piece in users_collections_dict:
            if key in collection_piece.keys():
                union_dict[key].append(collection_piece[key])
            else:
                union_dict[key].append(0)
    for key, value in union_dict.items():
        value.sort()
        result[key] = value[5] if value[5] < specific_user_collection_dict.get(
            key) else specific_user_collection_dict.get(key)
    return result


def get_minimum_viable_custom_build(username):
    users_complete_data = common.get_users_complete_data()
    users_collections_dict = []
    specific_user_data = None
    for user_complete_data in users_complete_data:
        if user_complete_data.get("username") == username:
            specific_user_data = user_complete_data
            break
    specific_user_collection_dict = common.map_user_collection_to_dict_new(specific_user_data)
    for user_complete_data in users_complete_data:
        if not user_complete_data.get("username") == username:
            user_collection_dict = common.map_user_collection_to_dict_new(user_complete_data)
            users_collections_dict.append(user_collection_dict)
    minimum_viable_custom_build_dict = calculate_max_amount_of_bricks_per_color(specific_user_collection_dict,
                                                                                users_collections_dict)
    collection_copy = copy.deepcopy(specific_user_data.get("collection"))
    for collection_entry in collection_copy:
        for variant in collection_entry.get("variants"):
            variant["count"] = minimum_viable_custom_build_dict.get(
                "{}#{}".format(collection_entry.get("pieceId"), variant.get("color")))
    return collection_copy


if __name__ == "__main__":
    minimum_viable_collection = get_minimum_viable_custom_build("megabuilder99")
    print(minimum_viable_collection)
"""
[
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
"""
