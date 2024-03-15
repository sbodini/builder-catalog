import requests

API_URL = "https://d16m5wbro86fg2.cloudfront.net/api"


def get_user_data_by_id(user_id):
    user_data_response = requests.Session().get(
        url="{}/user/by-id/{}".format(API_URL, user_id))
    if user_data_response.status_code != 200 or not user_data_response.json():
        print("Error getting user data for user with id {}".format(user_id))
        return None
    return user_data_response.json()


def get_set_complete_data_by_name(set_name):
    available_sets = get_all_available_sets()
    for available_set in available_sets:
        if available_set.get("name") == set_name:
            set_details_response = requests.Session().get(
                url="{}/set/by-id/{}".format(API_URL, available_set.get("id")))
            if set_details_response.status_code != 200:
                print("Error getting set details")
                return
            return set_details_response.json()


def get_all_available_sets():
    all_sets_overview_response = requests.Session().get(url=("%s/sets" % API_URL))
    if all_sets_overview_response.status_code != 200:
        print("Error getting all sets overview")
        return
    return all_sets_overview_response.json().get("Sets")


def get_set_details_by_id(set_id):
    set_details_response = requests.Session().get(
        url="{}/set/by-id/{}".format(API_URL, set_id))
    if set_details_response.status_code != 200:
        print("Error getting set details for set with id {}".format(set_id))
        return None
    return set_details_response.json()


def get_users_complete_data():
    users_overview_response = requests.Session().get(
        url="{}/users".format(API_URL))
    if users_overview_response.status_code != 200:
        print("Error getting users overview")
        return None
    users_complete_data = []
    for user_overview in users_overview_response.json().get("Users"):
        user_data = get_user_data_by_id(user_overview.get("id"))
        if user_data:
            users_complete_data.append(user_data)
    return users_complete_data


def get_user_complete_data_by_username(username):
    user_overview_response = requests.Session().get(
        url="{}/user/by-username/{}".format(API_URL, username))
    if user_overview_response.status_code != 200:
        print("Error getting user {} overview".format(username))
        return None
    return get_user_data_by_id(user_overview_response.json().get("id"))


def map_user_collection_to_dict(user_data):
    return {collection_entry.get("pieceId"): {variant_entry.get("color"): variant_entry.get("count") for variant_entry in collection_entry.get("variants")} for collection_entry in
            user_data.get("collection")}


def get_set_overview_by_name(set_name):
    set_overview_response = requests.Session().get(
        url="{}/set/by-name/{}".format(API_URL, set_name))
    if set_overview_response.status_code != 200:
        print("No set with name {} found".format(set_name))
        return
    return set_overview_response.json()


def map_user_collection_to_dict_new(user_data):
    result_map = {}
    for collection_entry in user_data.get("collection"):
        for variant_entry in collection_entry.get("variants"):
            if variant_entry.get("color") not in result_map:
                result_map["{}#{}".format(collection_entry.get("pieceId"), variant_entry.get("color"))] = variant_entry.get("count")
    return result_map


def user_has_all_pieces(set_pieces, user_collection_dict):
    for piece in set_pieces:
        if not user_collection_dict.get(piece.get("part").get("designID")):
            return False
        number_of_colored_pieces_in_user_collection = user_collection_dict.get(piece.get("part").get("designID")).get(str(piece.get("part").get("material")))
        if not number_of_colored_pieces_in_user_collection or number_of_colored_pieces_in_user_collection < piece.get("quantity"):
            return False
    return True