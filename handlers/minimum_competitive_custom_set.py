import copy
from collections import defaultdict

from helpers import common


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
    payload = {"minimum_viable_collection": collection_copy}
    return payload


if __name__ == "__main__":
    minimum_viable_collection = get_minimum_viable_custom_build("megabuilder99")
    print(minimum_viable_collection)
