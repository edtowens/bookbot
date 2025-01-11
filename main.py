def main():
    filename = "books/frankenstein.txt"
    file_contents = ""

    def word_count(str):
        count = len(str.split())
        return count
    
    def char_count(str):
        counts = {}
        for char in str.lower():
            if char in counts and char.isalpha():
                counts[char] += 1
            else:
                if char.isalpha():
                    counts[char] = 1
        return counts
    
    def report(str):
        print(f"--- Begin report of {filename} ---")
        print(f"{word_count(str)} words found in the document")
        for key in char_count(str):
            print(f"The '{key}' character was found {char_count(str)[key]} times")


    with open(filename) as f:
        file_contents = f.read()

    report(file_contents)

    

if __name__ == "__main__":
    main()