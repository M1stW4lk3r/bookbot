def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = get_word_count(text)
    char_count = get_char_count(text)
    char_sort = sort_char(char_count)
    report = create_report(char_sort, word_count)


def get_book_text(path):
    with open(path) as f:
        return f.read()

def get_word_count(text):
    words = text.split()
    count = 0
    for i in words:
        count += 1
    return count

def get_char_count(text):
    lowered = text.lower()
    char_dict = {}
    char_list = []
    for i in lowered:
        char_list.append(i)
    for i in char_list:
        char_dict[i] = char_dict.get(i, 0) + 1 
    return char_dict

def sort_logic(dict):
    return dict["num"]

def sort_char(char_dict):
    sorted_list = []
    for i in char_dict:
        if str.isalpha(i) == True:
            sorted_list.append({"char":i, "num":char_dict[i]})
    sorted_list.sort(reverse=True, key=sort_logic)
    return sorted_list

def create_report(sorted_list,word_count):
    print("---Start Report of frankenstein.txt---")
    print(f"{word_count} words found in the document.")
    print(" ")
    for item in sorted_list:
        print(f"The '{item['char']}' character was found {item['num']} times.")
    print("-------------End of Report-------------")



main()

