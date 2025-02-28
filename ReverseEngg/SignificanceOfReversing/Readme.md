# Capture The Flag -  Significance of Reversing Using Reverse Engineering

---

## Things You Need to Reverse using Reverse , You should know atleast one lang of these languages: 
- C++(For Decryption of Complex Files and converting them to executable ELF file)
- Python(For Reversing the complex string You Get , To Find & Capture the flag)
- Assembly(For Using it with crptography)

---

## Problem Statement:
Over the years, we hackers have been reversing stuff, thinking we understand how everything works and feel good about it. But, sometimes it feels like do we really understand what reversing means in mordern days? Anyways, here's a PNG, let's see if you can reverse your way out of this one.

## Given Data:
Reverseme.png
 

## How to decrypt that: 
- First Check the filetype using this command`file Reverseme.png ` then move to find images inner details using `binwalk -e Reverseme.png`


## Checking the final input and flag: 
- Run `solve.py` to get and reverse file like `Reverseme.ELF` 
- Then execute the same `Reverseme.ELF` using `chmod +x reversed_file.LEF`
- Then it's ready to decrypt your lovely flag:

## After Executing We'll get the flag easily:
- `Decrypted string: ACECTF{w3_74lk_4b0u7_r3v3r53}`
