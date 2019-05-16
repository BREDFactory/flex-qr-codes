import sys
import os
from reportlab.pdfgen import canvas
from reportlab.lib.units import cm


def chunker(seq, size):
    return (seq[pos:pos + size] for pos in range(0, len(seq), size))


class Generator:
	def __init__(self, pdf_file, qr_code_dir, nb_columns, nb_rows):
		self.pdf_file = pdf_file
		self.qr_code_dir = qr_code_dir
		self.nb_columns = nb_columns
		self.nb_rows = nb_rows
		self.c = canvas.Canvas(self.pdf_file)
		self.font_size = 8
		self.c.setFontSize(self.font_size)
		self.width = self.c._pagesize[0] / self.nb_columns
		self.text_height = self.c._fontsize
		self.height = self.c._pagesize[1] / self.nb_rows
		self.page_height = self.c._pagesize[1]
		self.image_width = min([self.width, self.height - self.text_height])
		self.image_height = self.image_width
		self.character_width = self.c._fontsize * 0.54

	def generate(self):
		images = sorted(os.listdir(self.qr_code_dir))
		for page in chunker(images, self.nb_columns * self.nb_rows):
			self.c.setFontSize(self.font_size)
			for j, row in enumerate(chunker(page, self.nb_columns)):
				for i, image in enumerate(row):
					self.c.drawImage("{}/{}".format(self.qr_code_dir, image), self.width * i + self.width / 2 - self.image_width / 2, self.page_height - self.height * j - self.image_height, self.image_width, self.image_height)
					image_name = os.path.splitext(image)[0]
					self.drawRotatedString(0, self.width * i + self.width / 2 - (len(image_name) * self.character_width) / 2, self.page_height - (self.height * j + self.image_height + self.text_height / 2), image_name)
			self.c.showPage()
		self.c.save()

	def drawRotatedString(self, rotation, x, y, text):
		self.c.rotate(rotation)
		self.c.drawString(x, y, text)
		self.c.rotate(360 - rotation)


def main(pdf_file, qr_code_dir, nb_columns, nb_rows):
	gen = Generator(pdf_file, qr_code_dir, nb_columns, nb_rows)
	gen.generate()


main(sys.argv[1], sys.argv[2], int(sys.argv[3]), int(sys.argv[4]))