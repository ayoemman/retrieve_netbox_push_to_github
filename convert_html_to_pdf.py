import pdfkit

def convert_html_to_pdf(html_file, pdf_file):
    try:
        pdfkit.from_file(html_file, pdf_file)
        print(f"Successfully converted {html_file} to {pdf_file}")
    except Exception as e:
        print(f"Failed to convert {html_file} to {pdf_file}: {e}")

if __name__ == "__main__":
    html_file = "/home/user1/netbox_data/netbox_data.html"  # Change this to your HTML file path
    pdf_file = "/home/user1/netbox_data/netbox_data.pdf"    # Change this to your desired PDF file path
    convert_html_to_pdf(html_file, pdf_file)
