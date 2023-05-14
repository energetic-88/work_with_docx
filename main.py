from docxtpl import DocxTemplate


def main():
    doc = DocxTemplate(r".\test.docx")
    context = {'unit_number': "А0000"}
    doc.render(context)
    doc.save("result.docx")


if __name__ == '__main__':
    main()
