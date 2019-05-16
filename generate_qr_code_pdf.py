import sys
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


def main(pdf_file, qr_code_dir, nb_columns, nb_rows):
	c = canvas.Canvas(pdf_file)
	width = c._pagesize[0] / nb_columns
	page_height = c._pagesize[1]
	image_height = width
	text_height = 0.2 * cm
	character_width = 0.23 * cm
	height = image_height + text_height
	images = sorted(os.listdir(qr_code_dir))
	for page in chunker(images, nb_columns * nb_rows):
		for j, row in enumerate(chunker(page, nb_columns)):
			for i, image in enumerate(row):
				c.drawImage("{}/{}".format(qr_code_dir, image), width * i, page_height - height * j - image_height, width, image_height)
				image_name = os.path.splitext(image)[0]
				c.drawString(width * i + width / 2 - (len(image_name) * character_width) / 2, page_height - (height * j + image_height), image_name)
		c.showPage()
	c.save()


main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))