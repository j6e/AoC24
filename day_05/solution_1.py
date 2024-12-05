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

accu = 0
for seq in seqs:
    any_wrong = False

    for i, elem in enumerate(seq):
        this_rule_after = rules_after[elem] if elem in rules_after else set()
        this_rule_before = rules_before[elem] if elem in rules_before else set()
        elems_before = set(seq[:i])
        elems_after = set(seq[i + 1 :])
        # If there is any element before that is forced to be after, it's wrong
        if wrong_before := elems_before & this_rule_after:
            # print(f"{elem} wrong_before: {wrong_before}")
            any_wrong = True
            break
        # If there is any element after that is forced to be before, it's wrong
        if wrong_after := elems_after & this_rule_before:
            # print(f"{elem} wrong_after: {wrong_after}")
            any_wrong = True
            break

    if not any_wrong:
        center_elem = seq[len(seq) // 2]
        accu += center_elem

print(accu)
