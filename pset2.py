{
  "nbformat": 4,
  "nbformat_minor": 0,
  "metadata": {
    "colab": {
      "name": "Day2_MoreAboutPython.ipynb",
      "provenance": [],
      "include_colab_link": true
    },
    "kernelspec": {
      "name": "python3",
      "display_name": "Python 3"
    },
    "language_info": {
      "name": "python"
    }
  },
  "cells": [
    {
      "cell_type": "markdown",
      "metadata": {
        "id": "view-in-github",
        "colab_type": "text"
      },
      "source": [
        "<a href=\"https://colab.research.google.com/github/ttiffanywin/datascience/blob/main/pset2.py\" target=\"_parent\"><img src=\"https://colab.research.google.com/assets/colab-badge.svg\" alt=\"Open In Colab\"/></a>"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "# Functions, loops, and more\n",
        "### Writing a Python program. First things to know:\n",
        "A program is a list of instructions. The instructions read line by line and executed. \n",
        "Indentation matters: instructions that are have to be indented \n",
        "We have differet \"types\" of instructions: arithmetic operations, assignations, input/output, loops, functions and many more. \n",
        "If you have any question, ask Google!"
      ],
      "metadata": {
        "id": "hGogxa8SSalE"
      }
    },
    {
      "cell_type": "code",
      "execution_count": null,
      "metadata": {
        "id": "3LT-FQpESRjD"
      },
      "outputs": [],
      "source": [
        "# this is an example of a Python program. It finds all the prime numbers in the input range. \n",
        "\n",
        "# Take input from the user and assign the value to variables\n",
        "lower = int(input(\"Enter lower range: \"))\n",
        "upper = int(input(\"Enter upper range: \"))\n",
        "\n",
        "# a for loop\n",
        "for num in range(lower, upper + 1):\n",
        "    \n",
        "    # a conditional expression, checks if the number num is greater than 1\n",
        "    if num > 1:\n",
        "    \n",
        "        # an initial assumption: it is prime\n",
        "        prime = True\n",
        "\n",
        "        # another for loop\n",
        "        for i in range(2, num):\n",
        "            \n",
        "            # another conditional to check if it has divisors\n",
        "            if (num % i) == 0:\n",
        "                prime = False\n",
        "\n",
        "                # a break\n",
        "                break\n",
        "\n",
        "        # another confitiona, to print the result if it is prime\n",
        "        if prime:\n",
        "            print(num)"
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Functions\n",
        "A function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result. To define a new function, use `def`."
      ],
      "metadata": {
        "id": "_3if8KwQaQsD"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# this function is equivalent to f(z) = z^3\n",
        "def cube (z):\n",
        "    return z*z*z\n",
        "    \n",
        "# this function is equivalent to f(z) = 1/z\n",
        "def inverse (z):\n",
        "    return 1./z\n",
        "    \n",
        "# this function is equivalent to f(z) = z^2 + 2*z + 1\n",
        "def a_polynomial (z):\n",
        "    return z**2 + 2*z + 1"
      ],
      "metadata": {
        "id": "lOTlHEMkaHQA"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "Once defined, functions can be called any time. To call a function, the input has to be in brackets `()`."
      ],
      "metadata": {
        "id": "toEsvZRoayql"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# assign to a the value of 9\n",
        "a = 9\n",
        "#call the functions defined above with a as input\n",
        "print(cube(a), inverse(a), a_polynomial(a))"
      ],
      "metadata": {
        "id": "bGG8ABdKa2al",
        "outputId": "da95ac3e-0e58-418c-e90e-772fc1b3337e",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "729 0.1111111111111111 100\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "Functions can have more than one argument:"
      ],
      "metadata": {
        "id": "CxKfv44RbFF8"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "def average (z,w):\n",
        "    return (z+w)/2\n",
        "\n",
        "print(average(10, 50))"
      ],
      "metadata": {
        "id": "ujvBJdgOa6t6",
        "outputId": "88221722-dcb8-4213-d3d6-9983b9d75007",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "30.0\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Loops\n",
        "#### The 'for' loop\n",
        "It is possible to repeat the same indented block a certain ammount of times by using the instruction `for`."
      ],
      "metadata": {
        "id": "DOtzpN8ibOvG"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# print all numbers from 0 to 9\n",
        "# this repeats the instruction \"print(i)\" 10 times, for values of i from 0 to 9. \n",
        "for i in range(10):\n",
        "       print(i)"
      ],
      "metadata": {
        "id": "x3CTZNQ3bOUR",
        "outputId": "720939ff-c27a-4a43-9ce1-5c77f24b3df9",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "0\n",
            "1\n",
            "2\n",
            "3\n",
            "4\n",
            "5\n",
            "6\n",
            "7\n",
            "8\n",
            "9\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# add all numbers from 0 to 9\n",
        "sum = 0\n",
        "for i in range(10):\n",
        "    sum = sum + i\n",
        "print(sum)"
      ],
      "metadata": {
        "id": "4oo3DMmXbJRB",
        "outputId": "b07e5581-fb42-43b2-f303-1da27f85f9ab",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "45\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "#Here 'a' takes values in the given list\n",
        "for a in [1, 2, 5, \"hi\", -1./9, False]:\n",
        "    print(\"This is an example\")\n",
        "    print(\"Now a has the value:\", a)"
      ],
      "metadata": {
        "id": "SbhwSi9Bb5Ge",
        "outputId": "ca75dfe7-c585-4bdd-dcec-a21d0d2786f8",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "This is an example\n",
            "Now a has the value: 1\n",
            "This is an example\n",
            "Now a has the value: 2\n",
            "This is an example\n",
            "Now a has the value: 5\n",
            "This is an example\n",
            "Now a has the value: hi\n",
            "This is an example\n",
            "Now a has the value: -0.1111111111111111\n",
            "This is an example\n",
            "Now a has the value: False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "markdown",
      "source": [
        "### Conditional statements\n",
        "The conditional `if/else` checks if the given condition is true or false. If it is true, the indented block below is executed, if it is false, it is skipped."
      ],
      "metadata": {
        "id": "K5w8F0UQcFwT"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# read input \n",
        "a = input()\n",
        "\n",
        "# check if the condition is true, this will be printed\n",
        "if a == 3:\n",
        "    print(\"a is equal to 3\")\n",
        "\n",
        "# if it is false, then this will be printed\n",
        "else:\n",
        "    print(a, \"is not equal to 3\")"
      ],
      "metadata": {
        "id": "9ZlmqccAb_2N"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "code",
      "source": [
        "a = 20\n",
        "\n",
        "# loop through all numbers from 1 to 10, \n",
        "for i in range(1,11):\n",
        "\n",
        "    # check if the remainder of 20 divided by that number is 0\n",
        "    if a%i == 0:\n",
        "\n",
        "        # in such case, print the number.\n",
        "        print(a, \"is divisible by\", i)"
      ],
      "metadata": {
        "id": "SxSyZhOscXtB"
      },
      "execution_count": null,
      "outputs": []
    },
    {
      "cell_type": "markdown",
      "source": [
        "## Homework"
      ],
      "metadata": {
        "id": "fpzW44GrdhUk"
      }
    },
    {
      "cell_type": "code",
      "source": [
        "# Use this cell for your code\n",
        "\n",
        "def average(a1):\n",
        "  sum = 0\n",
        "  for i in range(len(a1)):\n",
        "    sum += a1[i]\n",
        "  avg = sum/len(a1)\n",
        "  return avg\n",
        "\n",
        "a1 = [1,2,3,4]\n",
        "avg = average(a1)\n",
        "print(avg)"
      ],
      "metadata": {
        "id": "rB2eUZSydjEZ",
        "outputId": "8164976d-8fb8-4fe2-eb31-a7f0498b9ee0",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "2.5\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Use this cell for your code\n",
        "\n",
        "def common(a1, a2):\n",
        "  end = False\n",
        "\n",
        "  for v in a1:\n",
        "   for x in a2:\n",
        "      if v == x:\n",
        "        end = True\n",
        "      return end\n",
        "  return end\n",
        "\n",
        "a1=[1,2,3,4]\n",
        "a2=[5,4,7,10]\n",
        "\n",
        "print(common(a1,a2))\n"
      ],
      "metadata": {
        "id": "BqJ6a2AGdzzg",
        "outputId": "39883a9e-8e41-4167-a2c5-65819fc2afcf",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": 1,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "False\n"
          ]
        }
      ]
    },
    {
      "cell_type": "code",
      "source": [
        "# Use this cell for your code\n",
        "\n",
        "def zerooo(a):\n",
        "  a = [0,1,0,2,3]\n",
        "\n",
        "  for i in range(len(a)):\n",
        "    if a[i] == 0:\n",
        "      a[i] = \"zerooo\"\n",
        "\n",
        "print(a)"
      ],
      "metadata": {
        "id": "j9MBWd-edzQe",
        "outputId": "0ec9c00a-439b-4c9e-a668-35655d9f1919",
        "colab": {
          "base_uri": "https://localhost:8080/"
        }
      },
      "execution_count": null,
      "outputs": [
        {
          "output_type": "stream",
          "name": "stdout",
          "text": [
            "['zerooo', 1, 'zerooo', 2, 3]\n"
          ]
        }
      ]
    }
  ]
}