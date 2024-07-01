from tkinter import filedialog
from pypdf import PdfReader

def title_display():
    print("PDF Scanner: \nSelect your file.")

def file_selector():
    file_path = filedialog.askopenfilename()
    return file_path

    #If file choice is cancelled add an escape here

def print_filepath(file_path):
    print(file_path)

def prompt_keyword():
    try:
        keyword = input("Input keyword you are searching for: ")
        return keyword
    except EOFError:
        print("An EOF error occurred. The input was unexpectedly terminated.")
    except KeyboardInterrupt:
        print("The input operation was interrupted by the user.")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

def read_pdf(word, file_path):
    reader = PdfReader(file_path)
    line_hit = []
    for page in reader.pages:
        text = page.extract_text()
        for line in text.split("\n"):
            if word in line:
                line_hit.append(line)
    return line_hit
        ##Add an escape if no hits

def format_key_hits(hits):
    pass

def results():
    pass

def main():
    title_display()
    file_path = file_selector()
    print_filepath(file_path)
    keyword = prompt_keyword()
    hits = read_pdf(keyword, file_path)
    format_key_hits(hits)
    results()

main()