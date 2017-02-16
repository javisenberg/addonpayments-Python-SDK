# -*- encoding: utf-8 -*-

import re
import uuid
import hashlib
from datetime import datetime


class GenerationUtils(object):
    """
    Utils for the auto-generation of fields, for example the SHA1 hash.
    """

    date_format = "%Y%m%d%H%M%S"

    @staticmethod
    def generate_hash(to_hash, secret):
        """
        This method takes the pre-built string of concatenated fields and the secret and returns the SHA-1 hash to be
        placed in the request sent to HPP.
        :param to_hash: string
        :param secret: string
        :return: string
        """
        # Step 1: With the SHA-1 algorithm, obtain the hash value of a string composed of the requested values.
        to_hash_first_pass = hashlib.sha1(bytes("{}".format(to_hash), encoding="UTF-8")).hexdigest()
        # Step 2: Concatenate the hash value chain with the shared secret.
        return hashlib.sha1(bytes("{}.{}".format(to_hash_first_pass, secret), encoding="UTF-8")).hexdigest()

    def generate_order_id(self):
        """
        Order Id for a initial request should be unique per client ID. This method generates a unique order Id using
        the Python uuid class
        :return: string
        """
        return uuid.uuid4().hex

    def generate_timestamp(self):
        """
        Generate the current datetimestamp in the string format (YYYYMMDDHHSS) required in a request.
        :return: string
        """
        return datetime.now().strftime(self.date_format)


class ValidateUtils(object):
    """
    Utils for the attrs validation fields.
    """

    @staticmethod
    def validate_mandatory(name, value):
        """
        This method raise exception if value is empty
        :param name: string
        :param value:
        """
        if not value:
            raise ValueError("Missing required argument: {}".format(name))

    @staticmethod
    def validate_str(name, value):
        """
        This method raise exception if value is not string
        :param name: string
        :param value:
        """
        if not isinstance(value, str):
            raise ValueError("{} must be string".format(name))

    @staticmethod
    def validate_int(name, value):
        """
        This method raise exception if value is not int
        :param name: string
        :param value:
        """
        if not isinstance(value, int):
            raise ValueError("{} must be integer".format(name))

    @staticmethod
    def validate_list(name, value):
        """
        This method raise exception if value is not list
        :param name: string
        :param value:
        """
        if not isinstance(value, list):
            raise ValueError("{} must be list".format(name))

    @staticmethod
    def validate_dict(name, value):
        """
        This method raise exception if value is not dict
        :param name: string
        :param value:
        """
        if not isinstance(value, dict):
            raise ValueError("{} must be dict".format(name))

    @staticmethod
    def validate_length_range(name, value, minimum, maximum):
        """
        This method raise exception if the length of the value is not within the range
        :param name: string
        :param value: string
        :param minimum: int
        :param maximum: int
        """
        if len(value) < minimum or len(value) > maximum:
            raise ValueError("{} must be between {} and {} characters".format(name, minimum, maximum))

    @staticmethod
    def validate_length(name, value, length):
        """
        This method raise exception if the length of the value is not the correct
        :param name: string
        :param value: string
        :param length: int
        """
        if len(value) != length:
            raise ValueError("{} must be {} characters in length".format(name, length))

    @staticmethod
    def validate_regex(name, value, regex, regex_msg):
        """
        This method raise exception if the value does not match the regular expression
        :param name: string
        :param value: string
        :param regex: string
        :param regex_msg: string
        """
        if not re.match(regex, value):
            raise ValueError("{} must only contain {} characters".format(name, regex_msg))