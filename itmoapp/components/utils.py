import random
import string


class Utils:

    @staticmethod
    def endings(count, form1, form2, form5):
        """
        Return word with right ending

        :param integer count:
        :param string form1: стол, дерево, ложка
        :param string form2: стола, дерева, ложки
        :param string form5: столов, деревьев, ложек
        :return:
        """
        n = count % 100
        n1 = count % 10

        if n > 10 and n < 20:
            return form5

        if n1 > 1 and n1 < 5:
            return form2

        if n1 == 1:
            return form1

        return form5

    @staticmethod
    def generate_hash(size=8, chars=string.ascii_uppercase + string.digits):
        """
        Generate unique string

        :param size: size in symbols
        :param chars: letters used
        :return: string token
        """
        return ''.join(random.SystemRandom().choice(chars) for _ in range(size))
