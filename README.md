# Ceasar-Cipher
A function which carries out a Ceasar Cipher, including encryption and decryption.
<br/>
Multiple viable Ceaser Cipher functions are included, though the most potable option is at the end of the code.
# Usage
First, please ensure you have the modules/libraries ```english_dictionary``` and ```string``` installed.
You can assume you have them installed by default, though if it throws an error you can install them manually by running the following commands:
```
pip install english_words
pip install string
```
Next, run the following command through terminal:
<br/>
```
py Ceasar-Cipher.py
```
Enter any of the three options, which are:
```
a | Encrypt</li>
b | Decrypt - with a shift </li>
c | Decrypt - without a shift </li>
```
From there, follow the instructions provided by the program. <br/>

Also, please note that all of the commands above should work universally, in any terminal as long as you have python installed.
# Features
<ul>
  <li>Encryption</li>
  <li>Decryption</li>
  <li>Includes the option to decrypt without a shift (key) - Explained further below</li>
  <li>Allows you to include your own alphabet for the program to use to encrypt/decrypt with</li>
</ul> <br/>
<p>
The decryption (without a shift/key) option is a less efficient option than decryption (with a shift/key) as it will run through every possible shift, and only select the resulting decrypted text which has one of its words in the english dictionary to display, though if no valid word is found, it will display all of the possible decrypted versions of the text, along with their corresponding shifts, and therefore it is slower and less efficient than the option with a key, but all the more powerful.
  
Additionally, the code an be altered to run different included functions, though by default it will run the most efficient and featured function.
</p>

# Issues
If you find any issues, please contact me.
<br/>
Possible issues may include not having the correct python version, or not having the used modules installed.
<br/>
