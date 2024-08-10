def parse_tag_file(data):
    tags = {}
    for row in data:
        name, positive, negative = row
        t = tags
        if '-' in name:
            sections = name.split('-')
            t[sections[0]] = t.get(sections[0], {})
            t = t[sections[0]]

            for section in sections:
                if section not in t:
                    t[section] = {}
                t = t[section]
        else:
            if 'others' not in tags:
                tags['others'] = {}
            t = tags['others'][name] = {}
        t['positive'] = positive
        if negative:
            t['negative'] = negative
    return tags


if __name__ == '__main__':
    fname = "styles.csv"
    import csv
    with open(fname, "r", encoding="utf-8") as file:
        data = list(csv.reader(file))
        for k, v in parse_tag_file(data).items():
            print(k, v)
