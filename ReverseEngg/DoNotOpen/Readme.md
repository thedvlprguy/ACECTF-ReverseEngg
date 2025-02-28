# CAPTURE THE FLAG - DONOTOPEN  

---

## CTF Description  
A strange script file seems to be hiding something important, but it doesn’t want to cooperate. It’s obfuscated, tampered with, and asks for a password. Can you figure out how to unlock the mystery and reveal the hidden flag?  

---

## How to Find the Flag  

1. **Check for Hidden Content**  
   Run the following command to look for readable text inside the file:  

   ```bash
   strings DONTOPEN
   ```

   This reveals that a script named `pythonscript.py` is hidden inside the file.  

2. **Analyze the File Structure**  
   Use `binwalk` to check for any embedded files:  

   ```bash
   binwalk DONTOPEN
   ```

   The results show that the `DONTOPEN` file contains compressed data at offset `0x2B5`. The original name of this compressed data is `pythonscript.py`, meaning that the Python script is stored inside but needs to be extracted.  

3. **Extract the Compressed Script**  
   To extract the compressed data, use the `dd` command:  

   ```bash
   dd if=DONTOPEN of=pythonscript.gz bs=1 skip=693
   ```

   This will create a file named `pythonscript.gz`.  

4. **Decompress the Script**  
   Now, extract the gzip file:  

   ```bash
   gzip -d pythonscript.gz
   ```

   This will give you a file named `pythonscript`.  

5. **Check the Python Script Content**  
   Open the script to find any useful information:  

   ```bash
   cat pythonscript
   ```

   In the script, you will find a password:  

   ```
   ACE@SE7EN
   ```

6. **Run the Python Script**  
   Now, execute the script using:  

   ```bash
   python3 pythonscript
   ```

   - The script first redirects you to a website: **https://vipsace.org/**  
   - Then, it asks for a **PIN** in the terminal.  

7. **Enter the Correct PIN**  
   When prompted, enter the password:  

   ```
   ACE@SE7EN
   ```

8. **Get the Flag**  
   After entering the correct password, the terminal will reveal the flag:  

   ```
   ACE{e2e3619b630b3be9de762910fd58dba7}
   ```  

---

## Conclusion  
By carefully analyzing and extracting hidden data, we were able to uncover the Python script, find the correct password, and retrieve the flag. This challenge shows how important it is to understand file structures and extraction techniques in Capture The Flag (CTF) competitions.  

Happy hacking! 🚀