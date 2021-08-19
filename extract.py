import textract
text = textract.process("refs/2106.12139.pdf")


print(text)