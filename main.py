# import pytesseract
# from PIL import Image
# img = Image.open("761a95a8-b8fb-49e7-a6c3-3d9dc203b9b0.jpeg")
# pytesseract.pytesseract.tesseract_cmd("/usr/share/tesseract-ocr/4.00/tessdata/")
#
# result = pytesseract.image_to_string(img, lang="fas")
# with open("converted image.text", mode="w", encoding="utf-8") as text_file:
#     text_file.write(result)


from PIL import Image
import pytesseract


def process_image(iamge_name, lang_code):
    return pytesseract.image_to_string(Image.open(iamge_name), lang="fas")


def print_data(data):
    print(data)


def output_file(filename, data):
    file = open(filename, "w+")
    file.write(data)
    file.close()


def main():
    data_eng = process_image("761a95a8-b8fb-49e7-a6c3-3d9dc203b9b0.jpeg", "fas")
    # data_ben = process_image("test_ben.png", "ben")
    print_data(data_eng)
    # print_data(data_ben)
    output_file("eng.txt", data_eng)
    # output_file("ben.txt", data_ben)


if __name__ == '__main__':
    main()
