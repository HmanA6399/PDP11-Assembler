import re

from SingletonMeta import SingletonMeta
from stores import LabelStore
import constants

class Parser(metaclass=SingletonMeta):
    label_store : LabelStore = None
    
    def __init__(self):
        self.label_store = LabelStore()
    
    def parseSentence(self, str, position) :
        # Remove comments
        str = re.sub(constants.COMMENT_REGEX, '', str)

        # Extract Label
        str = self.extractLabel(str, position);

        # Segment the sentence
        segments = re.findall(constants.SEGMENT_REGEX, str);

        # print(segments)

        return segments;

    def extractLabel(self, sentence, position) :
        # Detect existence of label delimiter
        match = re.search(constants.LABEL_DELIMETER_REGEX, sentence);

        # Found a label
        if (match) :
            label = sentence[:match.start()]
            sentence = sentence[match.end():]
            self.label_store.setLabel(label, position)
        
        return sentence