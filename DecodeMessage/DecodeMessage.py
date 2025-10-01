from email import message


def decode(message_file):
    #open file
    with open(message_file, 'r') as file:
        lines = file.readlines()
    
    decoded_message = []
    for line in lines:
        words = line.strip().split()[1:]
        decoded_message.append(words[-1])
    return ' '.join(decoded_message)

# test
decode_message = decode('message.txt')
print(decode_message)

    
