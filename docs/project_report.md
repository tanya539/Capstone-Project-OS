# Project Report: Linux File Permission Manager

## 1. Abstract
Linux File Permission Manager is a desktop-based educational tool that helps users understand Linux file permissions. It allows a user to select Read, Write and Execute permissions separately for Owner, Group and Others. The application displays the symbolic permission string, calculates the octal value and generates the corresponding `chmod` command.

## 2. Problem Statement
Linux permissions are often difficult for beginners to interpret. Users may find it confusing to convert permission choices into symbolic notation and numeric `chmod` values. This project provides an interactive way to understand and generate the command.

## 3. Objectives
- Understand the Owner, Group and Others permission model.
- Select read, write and execute access independently.
- Convert selected permissions into symbolic notation.
- Calculate the equivalent octal permission.
- Generate and copy the appropriate `chmod` command.
- Demonstrate the principle of least privilege.

## 4. Technology Used
- Programming language: Python
- GUI library: Tkinter
- Testing: Python `unittest`
- Platform: Linux, Windows and macOS (subject to Tkinter availability)

## 5. Operating System Concepts
- File access permissions
- User / group / others
- Read (`r`), write (`w`) and execute (`x`) bits
- Symbolic notation (for example `-rw-r-----`)
- Octal notation (for example `640`)
- `chmod` utility
- Least privilege

## 6. Working
Each permission has a numeric value: Read = 4, Write = 2 and Execute = 1. For each role, the application adds the values of selected permissions. The three resulting digits are arranged in Owner, Group, Others order.

For the assignment example:
- Owner: Read + Write = 4 + 2 = 6
- Group: Read = 4
- Others: No permission = 0

Therefore:
- Symbolic: `-rw-r-----`
- Octal: `640`
- Command: `chmod 640 'myfile.txt'`

## 7. Modules
1. Permission selection: checkboxes for each role and permission.
2. Symbolic preview: builds the nine permission characters.
3. Octal calculator: calculates one digit per role.
4. Command generator: combines the octal value with the target path.
5. Clipboard utility: copies the generated command.
6. Reset utility: restores the example configuration.

## 8. Algorithm
1. Start the application.
2. Read the selected permissions for Owner.
3. Add 4 for Read, 2 for Write and 1 for Execute when selected.
4. Repeat for Group and Others.
5. Convert each selected permission to `r`, `w`, `x`; use `-` when not selected.
6. Prefix the nine characters with `-` to represent a regular file.
7. Join the three numeric totals to create the octal mode.
8. Generate `chmod <octal> <file-path>`.
9. Display the updated result whenever a checkbox or file path changes.

## 9. Test Cases
| Test | Owner | Group | Others | Expected octal |
|---|---|---|---|---|
| Assignment example | rw- | r-- | --- | 640 |
| Full access | rwx | rwx | rwx | 777 |
| Read only | r-- | r-- | r-- | 444 |
| No access | --- | --- | --- | 000 |
| Owner execute only | --x | --- | --- | 100 |

## 10. Least Privilege
The least privilege principle means giving users only the permissions needed for their tasks. For example, a private file may allow its owner to read and write while giving no access to group members or others.

## 11. Limitations
- The application generates commands but does not execute them.
- It models regular-file permissions and does not display special bits such as setuid, setgid or sticky bit.
- It does not change file ownership; `chown` is outside the current scope.

## 12. Future Scope
- Add directory permission explanations.
- Add special permission bits.
- Add a permission-string parser.
- Add a preview for recursive permission commands.
- Add an optional Linux-only apply feature with confirmation.

## 13. Conclusion
The project provides a simple interactive way to learn Linux file permissions and generate `chmod` commands. It connects the theoretical permission model with a practical operating-system utility.
