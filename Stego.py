import time
import cv2
from Cryptodome.Cipher import ChaCha20
from Cryptodome.Random import get_random_bytes
import base64
from img_slct import select_cover_image
from progress_bar import en_progress,dec_progress
from termcolor import colored
from headline_art import art

def get_image():
    time.sleep(0.99)
    print("\nChoose your cover file...")
    time.sleep(0.99)
    img_path = select_cover_image()
    img = cv2.imread(img_path)
    return img

def get_secret_code():
    msg = input("\nEnter the secret message : ")
    return msg

def encrypt(message):
    rand_key = get_random_bytes(32)
    time.sleep(0.99)
    print("\nHere is your decryption key : ", end="")
    print(colored(base64.b64encode(rand_key).decode(), 'cyan'))
    cipher = ChaCha20.new(key=rand_key)
    ciphertext = cipher.encrypt(message.encode())
    bse_code = base64.b64encode(cipher.nonce + ciphertext).decode('ascii')
    stopper = "@END@"
    base_code = bse_code + stopper
    return base_code

def embed_image(message):
    image = get_image()
    height, width, _ = image.shape
    if len(message) > height * width * 3:
        raise ValueError("Message is too long for this image!")
    m, n, z = 0, 0, 0
    for i in range(len(message)):
        image[m, n, z] = ord(message[i])
        z += 1
        if z == 3:
            z = 0
            n += 1
            if n == width:
                n = 0
                m += 1
    cv2.imwrite("Encrypted.png", image)
    en_progress(">>> En")
    print("\n✅ Encrypted image generated successfully!")

def decrypt():
    img_path = select_cover_image()
    image = cv2.imread(img_path)
    height, width, _ = image.shape
    key = input("Decrypt key : ")
    dec_progress(">>> De")
    message = ""
    m, n, z = 0, 0, 0
    found = False
    stopper = "@END@"
    for row in image:
        for pixel in row:
            k, l, b = pixel
            message += chr(int(k)) + chr(int(l)) + chr(int(b))
            if stopper in message:
                found = True
                break
        if found:
            break
    if stopper in message:
        encrypted_message = message.split(stopper)[0]
    else:
        print("[❌] No valid end marker (@END@) found in extracted data.")
        return
    try:
        encrypted_bytes = base64.b64decode(encrypted_message)
        nonce = encrypted_bytes[:8]
        ciphertext = encrypted_bytes[8:]
        key = base64.b64decode(key)
        cipher = ChaCha20.new(key=key, nonce=nonce)
        decrypted_message = cipher.decrypt(ciphertext).decode()
        print("\n[🔓] Decrypted Message:", decrypted_message)
    except Exception as e:
        print("[❌] Decryption Failed:", str(e))

def start_enc():
    code = get_secret_code()
    enc_msg = encrypt(code)
    embed_image(enc_msg)

def main():
    cho = art()
    if cho == "1":
        print(colored("\n[🔒] Encryption Mode Activated!", 'green'))
        time.sleep(0.99)
        start_enc()
    elif cho == "2":
        print(colored("\n[🔓] Decryption Mode Activated!", 'yellow'))
        time.sleep(0.99)
        print("\nChoose your encrypted file...\n")
        decrypt()
    elif cho == "3":
        print(colored("\n[👋] Exiting Shadow-C20. Stay secure!", 'red'))
        exit()
    else:
        print(colored("\n[❌] Invalid choice! Please select 1, 2, or 3.", 'red'))

main()
