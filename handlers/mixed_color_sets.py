from collections import defaultdict

from handlers.buildable_sets_by_user import get_user_buildable_sets
from helpers import common


def create_user_color_dict(user_data):
    user_color_dict = defaultdict(lambda: defaultdict(int))
    for collection_entry in user_data.get("collection"):
        for variant in collection_entry.get("variants"):
            if variant.get("color"):
                user_color_dict[variant.get("color")][collection_entry["pieceId"]] = variant.get("count")
    return user_color_dict


def create_set_color_dict(set_details):
    set_color_dict = defaultdict(lambda: defaultdict(int))
    for piece in set_details.get("pieces"):
        set_color_dict[str(piece.get("part").get("material"))][piece.get("part").get("designID")] = piece.get(
            "quantity")
    return set_color_dict


def user_has_enough_pieces_of_color(colored_pieces_from_user, colored_pieces_from_set):
    for piece_id in colored_pieces_from_set:
        if not colored_pieces_from_user:
            return False
        colored_piece_quantity_from_user = colored_pieces_from_user.get(piece_id)
        if not colored_piece_quantity_from_user:
            return False
        colored_piece_quantity_from_set = colored_pieces_from_set.get(piece_id)
        if colored_piece_quantity_from_set > colored_piece_quantity_from_user:
            return False
    return True


def find_another_suitable_color(user_color_dict, colored_pieces_from_set, taken_colors):
    for color_code in user_color_dict.keys():
        if color_code not in taken_colors and user_has_enough_pieces_of_color(user_color_dict.get(color_code),
                                                                              colored_pieces_from_set):
            return color_code


def is_set_buildable_with_different_colors(set_overview, user_color_dict):
    taken_colors = []
    set_details = common.get_set_details_by_id(set_overview.get("id"))
    set_color_dict = create_set_color_dict(set_details)
    for color in set_color_dict.keys():
        if color in taken_colors or not user_has_enough_pieces_of_color(user_color_dict.get(color),
                                                                        set_color_dict.get(color)):
            suitable_color = find_another_suitable_color(user_color_dict, set_color_dict.get(color), taken_colors)
            if not suitable_color:
                return False
            taken_colors.append(suitable_color)
    return True


def get_new_sets_by_switching_colors(username):
    new_buildable_sets = []
    already_buildable_sets = get_user_buildable_sets(username)
    user_data = common.get_user_complete_data_by_username(username)
    user_color_dict = create_user_color_dict(user_data)
    available_sets = common.get_all_available_sets()
    currently_not_buildable_sets = [available_set for available_set in available_sets if
                                    available_set.get("name") not in already_buildable_sets and available_set.get(
                                        "totalPieces") < user_data.get("brickCount")]
    for set_overview in currently_not_buildable_sets:
        if is_set_buildable_with_different_colors(set_overview, user_color_dict):
            new_buildable_sets.append(set_overview.get("name"))
    payload = {"mixed_color_sets": new_buildable_sets}
    return payload


if __name__ == "__main__":
    new_buildable_sets_response = get_new_sets_by_switching_colors("dr_crocodile")
    print(new_buildable_sets_response)
