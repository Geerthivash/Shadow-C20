# Shadow-C20 – Secure Steganography & Encryption Tool

Shadow-C20 is a Python-based tool that enables secure message embedding inside images using steganography combined with modern encryption.  
It encrypts user messages with the ChaCha20 algorithm and then hides the encrypted output within image pixel data, supporting covert and tamper-resistant communication.

This project demonstrates hands-on skills in Python scripting, encryption workflows, file handling, and steganographic encoding.

---

## 🚀 Features

- **ChaCha20 Encryption**
  - Messages are encrypted using a modern stream cipher for confidentiality.
  - Random nonce is generated for each encryption operation.

- **Image Steganography**
  - Encrypted bytes are embedded into image pixel values.
  - Supports concealment while preserving image appearance.

- **Binary/Hashed Encoding**
  - Encrypted output is converted to formats that reduce detectability in MITM scenarios.

- **Message Extraction**
  - Tool supports both embedding and restoring encrypted messages from images.

---

## 🛠️ Tech Stack

- **Python 3**
- **cryptography** library (ChaCha20)
- **Pillow (PIL)** for image manipulation
- Binary encoding & bitwise data handling

---

## 📦 How It Works

1. User inputs a plaintext message.  
2. Message is encrypted using ChaCha20 and converted into binary format.  
3. Binary data is embedded into the least-significant bits (LSBs) of image pixels.  
4. Resulting image can be shared without revealing that data is embedded.  
5. Extraction process reads the modified pixel bits and decrypts the message.

---

## 📌 Purpose

Shadow-C20 was created to demonstrate:

Applied cryptography (ChaCha20 encryption)

Data encoding and binary-level manipulation

Image processing and steganographic design

Python scripting for security tooling

