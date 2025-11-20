import pytest
from src.hamming import hamming_distance

def test_hamming_distance_counts_correct_number_diffs():
    # Arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CATCGTAATGACGGCCT"

    # Act
    result = hamming_distance(strand1, strand2)

    # Assert
    assert result == 7

def test_hamming_distance_all_letters_different():
    # Arrange
    strand1 = "GAGCCTACTAACGGGAT"
    strand2 = "CGTAGCGAAGGTACCCA"

    # Act
    result = hamming_distance(strand1, strand2)

    # Assert
    assert result == 17

def test_hamming_distance_raises_error_for_unequal_lengths():
    # Arrange
    strand1 = "GAG"
    strand2 = "G"

    result = hamming_distance(strand1, strand2)

    assert result is None

def test_hamming_distance_one_empty_string_returns_none():
    # Arrange
    strand1 = ""
    strand2 = ""

    result = hamming_distance(strand1, strand2)

    assert result == 0

def test_hamming_distance_empty_strings_returns_0():
    # Arrange
    strand1 = ""
    strand2 = ""

    result = hamming_distance(strand1, strand2)

    assert result == 0

def test_distance_is_zero_for_identical():
    # Arrange
    strand1 = "GAG"
    strand2 = "GAG"

    # Act
    result = hamming_distance(strand1, strand2)

    # Assert
    assert result == 0