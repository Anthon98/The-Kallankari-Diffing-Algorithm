# A new similarity metric diffing algorithm created by Github user Anthon98.

''' I want to avoid using libraries so that this can easily be converted into other programming languages.
    As of 21.10.2021 the most complex parts of the code have been made, but the ratio calculation is not here yet. '''


a = "loool lool"  # Word A
b = "loool oo"  # Word B


def get_dist(arr: list, base: list) -> int:
    # Distance between a single index to a single index in base. (Will be the same for any index anyway).
    maxfidx = max([arr[0], base[0]])
    minfidx = min([arr[0], base[0]])
    return maxfidx - minfidx


def new_dist_calc(a: list, b: list, longest: str):
    equals_found = 0
    smallest_dist = float('inf')
    ''' From smallest possible to greatest (iteration purpose). Length multiplied by 2 in iteration phase.
        This way numbers go from smallest ETC -7 to plus 7 index if the word length was 7.'''
    a_clone = [x + (-len(longest)) for x in a]
    for _ in range(len(longest)*2):
        for index, _ in enumerate(a_clone):
            a_clone[index] += 1
        this_run_equals = 0
        for _, val in enumerate(a_clone):
            # Is the index in a larger or smaller to largest or smallest in b
            if val <= max(b) and val >= min(b):
                # Value is clamped between smallest and greatest value
                # Compare which index it is equal to?
                for _, vals in enumerate(b):
                    if val == vals:
                        this_run_equals += 1
        if this_run_equals > equals_found:
            # We want a function here that calculates the distance of steps between these matches.
            dist = get_dist(a_clone, a)
            if dist < smallest_dist:
                smallest_dist = dist
            equals_found = this_run_equals
    return equals_found, smallest_dist


def compare(a: str, b: str, a_data: dict, b_data: dict) -> None:
    # Which one is the longest?
    longest = max([a, b], key=len)
    # Flip to make commutative.
    if longest == b:
        b = a
        a = longest
    # Find number of times a letters are found in b?
    for letter in a_data.keys():
        if letter in b_data.keys():
            aidx = a_data[letter]['indexes']
            bidx = b_data[letter]['indexes']
            ''' Find how many times a letter is off? We can group them like this.
                For example indexes 0, 1 are both off by 1 for 1 and 2, thats 2.
                Btw these values go from lowest to highest in case they are arrayed.
                This would kinda mimic radcliff / obershelp algorithm 
                except it finds the longest match per individual letter and takes into account the steps it took. '''
            equals, smallest_dist = new_dist_calc(aidx, bidx, longest)
            print("Letter:", letter, "Equals length:", equals,
                  "Shortest distance to longest match for the letter:", smallest_dist)
            ''' Meaning of equals length & smallest distance?

                Say we have these words: loool and loool. For the letter L we get 2 equals (length).
                This is because both words l indexes are at the exact same position.
                If this wasn't the case, we'd get only 1 if we can find any L in both words.
                For the letter O it's the length 

                The shortest distance to the longest match is self explanatory.
                Basically it finds the fewest steps it took to index the longest match.
            '''


def occurances(word: str) -> dict:
    originals = {}
    for idx, letter in enumerate(word):
        if letter not in originals.keys():
            originals.update({letter: {
                'occurances': 1,
                'indexes': [idx]
            }})
        else:
            originals[letter]['occurances'] += 1
            originals[letter]['indexes'].append(idx)
    return originals


if __name__ == '__main__':
    # I'll change this ugly double function call.
    aa = occurances(a)
    bb = occurances(b)
    compare(a, b, aa, bb)
