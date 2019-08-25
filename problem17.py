# word count

def word_count(string):
    list_words = string.split()
    set_words = set(list_words)
    dic_count = {}
    for i in set_words:
        count = list_words.count(i)
        dic_count[i] = count
    return dic_count

input = """
        Python has traditionally checked the up-to-dateness of bytecode cache files by comparing the source metadata with source
        metadata saved in the cache file header when it was generated. While effective, this invalidation method has its drawbacks. 
        When filesystem timestamps are too coarse, Python can miss source updates, leading to user confusion.
        Additionally, having a timestamp in the cache file is problematic for build reproducibility and content-based build systems.
        """

word_count = word_count(input)
print(word_count)