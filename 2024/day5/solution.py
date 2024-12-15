from collections import defaultdict


def parse_rules(rules):
    """
    Parse the rules into a dictionary of adjacency lists.
    """
    rule_dict = defaultdict(set)
    for rule in rules:
        a, b = map(int, rule.split("|"))
        rule_dict[a].add(b)
    return rule_dict


def is_valid_order(update, rule_dict):
    """
    Check if the update respects the rules in the rule_dict.
    """
    # Convert update into a mapping of page -> index
    page_to_index = {page: i for i, page in enumerate(update)}

    # Validate each rule that applies to this update
    for page_number in update:
        if page_number in rule_dict:
            for before_page_number in rule_dict[page_number]:
                # Check if before_page_number is in the update and if so, ensure page_number comes before before_page_number
                if (
                    before_page_number in page_to_index
                    and page_to_index[page_number] > page_to_index[before_page_number]
                ):
                    return False
    return True


def find_middle_page(update):
    """
    Find the middle page of an update.
    """
    return update[len(update) // 2]


def reorder_update(update, rule_dict):
    ordered_update = []

    for page_number in update:
        if page_number in rule_dict:
            for before_page_number in rule_dict[page_number]:
                # Check if before_page_number is in the update and if so, ensure page_number comes before before_page_number
                if before_page_number in ordered_update and page_number in ordered_update:
                    if ordered_update.index(before_page_number) < ordered_update.index(page_number):
                        ordered_update.pop(ordered_update.index(page_number))
                        ordered_update.insert(ordered_update.index(before_page_number), page_number)
                elif before_page_number not in ordered_update and page_number not in ordered_update:
                    ordered_update.append(page_number)
                elif page_number not in ordered_update:
                    ordered_update.insert(ordered_update.index(before_page_number), page_number)
        else:
            if page_number not in ordered_update:
                ordered_update.append(page_number)
    return ordered_update


def part1(ordering_rules, updates):
    valid_middle_pages = []
    rule_dict = parse_rules(ordering_rules)
    for update in updates:
        # Convert updates to integer
        update = [int(x) for x in update]
        if is_valid_order(update, rule_dict):
            valid_middle_pages.append(int(find_middle_page(update)))
    print(f"Solution part1: {sum(valid_middle_pages)}")


def part2(ordering_rules, updates):
    valid_middle_pages = []
    rule_dict = parse_rules(ordering_rules)
    invalid_updates = []
    for update in updates:
        # Convert updates to integer
        update = [int(x) for x in update]
        if not is_valid_order(update, rule_dict):
            invalid_updates.append(update)
    for update in invalid_updates:
        ordered_update = reorder_update(update, rule_dict)
        valid_middle_pages.append(int(find_middle_page(ordered_update)))
    print(f"Solution part2: {sum(valid_middle_pages)}")


def main():
    with open("input.txt", "r") as file:
        # Converts file into list
        # strips newline for each line
        ordering_rules_flag = True
        ordering_rules = []
        updates = []
        for line in file:
            line_striped = line.strip()
            if line_striped == "":
                ordering_rules_flag = False
            elif ordering_rules_flag:
                ordering_rules.append(line_striped)
            else:
                updates.append(line_striped.split(","))

    part1(ordering_rules, updates)
    part2(ordering_rules, updates)


if __name__ == "__main__":
    main()
