# coding: utf-8

# Copyright 2018 IBM All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
import configparser
import watson_health_cognitive_services.insights_for_medical_literature as wh

# To access a secure environment additional parameters are needed on the constructor which are listed below
CONFIG = configparser.RawConfigParser()
CONFIG.read('./tests/config.ini')

BASE_URL = CONFIG.get('settings', 'base_url')
APIKEY = CONFIG.get('settings', 'key')
IAMURL = CONFIG.get('settings', 'iam_URL')
LEVEL = CONFIG.get('settings', 'logging_level')
VERSION = CONFIG.get('settings', 'version')
DISABLE_SSL = CONFIG.get('settings', 'disable_ssl')
CORPUS = CONFIG.get('settings', 'corpus')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

def test_get_corpora():
    corpora_config_model = IML_TEST.get_corpora_config()
    corpus_list = corpora_config_model.corpora
    for item in corpus_list:
        assert item.corpus_name is not None

def test_get_corpora_verbose():
    corpora_config_model = IML_TEST.get_corpora_config(verbose=True)
    corpus_list = corpora_config_model.corpora
    for item in corpus_list:
        assert item.corpus_name is not None
        assert item.ontologies is not None
