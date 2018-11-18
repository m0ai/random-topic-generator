

sentences = []
count = 0

with open('topic.list') as fp:
    lines = fp.readlines()
    count = len(lines)
    for line in lines:
        if not line in sentences:
            sentences.append(line)


with open('removed_duplicated_topic.list','w') as fp:
    for l in sentences:
        fp.write(l)

print('%d > %d' % (count, len(sentences)))
