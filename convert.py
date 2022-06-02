from PIL import Image,ImageFilter

letterfield_x = 44
letterfield_y = 58
letter_height = 30
letter_width  = 30
letter_spacing = 2

word_spacing = 1

post_width = 36
post_height = 43

txt = Image.open('transparent.png')
txt_alpha = txt.convert("RGBA")

position = { "a": (0,0), "b": (1,0), "c": (2,0), "d": (3,0), "e": (4,0), "f": (5,0), "g": (6,0), "h": (7,0),
    "i": (8,0), "j": (9,0), "k": (10,0), "l": (11,0), "m": (12,0), "n": (13,0), "o": (14,0), "p": (15,0),
    "q": (0,1), "r": (1,1), "s": (2,1), "t": (3,1), "u": (4,1), "v": (5,1), "w": (6,1), "x": (7,1), "y": (8,1), "z": (9,2),
    "0": (0,2), "1": (1,2), "2": (2,2), "3": (3,2), "4": (4,2), "5": (5,2), "6": (6,2), "7": (7,2), "8": (8,2), "9": (9,2),
    " ": (9, 3)
}

def get_char(letter):
    if letter.lower() not in position:
        return
    letter = letter.lower()
    x,y = position[letter]
    base_x = letterfield_x+(letter_width+letter_spacing)*x
    base_y = letterfield_y+(letter_height+letter_spacing)*y
    letter_img = txt_alpha.crop((base_x, base_y, base_x+letter_width, base_y+letter_height))
    return letter_img.resize((post_width, post_height))

def make_meme(string):
    word_x = 240
    word_y = 625
    base = Image.open('garfield.jpeg')
    base_alpha = base.convert('RGBA')
    blank = Image.new("RGBA", size=base.size)
    for ch in string:
        letter = get_char(ch)
        if letter is not None:
            blank.paste(letter, box=(word_x, word_y), mask=letter)
        word_x += post_width+word_spacing

    tint = Image.new("RGBA", (blank.size), color=(0,0,255))
    blank = Image.blend(blank, tint, 0.3)
    blank = blank.filter(ImageFilter.BoxBlur(0.5))
    base_alpha.paste(blank, (0,0), blank)
    return base_alpha.convert("RGB")

def save_meme(string, fileobj):
    img = make_meme(string)
    img.save(fileobj, 'JPEG', quality=70)
    fileobj.seek(0)
    return fileobj
