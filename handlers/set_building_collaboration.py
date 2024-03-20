from collections import defaultdict, Counter

from helpers import common


def combine_users_collections(specific_user_data, user_complete_data):
    specific_user_collection_dict = common.map_user_collection_to_dict(specific_user_data)
    user_collection_dict = common.map_user_collection_to_dict(user_complete_data)
    collections_union = defaultdict(int)
    for key in specific_user_collection_dict.keys() | user_collection_dict.keys():
        if specific_user_collection_dict.get(key) and user_collection_dict.get(key):
            collections_union[key] = specific_user_collection_dict.get(key) + user_collection_dict.get(key)
        elif specific_user_collection_dict.get(key) and not user_collection_dict.get(key):
            collections_union[key] = specific_user_collection_dict.get(key)
        else:
            collections_union[key] = user_collection_dict.get(key)
    return collections_union


def users_collaboration_for_sets(username, set_name):
    compatible_users = []
    users_complete_data = common.get_users_complete_data()
    specific_user_data = None
    for user_complete_data in users_complete_data:
        if user_complete_data.get("username") == username:
            specific_user_data = user_complete_data
            break
    if not specific_user_data:
        print("No user with name {} found".format(username))
        return []
    set_overview = common.get_set_overview_by_name(set_name)
    if not set_overview:
        return []
    set_details = common.get_set_details_by_id(set_overview.get("id"))
    if not set_details:
        return []
    for user_complete_data in users_complete_data:
        if user_complete_data.get("username") != username and not user_complete_data.get(
                "id") == specific_user_data.get("id"):
            combined_collections_dict = combine_users_collections(specific_user_data, user_complete_data)
            if common.user_has_all_pieces(set_details.get("pieces"), combined_collections_dict):
                compatible_users.append(user_complete_data.get("username"))
    payload = {"compatible_users": compatible_users}
    return payload


if __name__ == "__main__":
    compatible_users_response = users_collaboration_for_sets("landscape-artist", "tropical-island")
    print(compatible_users_response)
