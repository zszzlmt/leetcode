class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        areal, aimg = a.split('+')
        breal, bimg = b.split('+')
        areal = int(areal)
        aimg = int(aimg[:-1])
        breal = int(breal)
        bimg = int(bimg[:-1])
        real = areal * breal - aimg * bimg
        img = areal * bimg + breal * aimg
        return str(real) + '+' + str(img) + 'i'
