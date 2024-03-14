import common


def get_user_buildable_sets(username):
    user_data = common.get_user_complete_data_by_username(username)
    if not user_data:
        return
    user_brick_count = user_data.get("brickCount")
    user_collection_dict = common.map_user_collection_to_dict(user_data)
    sets_user_can_build = []
    available_sets = common.get_all_available_sets()
    if not available_sets:
        return
    for set_overview in available_sets:
        if set_overview.get("id") and set_overview.get("totalPieces") <= user_brick_count:
            set_details = common.get_set_details_by_id(set_overview.get("id"))
            if common.user_has_all_pieces(set_details.get("pieces"), user_collection_dict):
                sets_user_can_build.append(set_overview)
    return sets_user_can_build

if __name__ == "__main__":
     buildable_sets = get_user_buildable_sets("brickfan35")
     print(buildable_sets) # the answer is 3 sets: car-wash, castaway and undersea-monster