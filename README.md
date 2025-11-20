# Hamming

## Problem Statment

Imagine working on software that analyzes mutations in DNA.

Create a function named `hamming_distance` that calculates the number of differences between two DNA strands (aka two strings). This method should take in two different DNA strands as inputs and the return value should be the number of differences between each string. 
- Input strings are guaranteed to be non-empty and only contain the characters “G”, “A”, “T”, & “C”. 
- A hamming distance can only be calculated if the inputs are the same length.
  - If the input lengths are different, return `None`. 

For example, given these two DNA strands (strings), `hamming_distance` should return `7` because there are 7 differences:

|Example Input | Expected Ouput |
|--|--|
|`strand1 = "GAGCCTACTAACGGGAT"` <br> `strand2 = "CATCGTAATGACGGCCT"` | `7`|

Explanation:
```
Strand #1:   GAGCCTACTAACGGGAT
Strand #2:   CATCGTAATGACGGCCT
Differences: ^ ^ ^  ^ ^    ^^
             7 in total
```

(This problem is sourced from [http://rosalind.info/problems/hamm/](http://rosalind.info/problems/hamm/))

## One-Time Project Setup

Follow these directions once, at the beginning of your project:


1. Navigate to your projects folder named `projects`.

If you followed Ada's recommended file system structure from the Intro to Dev Environment lesson in Learn, you can navigate to your projects folder with the following command:

```bash
$ cd ~/Developer/projects
```

2. In Github click on the "Fork" button in github and fork the repository to your Github account.  This will make a copy of the project in your github account. 

3. "Clone" (download a copy of this project) into your projects folder. This command makes a new folder called `hamming`, and then puts the project into this new folder.  Make sure you are cloning from your copy of the project and not the class version (ada-cX).

```bash
$ git clone ...
```

Use `ls` to confirm there's a new project folder

4. Move your location into this project folder

```bash
$ cd adagrams-py
```

5. Create a virtual environment named `venv` for this project:

```bash
$ python3 -m venv venv
```

6. Activate this environment:

```bash
$ venv/Scripts/activate
```

Verify that you're in a python3 virtual environment by running:

- `$ python --version` should output a Python 3 version
- `$ pip --version` should output that it is working with Python 3

7. Install dependencies once at the beginning of this project with

```bash
# Must be in activated virtual environment
$ pip install -r requirements.txt
```