from pdfrw import PdfReader, PdfWriter, IndirectPdfDict
import sys


def merge(paths, output_file_name):
	writer = PdfWriter()

	for path in paths:
		try:
			reader = PdfReader(path)
			writer.addpages(reader.pages)
		except:
			print(path , " could not be added")

	writer.trailer.Info = IndirectPdfDict(
		Title='merged pdf title',
		Author = 'abc',
		Subject='Pdf Merging',
		Creator= 'Merger'
		)
	writer.write(output_file_name)

	return



if __name__ == '__main__':
	# we are expecting the paths to have come from arguments
	number_of_pdfs = len(sys.argv) - 1

	paths = str(sys.argv)[1:]

	output_file_name = "outputs/merge.pdf"

	# we will pass this to our merge function

	merge(paths, output_file_name)


