# Input: Words on the current line of the document
# Output: Unique words in the document up to and including this line


def add_unique_word_on_line(words_on_line, word_list):
    for word in words_on_line:
        if word != "Gettysburg":
            word = word.lower()
        word = word.strip(".,")
        if word in word_list:
            pass
        elif word == "-":
            pass
        else:
            word_list.append(word)

# Input: A line of text in the input file
# Output: Words as strings of text on that line


def gimme_words(line_of_text):
    words_on_line = line_of_text.split()
    return words_on_line

# Input: file name containing text to find unique words in
# Output: list of unique words


def process_document(filename):
    try:
        document = open(filename, "r")
    except:
        print("File " + filename + " did not open.")
        document = open("GettysburgAddress.txt", "r")

    word_list = []
    for line_of_text in document:
        line_of_text = line_of_text.strip()
        words_on_line = gimme_words(line_of_text)
        add_unique_word_on_line(words_on_line, word_list)

    print(len(word_list))

    document.close()
    
    return word_list


def main():

    unique = process_document("GettysburgAddress.txt")
    unique.sort()
    print(unique)

main()
