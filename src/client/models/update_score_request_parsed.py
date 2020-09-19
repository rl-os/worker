# coding: utf-8

"""
    RL API Internal

    Internal API endpoint, requires `internal.\\*.\\*` scope  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

import pprint
import re  # noqa: F401

import six

class UpdateScoreRequestParsed(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """
    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'mode': 'str',
        'enabled_mods': 'list[str]',
        'count50': 'int',
        'count100': 'int',
        'count300': 'int',
        'countgeki': 'int',
        'countkatu': 'int',
        'countmiss': 'int',
        'maxcombo': 'int',
        'passed': 'int',
        'perfect': 'int',
        'score': 'int',
        'frame': 'int',
        'playtime': 'int',
        'accuracy': 'float',
        'pp': 'float'
    }

    attribute_map = {
        'mode': 'mode',
        'enabled_mods': 'enabled_mods',
        'count50': 'count50',
        'count100': 'count100',
        'count300': 'count300',
        'countgeki': 'countgeki',
        'countkatu': 'countkatu',
        'countmiss': 'countmiss',
        'maxcombo': 'maxcombo',
        'passed': 'passed',
        'perfect': 'perfect',
        'score': 'score',
        'frame': 'frame',
        'playtime': 'playtime',
        'accuracy': 'accuracy',
        'pp': 'pp'
    }

    def __init__(self, mode=None, enabled_mods=None, count50=None, count100=None, count300=None, countgeki=None, countkatu=None, countmiss=None, maxcombo=None, passed=None, perfect=None, score=None, frame=None, playtime=None, accuracy=None, pp=None):  # noqa: E501
        """UpdateScoreRequestParsed - a model defined in Swagger"""  # noqa: E501
        self._mode = None
        self._enabled_mods = None
        self._count50 = None
        self._count100 = None
        self._count300 = None
        self._countgeki = None
        self._countkatu = None
        self._countmiss = None
        self._maxcombo = None
        self._passed = None
        self._perfect = None
        self._score = None
        self._frame = None
        self._playtime = None
        self._accuracy = None
        self._pp = None
        self.discriminator = None
        if mode is not None:
            self.mode = mode
        if enabled_mods is not None:
            self.enabled_mods = enabled_mods
        if count50 is not None:
            self.count50 = count50
        if count100 is not None:
            self.count100 = count100
        if count300 is not None:
            self.count300 = count300
        if countgeki is not None:
            self.countgeki = countgeki
        if countkatu is not None:
            self.countkatu = countkatu
        if countmiss is not None:
            self.countmiss = countmiss
        if maxcombo is not None:
            self.maxcombo = maxcombo
        if passed is not None:
            self.passed = passed
        if perfect is not None:
            self.perfect = perfect
        if score is not None:
            self.score = score
        if frame is not None:
            self.frame = frame
        if playtime is not None:
            self.playtime = playtime
        if accuracy is not None:
            self.accuracy = accuracy
        if pp is not None:
            self.pp = pp

    @property
    def mode(self):
        """Gets the mode of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The mode of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: str
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this UpdateScoreRequestParsed.


        :param mode: The mode of this UpdateScoreRequestParsed.  # noqa: E501
        :type: str
        """

        self._mode = mode

    @property
    def enabled_mods(self):
        """Gets the enabled_mods of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The enabled_mods of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: list[str]
        """
        return self._enabled_mods

    @enabled_mods.setter
    def enabled_mods(self, enabled_mods):
        """Sets the enabled_mods of this UpdateScoreRequestParsed.


        :param enabled_mods: The enabled_mods of this UpdateScoreRequestParsed.  # noqa: E501
        :type: list[str]
        """

        self._enabled_mods = enabled_mods

    @property
    def count50(self):
        """Gets the count50 of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The count50 of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._count50

    @count50.setter
    def count50(self, count50):
        """Sets the count50 of this UpdateScoreRequestParsed.


        :param count50: The count50 of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._count50 = count50

    @property
    def count100(self):
        """Gets the count100 of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The count100 of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._count100

    @count100.setter
    def count100(self, count100):
        """Sets the count100 of this UpdateScoreRequestParsed.


        :param count100: The count100 of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._count100 = count100

    @property
    def count300(self):
        """Gets the count300 of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The count300 of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._count300

    @count300.setter
    def count300(self, count300):
        """Sets the count300 of this UpdateScoreRequestParsed.


        :param count300: The count300 of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._count300 = count300

    @property
    def countgeki(self):
        """Gets the countgeki of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The countgeki of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._countgeki

    @countgeki.setter
    def countgeki(self, countgeki):
        """Sets the countgeki of this UpdateScoreRequestParsed.


        :param countgeki: The countgeki of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._countgeki = countgeki

    @property
    def countkatu(self):
        """Gets the countkatu of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The countkatu of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._countkatu

    @countkatu.setter
    def countkatu(self, countkatu):
        """Sets the countkatu of this UpdateScoreRequestParsed.


        :param countkatu: The countkatu of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._countkatu = countkatu

    @property
    def countmiss(self):
        """Gets the countmiss of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The countmiss of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._countmiss

    @countmiss.setter
    def countmiss(self, countmiss):
        """Sets the countmiss of this UpdateScoreRequestParsed.


        :param countmiss: The countmiss of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._countmiss = countmiss

    @property
    def maxcombo(self):
        """Gets the maxcombo of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The maxcombo of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._maxcombo

    @maxcombo.setter
    def maxcombo(self, maxcombo):
        """Sets the maxcombo of this UpdateScoreRequestParsed.


        :param maxcombo: The maxcombo of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._maxcombo = maxcombo

    @property
    def passed(self):
        """Gets the passed of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The passed of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._passed

    @passed.setter
    def passed(self, passed):
        """Sets the passed of this UpdateScoreRequestParsed.


        :param passed: The passed of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._passed = passed

    @property
    def perfect(self):
        """Gets the perfect of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The perfect of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._perfect

    @perfect.setter
    def perfect(self, perfect):
        """Sets the perfect of this UpdateScoreRequestParsed.


        :param perfect: The perfect of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._perfect = perfect

    @property
    def score(self):
        """Gets the score of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The score of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._score

    @score.setter
    def score(self, score):
        """Sets the score of this UpdateScoreRequestParsed.


        :param score: The score of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._score = score

    @property
    def frame(self):
        """Gets the frame of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The frame of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._frame

    @frame.setter
    def frame(self, frame):
        """Sets the frame of this UpdateScoreRequestParsed.


        :param frame: The frame of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._frame = frame

    @property
    def playtime(self):
        """Gets the playtime of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The playtime of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: int
        """
        return self._playtime

    @playtime.setter
    def playtime(self, playtime):
        """Sets the playtime of this UpdateScoreRequestParsed.


        :param playtime: The playtime of this UpdateScoreRequestParsed.  # noqa: E501
        :type: int
        """

        self._playtime = playtime

    @property
    def accuracy(self):
        """Gets the accuracy of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The accuracy of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: float
        """
        return self._accuracy

    @accuracy.setter
    def accuracy(self, accuracy):
        """Sets the accuracy of this UpdateScoreRequestParsed.


        :param accuracy: The accuracy of this UpdateScoreRequestParsed.  # noqa: E501
        :type: float
        """

        self._accuracy = accuracy

    @property
    def pp(self):
        """Gets the pp of this UpdateScoreRequestParsed.  # noqa: E501


        :return: The pp of this UpdateScoreRequestParsed.  # noqa: E501
        :rtype: float
        """
        return self._pp

    @pp.setter
    def pp(self, pp):
        """Sets the pp of this UpdateScoreRequestParsed.


        :param pp: The pp of this UpdateScoreRequestParsed.  # noqa: E501
        :type: float
        """

        self._pp = pp

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(UpdateScoreRequestParsed, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, UpdateScoreRequestParsed):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other