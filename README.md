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

8. You should see a few directories on the side. The testing directory holds the tests in a file called `test_hamming.py`. The `src` directory holds a file called `hamming.py`. That file is where you should write the function. The function definition is provided.
   
# Run Tests

Follow the steps to run your tests. There are two options.

1. Open up a terminal and run the command `pytest`. You should get a list of the tests with "ERROR" before them. Or, if you have written the code correctly, they should all pass.

2. Open up the flask icon on the side and click "Configure Python Tests". A dropdown should appear from the top of the panel. Select "pytest" and then "tests". The testing pane should show up on the left side. You can run the tests by clicing the play button at the top or the play button that pops up for any individual test. If the tests turn green, they are passing. If they turn red, they are failing.