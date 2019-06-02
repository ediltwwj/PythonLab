"""实验七第三题"""


def getTxt(file_name):
    """读取英本文本，处理符号转换为只有单词和空格的文本"""
    txt = open(file_name).read()
    txt = txt.lower()

    for ch in '!"@#$%^&*()+,-./:;<=>?@[\\]_`~{|}':
        txt.replace(ch, " ")

    return txt


def txt_split_count(text):
    """切割文本，统计词频"""
    txt_list = text.split()  # 分割文本，适合英文
    counts_list = {}

    for word in txt_list:
        counts_list[word] = counts_list.get(word, 0) + 1

    return counts_list


def sort_print(**counts_list):
    """排序并输出单词词频"""
    new_counts_list = list(counts_list.items())
    new_counts_list.sort(key=lambda x: x[1], reverse=True)

    for i in range(len(new_counts_list)):
        word, count = new_counts_list[i]
        print('{0:<10}{1:>5}'.format(word, count))


if __name__ == "__main__":
    file_name = "three.txt"
    new_txt = getTxt(file_name)
    counts_list = txt_split_count(new_txt)
    sort_print(**counts_list)
