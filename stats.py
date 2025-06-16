def get_num_words(contents: str) -> int:
    split_contents = contents.split()
    return len(split_contents)


def char_count(contents: str) -> dict[str, int]:
    char_dict: dict[str, int] = {}

    for c in contents:
        lil_c: str = c.lower()
        if lil_c in char_dict:
            char_dict[lil_c] += 1
        else:
            char_dict[lil_c] = 1
    return char_dict


def sorted_dict(char_dict: dict[str, int]) -> list[dict[str, str | int]]:
    new_list: list[dict[str, str | int]] = []
    for key, value in char_dict.items():
        new_dict = {"char": key, "num": value}
        new_list.append(new_dict)
    sorted_list = sorted(new_list, key=lambda item: item["num"], reverse=True)
    return sorted_list
