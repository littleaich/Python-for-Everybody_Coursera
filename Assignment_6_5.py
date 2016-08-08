text = "X-DSPAM-Confidence:    0.8475";

pos_space = text.find(' ');
num_str = text[pos_space:]
num_str = num_str.strip() # strip spaces from begin and end of string
num = float(num_str)

print num
