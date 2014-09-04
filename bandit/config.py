# -*- coding:utf-8 -*-
#
# Copyright 2014 Hewlett-Packard Development Company, L.P.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.

import sys
import yaml


class BanditConfig():

    _config = dict()
    _logger = None

    def __init__(self, logger, config_file):
        '''
        Attempt to initialize a config dictionary from a yaml file, error out
        if this fails for any reason.
        :param logger: Logger to be used in the case of errors
        :param config_file: The Bandit yaml config file
        :return: -
        '''

        self._logger = logger

        try:
            f = open(config_file, 'r')
        except IOError:
            logger.error("could not open config file: %s" % config_file)
            sys.exit(2)
        else:
            # yaml parser does its own exception handling
            self._config = yaml.load(f)

    def get_option(self, option_string):
        option_levels = option_string.split('.')
        cur_item = self._config
        for level in option_levels:
            if level in cur_item:
                try:
                    cur_item = cur_item[level]
                except Exception:
                    self._logger.error("error while accessing config property: %s" %
                                 option_string)
                    return None
            else:
                return None

        return cur_item

    @property
    def config(self):
        '''
        Property to return the config dictionary
        :return: Config dictionary
        '''
        return self._config