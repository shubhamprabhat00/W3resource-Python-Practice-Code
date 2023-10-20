# <!-- # https://www.w3resource.com/python-exercises/python-basic-exercises.php


# 7. Write a Python program that accepts a filename from the user and prints the extension of the file.
# Sample filename : abc.java
# Output : java

sample_filename = "abc.java"
f_extension = sample_filename.split(".")

print(f'File Extension:','.'+ f_extension[-1])