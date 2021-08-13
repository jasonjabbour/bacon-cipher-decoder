# Bacon Cipher Decode

## Usage

```python
from bacon_cipher import bacon_cipher

bacon_cipher = bacon_cipher()
bacon_cipher.decode(message,upperCase)
```

### Background

Bacon's Cipher is as steganography technique used to hide messages in plain text. The plain text is identified into two font types. It is common to make the distinction between font types through bolding letters or capitalizing letters.

### Documentation 

```bacon_cipher``` implements the version of Bacon's cipher which I, J, U and V have unique patterns. The message passed in must be a string with no digits. Spaces are ignored and punctuation characters are treated as lowercase letters by default. The ```upperCase``` parameter defines which type capital letters will be classified as. One may pass in _A_ or _B_ into this input. 

### Examples

The encoded message to be decoded is: t**HI**s i**S** **A** t**ES**t **ME**s**S**a**GE** wi**T**h **BOL**d **FO**r a 

```python
bacon_cipher.decode('tHIs iS A tESt MEsSaGE wiTh BOLd FOr a')
```
Returned Value: TESTIT

If the encoded message is the opposite: **T**hi**S** **I**s a **T**es**T** me**S**s**A**ge **WI**t**H** bol**D** fo**R B**

```python
bacon_cipher.decode('ThiS Is a TesT meSsAge WItH bolD foR B','B')
```
Returned Value: TESTIT

