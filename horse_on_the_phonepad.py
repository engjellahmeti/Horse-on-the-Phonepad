# @task Horse on the Phonepad
# @author Engjëll Ahmeti
# @date 4/28/2021
# @ description
        # imagine you place a knight chess piece on a phone dial pad. This chess piece moves in an uppercase “L” shape:
        #               - two steps horizontally followed by one vertically, or
        #               - one step horizontally then two vertically:
        #               - two steps vertically followed by one horizontally
        #               - one step vertically followed by two horizontally
        #
        # https://imgur.com/a/RoKf8Sg
        #
        # Pay no attention to the poorly-redacted star and pound keys
        #
        # Suppose you dial keys on the keypad using only hops a knight can make. Every time the knight lands on a key, we dial that key and make another hop.
        # The starting position counts as being dialed.
        #
        # Your mission is now “Write a software that solves the following question:
        #
        # How many distinct numbers can you dial in N hops from a particular starting position?”

class HorseOnPhonepad:
    # @construrctor HorseOnPhonepad
    #   - here all the moves are set up for which a knight from either position can make
    def __init__(self):
        self.moves = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4]}

    # @method helper uses recursion to branch on the moves that a knight can jump to
    #       - @param N - number of hops that a knight can do
    #       - @param S - starting position of the night
    def helper(self, N, S):
        if N == 0:
            return 1

        result = 0
        for position in self.moves[S]:
            result += self.helper(N-1, position)

        return result

    # @method horse_on_phonepad returns the distinct numbers that a knight can dial from a starting position S by doing N hops.
    #       - @param N - number of hops that a knight can do
    #       - @param S - starting position of the night
    def horse_on_phonepad(self, N, S):
        return self.helper(N-1, S)

