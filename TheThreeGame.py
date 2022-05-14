# Author: Juliet Cuthbert
# Date: 11/18/2021
# Description: TheThreeGame

class TheThreeGame:
    """A class to represent TheThreeGame: A game involving two players taking turns choosing numbers between 1-9.
    After a number is chosen by one player, it can no longer be chosen by anyone.
    The first player to pick 3 numbers that exactly sum to 15 wins.
    If all numbers between 1-9 are chosen but neither player has chosen 3 numbers that sum to 15, it is a draw."""

    def __init__(self):
        """Creates a new game of TheThreeGame. Takes no parameters.
        Initializes data members to keep track of what numbers have been chosen, what the state of the game is,
        which player’s turn it is, a list of the first player’s numbers, and a list of the second player’s numbers.
        All data members are private."""
        self._numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self._game_state = "GAME_UNFINISHED"
        self._turn = 0
        self._list_one = []
        self._list_two = []

    def get_winner(self):
        """Takes no parameters. Returns the string ‘FIRST_PLAYER_WON’ or ‘SECOND_PLAYER_WON’ depending on the winner of
        the game,if there is one. Returns None if the game is unfinished or if the game is a draw."""
        if self._game_state == "GAME_UNFINISHED" or "IT_IS_A_DRAW":
            return None
        else:
            return self._game_state


    def is_it_a_draw(self):
        """Takes no parameters.
        Returns the string ‘FIRST_PLAYER_WON’ or ‘SECOND_PLAYER_WON’ depending on the winner of the game, if there is
        one. Returns the string ‘IT_IS_A_DRAW’ if the game is a draw. Returns the string ‘GAME_UNFINISHED’ otherwise."""
        #check if the game is a draw/is the numbers set empty?
        if self._numbers == set():
            self._game_state = "IT_IS_A_DRAW"
            return self._game_state
        else:
            return self._game_state

    def equals_fifteen(self, list_no):
        """Takes one parameter: the list that is associated with whichever player’s turn it is.
        Determines if there are three numbers within the list that sum to exactly 15.
        Updates the state of the game."""
        for index in range(0, len(list_no) - 1):
            # use sum of two numbers in the list as a constant
            two_sum = list_no[index] + list_no[index + 1]
            for num in list_no:
                # make sure not to add a number already used in previous sum to the sum of 3 numbers
                if num != list_no[index] and num != list_no[index + 1]:
                    if 15 - (two_sum + num) == 0:
                        if list_no == self._list_one:
                            self._game_state = "FIRST_PLAYER_WON"
                            return self._game_state
                        if list_no == self._list_two:
                            self._game_state = "SECOND_PLAYER_WON"
                            return self._game_state
        return self._game_state

    def make_move(self, player_no, num_choice):
        """Takes two parameters: the player and the number the associated player chooses for their turn.
        Returns False if the game is won or drawn.
        Returns False if it is not the player’s turn.
        Returns False if the number the player chooses has already been chosen.
        Otherwise, records the number the player chooses, calls method _is_it_a_draw and updates the state of the game,
        updates which player’s turn it is, and returns True."""
        #check if game is won or drawn
        if self._game_state == "GAME_UNFINISHED":
            #check if it is player one's turn
            if self._turn % 2 == 0 and player_no == "first_player":
                #check that integer is in range and hasn't been chosen already
                if num_choice in self._numbers:
                    #record the move
                    self._list_one.append(num_choice)
                    #update which player's turn it is
                    self._turn += 1
                    self._numbers.remove(num_choice)
                    #update the current state if the move caused a win or draw
                    TheThreeGame.equals_fifteen(self, self._list_one)
                    return True
                else:
                    return False
            #check if it is player two's turn
            if self._turn % 2 != 0 and player_no == "second_player":
                #check that integer is in range and hasn't been chosen already
                if num_choice in self._numbers:
                    #record the move
                    self._list_two.append(num_choice)
                    #update which player's turn it is
                    self._turn += 1
                    self._numbers.remove(num_choice)
                    #update the current state if the move caused a win or draw
                    TheThreeGame.equals_fifteen(self, self._list_two)
                    return True
                else:
                    return False
            else:
                return False
        else:
            return False



