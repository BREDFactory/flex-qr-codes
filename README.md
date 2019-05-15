install dependency:
npm install -g qrcode

to generate qr codes launch:
python generate\_qr\_codes.py places.json qr\_codes

to generate pdf with all qr codes:
python generate_qr_code_pdfs.py qr_codes.pdf qr_codes *nb_columns* *nb_rows*