def caesar_minus_one(message):
    letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    new_message = ''
    for letter in message:
        if letter in letters:
            num = letters.find(letter)
            new_message += letters[num - 1]
        else:
            new_message += letter
    return new_message


def encrypt(message):
    new_message = ''
    words = message.split(' ')
    replace_index = 3
    for word in words:
        new_word = ''
        for i in range(len(word)):
            new_word += word[(i - replace_index) % len(word)]
        if new_word.endswith('/'):
            replace_index += 1
        new_message += new_word + ' '
    new_message = replaces(new_message)
    return new_message


def replaces(text):
    text = text.replace('-',',').replace('/','.\n').replace('(',"'").replace('..','--').replace('+','*').replace('"','!')
    return text


text = 'vujgvmCfb tj ufscfu ouib z/vhm jdjuFyqm jt fscfuu uibo jdju/jnqm fTjnqm tj scfuuf ibou fy/dpnqm yDpnqmf jt cfuufs boui dbufe/dpnqmj uGmb tj fuufsc ouib oftufe/ bstfTq jt uufscf uibo otf/ef uzSfbebcjmj vout/dp djbmTqf dbtft (ubsfo djbmtqf hifopv up csfbl ifu t/svmf ipvhiBmu zqsbdujdbmju fbutc uz/qvsj Fsspst tipvme wfsof qbtt foumz/tjm omfttV mjdjumzfyq odfe/tjmf Jo fui dfgb pg hvjuz-bncj gvtfsf fui ubujpoufnq up ftt/hv Uifsf vmetip fc pof.. boe sbcmzqsfgf zpom pof pvt..pcwj xbz pu pe ju/ Bmuipvhi uibu bzx bzn puo cf wjpvtpc bu jstug ttvomf sfzpv( i/Evud xOp tj scfuuf ibou /ofwfs uipvhiBm fsofw jt fopgu cfuufs boui iu++sjh x/op gJ ifu nfoubujpojnqmf tj eibs pu mbjo-fyq tju( b bec /jefb Jg fui foubujpojnqmfn jt fbtz up bjo-fyqm ju znb cf b hppe jefb/ bnftqbdftO bsf pof ipoljoh sfbuh efbj .. fu(tm pe psfn gp tf"uip'
new_message = encrypt(caesar_minus_one(text))
print(new_message)
