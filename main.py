import sys

import pandas as pd

def gethastags(data):  # get all the hastags into the dict
    hashtags_list = list()
    dic_ht = dict()
    hashtags = pd.DataFrame(raw, columns=["hashtags"])
    dic_ht = hashtags.to_dict()
    dic_ht = dic_ht["hashtags"]
    for i in dic_ht:
        for j in dic_ht[i]:
            hashtags_list.append(j.lower())
    for i in data.index:
        text = set(data.at[i, 'full_text'].split())
        for i in text:
            if i[0] == "#":
                hashtags_list.append(i[1:].lower())
    tmp = [0] * len(set(hashtags_list))
    return dict(zip(set(hashtags_list), tmp))


def getdatabym(data, M):  # get all the tweets by month
    data = pd.DataFrame(data, columns=["created_at", "full_text", "hashtags"])
    tmp = pd.Timestamp(("2020-0" + str(M) + "-01"), tz="UTC")
    tmp_1 = pd.Timestamp(("2020-0" + str(M + 1) + "-01"), tz="UTC")
    data = data[data.created_at < tmp_1]
    return data[data.created_at > tmp]


if __name__ == '__main__':
    raw = pd.read_pickle(sys.argv[1])
    for i in range(1,8):
        data = getdatabym(raw, i)
        hashtags = gethastags(data)
        for tw in data.index:
            text = set([x.lower() for x in (data.at[tw, 'full_text'].split())])
            for hashtag in data.at[tw, 'hashtags']:
                if hashtag.lower() in hashtags:
                    hashtags[hashtag.lower()] += 1
            for word in text:
                if word in hashtags:
                    hashtags[word] += 1
                elif word[0:] in hashtags:
                    hashtags[word] += 1
        out = sorted(hashtags.items(), key=lambda x: x[1], reverse=True)
        out = pd.DataFrame(out[:20])
        out.columns = ["Month",i]
        out.to_csv((sys.argv[1].split('.')[0] + '.csv'), mode="a", index=False)
