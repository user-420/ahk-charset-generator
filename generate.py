# "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"
# "1","2","3","4","5","6","7","8","9","0","!","@","#","$","%","^","&","*","(",")"

import os


def clear():
	os.system('cls' if os.name == 'nt' else 'clear')


alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u",
			"v", "w", "x", "y", "z", "A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P",
			"Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]

numbers_symbols = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0","!","@","#","$","%","^","&","*","(",")"]

charsets = [
	["𝔞", "𝔟", "𝔠", "𝔡", "𝔢", "𝔣", "𝔤", "𝔥", "𝔦", "𝔧", "𝔨", "𝔩", "𝔪", "𝔫", "𝔬", "𝔭", "𝔮", "𝔯", "𝔰", "𝔱", "𝔲", "𝔳", "𝔴",
	 "𝔵", "𝔶", "𝔷", "𝔄", "𝔅", "ℭ", "𝔇", "𝔈", "𝔉", "𝔊", "ℌ", "ℑ", "𝔍", "𝔎", "𝔏", "𝔐", "𝔑", "𝔒", "𝔓", "𝔔", "ℜ", "𝔖", "𝔗",
	 "𝔘", "𝔙", "𝔚", "𝔛", "𝔜", "ℨ", "gothic"],  # "gothic"
	["𝖆", "𝖇", "𝖈", "𝖉", "𝖊", "𝖋", "𝖌", "𝖍", "𝖎", "𝖏", "𝖐", "𝖑", "𝖒", "𝖓", "𝖔", "𝖕", "𝖖", "𝖗", "𝖘", "𝖙", "𝖚", "𝖛", "𝖜",
	 "𝖝", "𝖞", "𝖟", "𝕬", "𝕭", "𝕮", "𝕯", "𝕰", "𝕱", "𝕲", "𝕳", "𝕴", "𝕵", "𝕶", "𝕷", "𝕸", "𝕹", "𝕺", "𝕻", "𝕼", "𝕽", "𝕾", "𝕿",
	 "𝖀", "𝖁", "𝖂", "𝖃", "𝖄", "𝖅", "gothic_bold"],  # "gothic_bold"
	["𝒶", "𝒷", "𝒸", "𝒹", "𝑒", "𝒻", "𝑔", "𝒽", "𝒾", "𝒿", "𝓀", "𝓁", "𝓂", "𝓃", "𝑜", "𝓅", "𝓆", "𝓇", "𝓈", "𝓉", "𝓊", "𝓋", "𝓌",
	 "𝓍", "𝓎", "𝓏", "𝒜", "𝐵", "𝒞", "𝒟", "𝐸", "𝐹", "𝒢", "𝐻", "𝐼", "𝒥", "𝒦", "𝐿", "𝑀", "𝒩", "𝒪", "𝒫", "𝒬", "𝑅", "𝒮", "𝒯",
	 "𝒰", "𝒱", "𝒲", "𝒳", "𝒴", "𝒵", "cursive"],  # "cursive"
	["𝓪", "𝓫", "𝓬", "𝓭", "𝓮", "𝓯", "𝓰", "𝓱", "𝓲", "𝓳", "𝓴", "𝓵", "𝓶", "𝓷", "𝓸", "𝓹", "𝓺", "𝓻", "𝓼", "𝓽", "𝓾", "𝓿", "𝔀",
	 "𝔁", "𝔂", "𝔃", "𝓐", "𝓑", "𝓒", "𝓓", "𝓔", "𝓕", "𝓖", "𝓗", "𝓘", "𝓙", "𝓚", "𝓛", "𝓜", "𝓝", "𝓞", "𝓟", "𝓠", "𝓡", "𝓢", "𝓣",
	 "𝓤", "𝓥", "𝓦", "𝓧", "𝓨", "𝓩", "cursive_bold"],  # "cursive_bold"
	["𝕒", "𝕓", "𝕔", "𝕕", "𝕖", "𝕗", "𝕘", "𝕙", "𝕚", "𝕛", "𝕜", "𝕝", "𝕞", "𝕟", "𝕠", "𝕡", "𝕢", "𝕣", "𝕤", "𝕥", "𝕦", "𝕧", "𝕨",
	 "𝕩", "𝕪", "𝕫", "𝔸", "𝔹", "ℂ", "𝔻", "𝔼", "𝔽", "𝔾", "ℍ", "𝕀", "𝕁", "𝕂", "𝕃", "𝕄", "ℕ", "𝕆", "ℙ", "ℚ", "ℝ", "𝕊", "𝕋",
	 "𝕌", "𝕍", "𝕎", "𝕏", "𝕐", "ℤ", "outlines"],  # "outlines"
	["ａ", "ｂ", "ｃ", "ｄ", "ｅ", "ｆ", "ｇ", "ｈ", "ｉ", "ｊ", "ｋ", "ｌ", "ｍ", "ｎ", "ｏ", "ｐ", "ｑ", "ｒ", "ｓ", "ｔ", "ｕ", "ｖ", "ｗ",
	 "ｘ", "ｙ", "ｚ", "Ａ", "Ｂ", "Ｃ", "Ｄ", "Ｅ", "Ｆ", "Ｇ", "Ｈ", "Ｉ", "Ｊ", "Ｋ", "Ｌ", "Ｍ", "Ｎ", "Ｏ", "Ｐ", "Ｑ", "Ｒ", "Ｓ", "Ｔ",
	 "Ｕ", "Ｖ", "Ｗ", "Ｘ", "Ｙ", "Ｚ", "fullwidth"],  # "fullwidth"
	["ᵃ", "ᵇ", "ᶜ", "ᵈ", "ᵉ", "ᶠ", "ᵍ", "ʰ", "ⁱ", "ʲ", "ᵏ", "ˡ", "ᵐ", "ⁿ", "ᵒ", "ᵖ", "q", "ʳ", "ˢ", "ᵗ", "ᵘ", "ᵛ", "ʷ",
	 "ˣ", "ʸ", "ᶻ", "ᴬ", "ᴮ", "ᶜ", "ᴰ", "ᴱ", "ᶠ", "ᴳ", "ᴴ", "ᴵ", "ᴶ", "ᴷ", "ᴸ", "ᴹ", "ᴺ", "ᴼ", "ᴾ", "Q", "ᴿ", "ˢ", "ᵀ",
	 "ᵁ", "ⱽ", "ᵂ", "ˣ", "ʸ", "ᶻ", ["¹","²","³","⁴","⁵","⁶","⁷","⁸","⁹","⁰","!","@","#","$","%","^","&","*","⁽","⁾"], "superscript"],  # "superscript", doesn't have the letter q, wtf unicode consortium?
	["𝘢", "𝘣", "𝘤", "𝘥", "𝘦", "𝘧", "𝘨", "𝘩", "𝘪", "𝘫", "𝘬", "𝘭", "𝘮", "𝘯", "𝘰", "𝘱", "𝘲", "𝘳", "𝘴", "𝘵", "𝘶", "𝘷", "𝘸",
	 "𝘹", "𝘺", "𝘻", "𝘈", "𝘉", "𝘊", "𝘋", "𝘌", "𝘍", "𝘎", "𝘏", "𝘐", "𝘑", "𝘒", "𝘓", "𝘔", "𝘕", "𝘖", "𝘗", "𝘘", "𝘙", "𝘚", "𝘛",
	 "𝘜", "𝘝", "𝘞", "𝘟", "𝘠", "𝘡", "italic"]  # "italic"
	# todo: add more lol
]


def print_options(wrong_p):
	clear()
	print(
		"Pick a charset\n1) 𝔊𝔬𝔱𝔥𝔦𝔠 (gothic)\n2) 𝕲𝖔𝖙𝖍𝖎𝖈 𝕭𝖔𝖑𝖉 (gothic bold)\n3) 𝒞𝓊𝓇𝓈𝒾𝓋𝑒 ("
		"cursive)\n4) 𝓒𝓾𝓻𝓼𝓲𝓿𝓮 𝓑𝓸𝓵𝓭 (cursive bold)\n5) 𝕆𝕦𝕥𝕝𝕚𝕟𝕖𝕤 (outlines)\n6) Ｆｕｌｌｗｉｄｔｈ ("
		"fullwidth)\n7) ˢᵘᵖᵉʳˢᶜʳⁱᵖᵗ (superscript)\n8) 𝘐𝘵𝘢𝘭𝘪𝘤 (italic)")
	if wrong_p:
		print("\n!ERROR! Input a number from 1-8.\n")


wrong = False
option = None

while 1:
	if not option:
		print_options(wrong)
		option = input("\nPick an option (1-8): ")
	else:
		try:
			option = int(option)
			if option > 8 or option < 1:
				wrong = True
				option = None
				continue
			else:
				clear()
				break
		except Exception as e:
			wrong = True
			option = None
			continue

clear()
print("Pick a key to pause the script (any letter, number, F key, else look here: https://www.autohotkey.com/docs/v1/KeyList.htm)")
print("(*this script does not check if this is a valid key, that's on you*)\n")
pause_key = input("Key: ")

# ok now we actually do the generation

option = option - 1 # because lists (aka arrays aka tables) start at 0 in py

if type(charsets[option][52]) == list:
	charset_name = charsets[option][53]
else:
	charset_name = charsets[option][52]

ahk_file = open(charset_name + "_charset.ahk", "w", encoding="utf-8")

ahk_file.write("; generated by monke's charset generator script\n\n")

ahk_file.write(pause_key+"::Suspend,Toggle\n")

i = 0

clear()

print("Creating script... (charset: "+ charset_name + ")")
for letter in alphabet:

	ordinal = ''.join(r'{:04X}'.format(ord(charsets[option][i])))

	if i > 25:
		ahk_file.write("+" + letter + "::Send {U+" + str(ordinal) + "}" + "\n")
	else:
		ahk_file.write(letter + "::Send {U+" + str(ordinal) + "}" + "\n")
	i = i+1

i = 0

for char in numbers_symbols:
	if type(charsets[option][52]) != list:
		break

	if i < 10:
		ordinal = ''.join(r'{:04X}'.format(ord(charsets[option][52][i])))
		ahk_file.write(char + "::Send {U+" + str(ordinal) + "}" + "\n")
		i = i + 1
	else:
		ordinal = ''.join(r'{:04X}'.format(ord(charsets[option][52][i])))
		ahk_file.write("+" + char + "::Send {U+" + str(ordinal) + "}" + "\n")
		i = i + 1




ahk_file.close()

the_slash = "\\" if os.name == "nt" else "/"

print("Done!\nSaved to: " + os.path.dirname(os.path.realpath(__file__)) + the_slash + charset_name + "_charset.ahk")
