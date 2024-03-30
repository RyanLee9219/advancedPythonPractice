from translate import Translator
translator = Translator(to_lang='zh')
try:
    with open('./test.txt',mode='r') as my_file:
        text = my_file.read()
        translation = translator.translate(text)
        print(translation)
     # with open('test-zh.txt', mode="w") as my_file2:
     #        my_file2.write(translation)
except UnicodeEncodeError as e:
    print('what is going on?')