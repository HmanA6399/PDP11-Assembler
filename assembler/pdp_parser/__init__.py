import re

from SingletonMeta import SingletonMeta
import constants

class Parser(metaclass=SingletonMeta):
    
    def parseSentence(self, str) :
        # Remove comments
        str = re.sub(constants.COMMENT_REGEX, '', str)

        # Segment the sentence
        segments = re.findall(constants.SEGMENT_REGEX, str);

        return segments;
