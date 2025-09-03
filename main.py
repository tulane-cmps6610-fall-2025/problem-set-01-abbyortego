"""
CMPS 6610  Assignment 1.
See problemset-01.pdf for details.
"""
# no imports needed.

def foo(a, b):
    if a==0:
        return b
    elif b==0:
        return a
    else:
        x, y = (min(a,b), max(a,b))
        return foo(y, y % x)
    #
#

def longest_run(mylist, key):
    """
    Input:
        `myarray`: a list of ints
        `key`: an int
    Return:
        the longest continuous sequence of `key` in `myarray`
    """
    
    seq_count = 0
    key_count = 0
    for val in mylist: 
        if val==key:
            key_count += 1
        else:
            seq_count = max(seq_count, key_count)
            key_count = 0
        #
    #
    return seq_count
#

class Result:
    """ done """
    def __init__(self, left_size, right_size, longest_size, is_entire_range):
        self.left_size = left_size              # the length of the longest run on left side of input
                                                # eg, with a key of 12, [12 12 3] has left_size of 2 
        self.right_size = right_size            # length of longest run on right side of input
                                                # eg, key 12, [3 12 12] has right_size of 2
        self.longest_size = longest_size        # length of longest run in input
                                                # eg, [12 12 4 12 12 12]: longest_size is 3
        self.is_entire_range = is_entire_range  # True if the entire input matches the key
        
    def __repr__(self):
        return('longest_size=%d left_size=%d right_size=%d is_entire_range=%s' %
              (self.longest_size, self.left_size, self.right_size, self.is_entire_range))

seq_count = Result(0, 0, 0, False)

def longest_run_recursive(mylist, key):
    # TODO
    print('sequencing %s' % mylist)

    if len(mylist)==1:
        return mylist[0]
        # seq_count.left_size+=1
        # seq_count.right_size+=1
        # seq_count.longest_size+=1
    else:
        if longest_run_recursive(mylist[:len(mylist)//2], key)==key:
            seq_count.left_size += 1
        if longest_run_recursive(mylist[len(mylist)//2:], key)==key:
            seq_count.right_size += 1
        return max(seq_count.left_size, seq_count.right_size)

        # print(longest_run_recursive(mylist[:len(mylist)//2], key)==key)
        # print(longest_run_recursive(mylist[len(mylist)//2:], key)==key)

        # # if longest_run_recursive(mylist[:len(mylist)//2], key) == longest_run_recursive(mylist[len(mylist)//2:], key):
        # #     return "huh"                                                                       

        # seq_count.left_size += longest_run_recursive(mylist[:len(mylist)//2], key)
        # seq_count.right_size += longest_run_recursive(mylist[len(mylist)//2:], key)
        # return max(seq_count.left_size, seq_count.right_size)

        # if longest_run_recursive(mylist[len(mylist)//2:], key)==key:
        #     print(key)

        # if mylist[0]==key:
        #     seq_count.left_size += 1
        # man idek anymore

        # seq_count.right_size += longest_run_recursive(mylist[len(mylist)//2:], key)
        # L_s, R_s = [longest_run_recursive(mylist[len(mylist)//2:], key), longest_run_recursive(mylist[:len(mylist)//2], key)]
        # longest_run_recursive(mylist[:len(mylist)//2], key) + longest_run_recursive(mylist[len(mylist)//2:], key)
    #
#
print(longest_run_recursive([2,12,12,8,12,12,12,0,12,1], 12))

## Feel free to add your own tests here.
def test_longest_run():
    assert longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3
#
# test_longest_run()
