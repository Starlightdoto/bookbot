path_to_file = 'books/frankenstein.txt'

def count_chars(text):
    chars = {}
    for char in text.lower():
        if char not in chars:
            chars[char] = 1
        else:
            chars[char] +=1

    return chars
          

def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open(path_to_file) as f:
        file_contents = f.read()
    
    words_count = count_words(file_contents)
    chars = count_chars(file_contents)

    print(f'--- Begin report of {path_to_file} ---')
    print(f"{words_count} words found in the document")
    for i in chars:
        print(f"The {i} character was found {chars[i]} times")


main()