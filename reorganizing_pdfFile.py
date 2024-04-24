from PyPDF2 import PdfFileReader, PdfFileWriter


def ifexists(total_pages, page_no):
    """
    This function organize a pdf file based on a list of numbers with
    the order of each page. It's useful when you have a large pdf file.

    :param File name: Name of the original pdf File with the .pdf term
    :ordered_pages_str: List with the position values of each page like [a, b, c, ...]
    """
    if page_no <= total_pages:
        return False
    return True


def reodering(path):
    """
    This function takes file location and then reorders it as specified by the user.
    and saves it into a pdf file with specified name into the current directory.
    :param path: File on which operation is going to perform
    """

    # Creating object of Read and Write functions of the Library.
    pdf_writer = PdfFileWriter()
    pdf_reader = PdfFileReader(path)

    # get total no.of pages ie length of PDF
    total_pages = pdf_reader.getNumPages()

    # Taking input that how many pages want to reorder
    #n = int(input("Enter the Total Number of pages which you want to reorder:"))

    ordered_pages_str = input("Insert the list of the values with the position of each page separeted by comma:")

    # Removendo os colchetes e dividindo a string em substrings nos espaços
    substrings = ordered_pages_str[1:-1].split(", ")

    # Convertendo cada substring em um número inteiro e criando uma lista
    ordered_pages = [int(substring) for substring in substrings]
    
    print("Pages are going to be in these order: ", end="")
    print(ordered_pages)
    print(type(ordered_pages))

    # if ordered pages are ready in a list then passing it further into write function
    print("\nPDF being prepared !")
    for page in ordered_pages:
        pdf_writer.addPage(pdf_reader.getPage(page - 1))

    # Saving the PDF with the specified name
    output_file = input("Enter the filename in which you want to save (without .pdf extension): ") + '.pdf'
    with open(output_file, 'wb') as fh:
        pdf_writer.write(fh)

    print(f"Great Success!!! Check your directory for {output_file} file!")


if __name__ == '__main__':
    path = input("Enter File name: ")
    reodering(path)