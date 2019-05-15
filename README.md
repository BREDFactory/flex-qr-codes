install dependencies:
```
npm install -g qrcode
pip install reportlab
```

to generate qr codes launch:
```
python generate_qr_codes.py places.json qr_codes
```

to generate pdf with all qr codes:
```
python generate_qr_code_pdf.py qr_codes.pdf qr_codes <nb_columns> <nb_rows>
```