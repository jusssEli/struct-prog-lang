def eval(s):
        for c in s:
            assert c in "-0123456789."
        n = 0
        if s[0] == '-':
            sign = -1
            s = s[1:] #drop first character/token and give rest of sequence - also called consuming token
        else:
            sign = 1
        multi = 1.0
        fractional = False

        assert len(s) > 0
        while len(s) > 0:
            n = n * 10 + ord(s[0]) - ord("0")
            s = s[1:]
        return n * sign

def test_eval():
        """ test eval """
        print("Testing eval().")
        assert eval("0") == 0, "Expect 0 to be 0"      #Explanatory comment is the second half/not printed
        assert eval("1") == 1
        assert eval("99") == 99
        assert eval("1099") == 1099
        assert eval("0001") == 1
        assert eval("-99") == -99
        assert eval("1.") == 1
        
if __name__ == "__main__":
        test_eval()
        print("Done.")
