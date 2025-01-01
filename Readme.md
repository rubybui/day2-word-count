# ccwc: A Simple Command-Line Word Counter

`ccwc` is a lightweight command-line tool that counts lines, words, bytes, and characters in a file or from standard input, similar to the `wc` command.

---

## Features
- **Count Lines**: Use `-l` to count the number of lines.
- **Count Words**: Use `-w` to count the number of words.
- **Count Bytes**: Use `-c` to count the number of bytes.
- **Count Characters**: Use `-m` to count the number of characters.
- **Default Behavior**: Without options, `ccwc` counts lines, words, and bytes.
- **Standard Input Support**: Reads from standard input if no file is specified.

---

## Installation

Step 1: Clone or download the repository containing `ccwc`  
```git clone https://github.com/rubybui/day2-wordcount.git```
```cd day2-word-count```

Step 2: Install the tool using `pip`  
```pip install .```

Step 3: Verify the installation by running  
```ccwc -h```
This should display the help message for the tool.

---

## Usage

### Count Lines, Words, and Bytes (Default Behavior)
```ccwc test.txt```
Output:  
`    7145   58164  342190 test.txt`

### Count Specific Metrics
- Count lines:  
  ```ccwc -l test.txt```
- Count words:  
  ```ccwc -w test.txt```
- Count bytes:  
  ```ccwc -c test.txt```
- Count characters:  
  ```ccwc -m test.txt```

### Read from Standard Input
You can pipe input to `ccwc`:  
```echo "Hello World\nThis is a test" | ccwc```

---

## Uninstallation

To uninstall `ccwc`, simply run  
```pip uninstall ccwc```

---

## Development

This is a challenge in https://codingchallenges.fyi/challenges/challenge-wc
---
