import sys
import numpy as np


def extract_x_and_y_from_file(examples_file_path):
    """
    :param examples_file_path: A string containing the path to the examples/training set file.
    :return: Array of instances (which are also an array of literals) and an array of tags.
    """
    training_set = np.loadtxt(examples_file_path)

    return [line[:-1] for line in training_set], [line[-1] for line in training_set]


def hypothesis_wrong(h, instance_representation):
    """
    The hypothesis is wrong if a given instance whose y is 1 is not a subset of the hypothesis.
    :param h: array of tuples of literals index and condition (true/false)
    :param instance_representation:
    :return:
    """
    return not h.issubset(instance_representation)


def instance_representation(instance):
    """
    :param instance: an array of literal's condition (1 for true, 0 for false)
    :return: a set of tuples of literal index and condition
    """
    return set(zip(range(len(instance)), instance))


def algorithm2(x, y):
    instance_length = len(x[0])
    h = create_all_wrong_hypothesis(instance_length)

    for example_index, instance in enumerate(x):
        if y[example_index] == 1:
            representation = instance_representation(instance)
            if hypothesis_wrong(h, representation):
                h = representation.intersection(h)

    return h


def create_all_wrong_hypothesis(size):
    """
    create an all wrong hypothesis where each literal is existing both in it's form and negative form
    :param size:
    :return:
    """
    return set(zip(sorted(2 * range(size)), [0, 1] * size))


def pretty_print_hypothesis(h):
    for item in sorted(h, key=lambda x: x[0]):
        if item[1] == 1:
            outputFile.write("x" + str(item[0] + 1) + ",")
        elif item[1] == 0:
            outputFile.write("not(x" + str(item[0] + 1) + "),")


if __name__ == '__main__':
    # inputFilePath = "D:\Projects\MachineLearningEx1\example2.txt"
    inputFilePath = sys.argv[1]
    outputFilePath = "./output.txt"

    outputFile = open(outputFilePath, "w+")

    x, y = extract_x_and_y_from_file(inputFilePath)
    pretty_print_hypothesis(algorithm2(x, y))
