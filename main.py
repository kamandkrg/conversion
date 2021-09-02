# import pytesseract
# from PIL import Image
# img = Image.open("761a95a8-b8fb-49e7-a6c3-3d9dc203b9b0.jpeg")
# pytesseract.pytesseract.tesseract_cmd("/usr/share/tesseract-ocr/4.00/tessdata/")
#
# result = pytesseract.image_to_string(img, lang="fas")
# with open("converted image.text", mode="w", encoding="utf-8") as text_file:
#     text_file.write(result)

from pdf2image import convert_from_path
from PIL import Image
import pytesseract
import os


def process_image(image_name, lang_code):
    return pytesseract.image_to_string(Image.open(image_name), lang=lang_code)


def output_file(filename, data):
    file = open(filename, "w+")
    file.write(data)
    file.close()


def main(pdf):
    result = ""
    images = convert_from_path(pdf)
    for i in range(len(images)):
        images[i].save("page" + str(i) + ".jpg", "JPEG")
        data_eng = process_image("page" + str(i) + ".jpg", "fas+eng")
        result += data_eng
        os.remove("page" + str(i) + ".jpg")
    output_file(f"result.txt", result)


if __name__ == "__main__":
    main("جنرالیزاسیون.pdf")
