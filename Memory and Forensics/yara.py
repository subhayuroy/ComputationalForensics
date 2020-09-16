import operator
import os
import sys

sys.path.insert(0, os.getcwd())
import plyara.interp as interp

# Plyara is a script that lexes and parses a file consisting of one more Yara
# rules into a python dictionary representation.
if __name__ == '__main__':
    file_to_analyze = sys.argv[1]
    rulesDict = interp.parseString(open(file_to_analyze).read())
    authors = {}
    imps = {}
    meta_keys = {}
    max_strings = []
    max_string_len = 0
    tags = {}
    rule_count = 0

    for rule in rulesDict:
        rule_count += 1

        # Imports
    if 'imports' in rule:
        for imp in rule['imports']:
            imp = imp.replace('"', '')

            if imp in imps:
                imps[imp] += 1
            else:
                imps[imp] = 1
                # Tags
    if 'tags' in rule:
        for tag in rule['tags']:
            if tag in tags:
                tags[tag] += 1
            else:
                tags[tag] = 1

    # Metadata
    if 'metadata' in rule:
        for key in rule['metadata']:
            if key in meta_keys:
                meta_keys[key] += 1
            else:
                meta_keys[key] = 1

            if key in ['Author', 'author']:
                if rule['metadata'][key] in authors:
                    authors[rule['metadata'][key]] += 1
                else:
                    authors[rule['metadata'][key]] = 1

                    # Strings
    if 'strings' in rule:
        for strr in rule['strings']:
            if len(strr['value']) > max_string_len:
                max_string_len = len(strr['value'])
                max_strings = [(rule['rule_name'], strr['name'], strr['value'])]
            elif len(strr['value']) == max_string_len:
                max_strings.append((rule['rule_name'], strr['key'], strr['value']))

    print("\nThe number of rules implemented" + str(rule_count))
    ordered_meta_keys = sorted(meta_keys.items(), key=operator.itemgetter(1),
                               reverse=True)
    ordered_authors = sorted(authors.items(), key=operator.itemgetter(1),
                             reverse=True)
    ordered_imps = sorted(imps.items(), key=operator.itemgetter(1), reverse=True)
    ordered_tags = sorted(tags.items(), key=operator.itemgetter(1), reverse=True)