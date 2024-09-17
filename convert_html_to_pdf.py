import pdfkit

def html_to_pdf(input_html, output_pdf):
    config = pdfkit.configuration(wkhtmltopdf='/usr/local/bin/wkhtmltopdf')  # Update the path as necessary
    pdfkit.from_file(input_html, output_pdf, configuration=config)

if __name__ == '__main__':
    import sys
    input_html = sys.argv[1]
    output_pdf = sys.argv[2]
    html_to_pdf(input_html, output_pdf)
