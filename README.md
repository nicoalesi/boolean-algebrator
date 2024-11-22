# Truth table generator

**Truth table generator is a generator of truth tables.**

It has been designed to generate any kind of truth table starting from a given boolean expression.
This project was born to help Computer Architecture students
and ease the process of double-checking their results.

## Index
 - [Usage](#usage)
 - [Information](#information)
 - [How it works](#how-it-works)

----

## Usage

To use this program follow these steps:

1. Download all the files from GitHub.
2. Open the terminal.
3. Move to the directory where the project is located.
4. Make sure to have python installed on your computer.
5. Run the main file ***truth_table_generator.py*** using the following command:
   
   `python truth_table_generator.py`

## Information

The program is capable of generating truth tables with up to 26 inputs, all the alphabet letters.
The only characters allowed besides letters are: `+` *or*, `'` *not*, `(` `)` *open and closed parentheses*.
The output consists in a drawn table.

> ## Example
> 
> Expression
> ```
> AB+AC+BC'
> ```
> Table:
> ```
> +-------+---+
> | A B C | Y |
> +-------+---+
> | 0 0 0 | 0 |
> | 0 0 1 | 0 |
> | 0 1 0 | 1 |
> | 0 1 1 | 0 |
> | 1 0 0 | 0 |
> | 1 0 1 | 1 |
> | 1 1 0 | 1 |
> | 1 1 1 | 1 |
> +-------+---+
> ```

## How it works

After getting the expression as input, the first step is to catch all the variables in it.
All the unique variables are stored in an alphabetically sorted list.

Then the expression is converted in an executable string.

Once everything is ready the structure of the table is built and inputs are
written along with it.

To create inputs the program takes all integers from *0* to *2 raised to the number of variables*
and converts them in binary, then splits the obtained values charwise to get the inputs.
> ### Example with 2 variables
> > 0<sub>10</sub> = 00<sub>2</sub> &nbsp; *split* > &nbsp; 0 &nbsp; 0
> 
> > 1<sub>10</sub> = 01<sub>2</sub> &nbsp; *split* > &nbsp; 0 &nbsp; 1
> 
> > 2<sub>10</sub> = 10<sub>2</sub> &nbsp; *split* > &nbsp; 1 &nbsp; 0
> 
> > 3<sub>10</sub> = 11<sub>2</sub> &nbsp; *split* > &nbsp; 1 &nbsp; 1

After input values are generated, they are substituted into their correspondent variables in the executable string.
At the end the string is executed and the result is printed in the right column of the table.
