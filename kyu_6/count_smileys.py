def count_smileys(arr):
    """Valid smiley face examples: :) :D ;-D :~)
    Invalid smiley faces: ;( :> :} :]

    Example
    countSmileys([':)', ';(', ';}', ':-D']);       // should return 2;
    countSmileys([';D', ':-(', ':-)', ';~)']);     // should return 3;
    countSmileys([';]', ':[', ';*', ':$', ';-D']); // should return 1;

    Each smiley face must contain a valid pair of eyes. 
    Eyes can be marked as : or ;
    A smiley face can have a nose but it does not have to. 
    Valid characters for a nose are - or ~
    Every smiling face must have a smiling 
    mouth that should be marked with either ) or D
    """

    eyes = ":;"
    noses = "-~"
    mouthes = ")D"
    c = 0
    
    for smile in arr:
        if (
            len(smile) == 2
            and smile[0] in eyes
            and smile[-1] in mouthes
        ):
            c += 1
        elif (
            len(smile) == 3
            and smile[0] in eyes
            and smile[-1] in mouthes
            and smile[1] in noses
        ):
            c += 1

    return c
