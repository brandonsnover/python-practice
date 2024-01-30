def decode(message_file):
    number_word_map = {}
    with open(message_file, 'r') as file:
        for line in file:
            number, word = line.split(' ', 1)
            number_word_map[int(number)] = word.strip()

    pyramid_keys = []
    counter, step = 1, 2
    while counter in number_word_map:
        pyramid_keys.append(counter)
        counter += step
        step += 1

    decoded_message = ' '.join(number_word_map[key] for key in pyramid_keys if key in number_word_map)
    return decoded_message


message_file = 'coding_qual_input.txt' 
decoded_message = decode(message_file)
print(decoded_message)
