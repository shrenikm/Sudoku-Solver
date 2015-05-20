# Sudoku-Solver
A Sudoku Solver using the pygame library.

The sudokuGUI.py contains the main GUI code that uses pygame. It displays the graphical grid and has options for the user to enter the 
numbers in the grid. Interactive colors are used effectively to make the grid easier to work with.

This file also contains many game logic functions that depend on a lot of the files variables and dictionaries.

The gridNotation.py mainly contains the notation generation algorithms that are used to grant access to each of the squares of the puzzle.
It also contains certain functions to refresh values of dictionaries, as they are notation dependent.

The sudokuAlgo.py is the core game logic. It does not have any gui code in it. It is basically a constrictive algorithm that is used to
solve the puzzle once the user has entered the puzzle in the main GUI application. It takes the entered data from the GUI application, solves
the puzzle and then returns this value to the GUI program to display the result on the grid.


# The Application

The application starts of with a blank grid. We can hover over any of the grids and click on them to enter a number. Once we click on it, 
an options menu pops up on the right side that contains a list of numbers from 0 to 9. On selecting a number, that number is entered in the
grid. If 0 is selected, then the square that was selected is deselected. We can do that same (select 0) to clear a square. We can also click away to clear the selection.

The application has 3 buttons. The solve button is used to solve the sudoku. Once it is clicked, the sudoku is solved and the result is displayed on the grid itself. The computer generated numbers are displayed in red, whereas the user entered numbers are in black.

The reset button is used to reset the grid to its state before the solve button was pressed, thus the user can enter or change values.

The clear button is used to clear the entire grid and start from scratch.

In case the user enters invalid grid values, or tries to solve an empty puzzle, appropriate error message is displayed.
