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
import sys

moves = {0:[4, 6], 1:[6, 8], 2:[7, 9], 3:[4, 8], 4:[0, 3, 9], 5:[], 6:[0, 1, 7], 7:[2, 6], 8:[1, 3], 9:[2, 4]}

# @method helper uses recursion to branch on the moves that a knight can jump to
#       - @param N - number of hops that a knight can do
#       - @param S - starting position of the night
def helper(N, S):
	if N == 0:
		return 1

	result = 0
	for position in moves[S]:
		result += helper(N-1, position)

	return result

# @method horse_on_phonepad returns the distinct numbers that a knight can dial from a starting position S by doing N hops.
#       - @param N - number of hops that a knight can do
#       - @param S - starting position of the night
def horse_on_phonepad(N, S):
	return helper(N-1, S)


try:
	args = sys.argv[1:]
	N, S = -1, -1

	for index, arg in enumerate(args):
		if arg == 'N':
			N = int(args[index+1])
		elif arg == 'S':
			S = int(args[index+1])
	if N == -1 or S == -1:
		print('The arguments are not correct!!!')
		print('Example: "python horse_on_the_phonepad.py N 4 S 1"')
		sys.exit(0)
		
	print('You can dial {0} distinct numbers in {1} hops from a starting position of {2}.'.format(horse_on_phonepad(N, S), N, S))

except Exception as e:
	print('The arguments are not correct!!!')
	print('Example: "python horse_on_the_phonepad.py N 4 S 1"')
