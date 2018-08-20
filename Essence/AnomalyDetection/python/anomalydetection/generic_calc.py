

class GenericCalc():
    """
    Standardize the test function so when we implement different
    algorithms the code doesn't have to change much
    """

    @staticmethod
    def test(self, train_h, test_h):
        assert(isinstance(train_h, Histograms))
        assert(isinstance(test_h, Histograms))
        
        raise NotImplementedError()
    
