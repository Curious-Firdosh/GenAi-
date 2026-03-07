import tiktoken 

enc = tiktoken.encoding_for_model('gpt-4o')

text = "Hey There! My name is Piyush Garg"


tokens = enc.encode(text)

print(f"TOKENS : {tokens}")

decoded = enc.decode([25216, 3234, 0, 3676, 1308, 382, 398, 3402, 1776, 170679])

print("Decoded Tokens : " , decoded)