import pdfkit
import sys

def html_to_pdf(input_html, output_pdf):
    pdfkit.from_file(input_html, output_pdf)

if __name__ == "__main__":
    input_html = sys.argv[1]
    output_pdf = sys.argv[2]
    html_to_pdf(input_html, output_pdf)
