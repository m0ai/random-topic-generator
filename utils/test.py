import json

sentences = []
count = 0

#[{} {} {}]

with open('../data/topic.list') as enfp, open('../data/topic_kr.list') as krfp:
    en_sentences = enfp.readlines()
    kr_sentences = krfp.readlines()

    for en,kr in zip(en_sentences, kr_sentences):
        sentences.append({'en' : en, 'kr' : kr})

with open('../data/topic.json','w') as fp:
    json.dump(sentences , fp, indent=4, sort_keys=True,ensure_ascii=False)
