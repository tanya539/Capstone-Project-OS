# Viva Questions and Answers

**1. What is a Linux file permission?**  
It defines which users can read, modify or execute a file.

**2. What are Owner, Group and Others?**  
Owner is the file's user, Group means users in the file's group, and Others means all remaining users.

**3. What does `r` mean?**  
Read permission. Its numeric value is 4.

**4. What does `w` mean?**  
Write permission. Its numeric value is 2.

**5. What does `x` mean?**  
Execute permission. Its numeric value is 1.

**6. Explain `-rw-r-----`.**  
The first `-` indicates a regular file. Owner has read and write; Group has read; Others have no permission.

**7. What is the octal value of `-rw-r-----`?**  
640: Owner 6 (4+2), Group 4, Others 0.

**8. What does `chmod` do?**  
It changes file or directory permission bits on Unix-like systems.

**9. What does `chmod 640 file.txt` mean?**  
Owner gets read/write, Group gets read, Others get no access.

**10. What is least privilege?**  
Giving each user only the minimum access required.

**11. Why does the application show both symbolic and octal formats?**  
They represent the same permission settings in human-readable and numeric forms.

**12. Does this application change actual file permissions?**  
No. It generates the command only, so the user can review and execute it manually.

**13. Which GUI library is used?**  
Tkinter, Python's standard GUI library.

**14. Why is input quoting important?**  
It helps paths containing spaces or shell-special characters be treated as one argument.

**15. What is one limitation?**  
The current version does not implement special permission bits or change ownership.
