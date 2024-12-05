import random


rules_before, rules_after = {}, {}
seqs = []

with open("day_05/input.txt") as f:
    parsing_rules = True
    for line in f:
        if parsing_rules:
            if line == "\n":
                parsing_rules = False
                continue

            a, b = [int(x) for x in line.strip().split("|")]
            rules_before[b] = rules_before[b] | {a} if b in rules_before else {a}
            rules_after[a] = rules_after[a] | {b} if a in rules_after else {b}
        else:
            seqs.append([int(x) for x in line.strip().split(",")])


def get_incorrect_pairs(seq: list[int]) -> set[tuple[int, int]]:
    incorrect_pairs = set()
    for i, elem in enumerate(seq):
        this_rule_after = rules_after[elem] if elem in rules_after else set()
        this_rule_before = rules_before[elem] if elem in rules_before else set()
        elems_before = set(seq[:i])
        elems_after = set(seq[i + 1 :])
        # If there is any element before that is forced to be after, it's wrong
        # If there is any element after that is forced to be before, it's wrong
        if (wrong_before := elems_before & this_rule_after) or (
            wrong_after := elems_after & this_rule_before
        ):
            pairs_before = {
                (elem, y) if elem < y else (y, elem) for y in wrong_before if elem != y
            }
            pairs_after = {
                (elem, y) if elem < y else (y, elem) for y in wrong_after if elem != y
            }
            incorrect_pairs |= pairs_before | pairs_after

    return incorrect_pairs


accu = 0
for seq in seqs:
    incorrect_pairs = get_incorrect_pairs(seq)

    if not incorrect_pairs:
        continue

    # Fix the order of the ones that are wrong
    while incorrect_pairs:
        # A bit of randomness to avoid infinite loops
        x, y = random.choice(list(incorrect_pairs))
        # Swap x and y on a copy of the sequence
        new_seq = seq.copy()
        new_seq[seq.index(x)], new_seq[seq.index(y)] = y, x
        # Check if the new sequence is correct and
        # asign the new sequence to the original
        incorrect_pairs = get_incorrect_pairs(new_seq)
        seq = new_seq

    accu += seq[len(seq) // 2]

print(accu)
