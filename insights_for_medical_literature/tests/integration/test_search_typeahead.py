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
# This is an example of invoking the /v1/corpora/{corpus}/search/{corpus}/typeahead REST API
#  of Insights for Medical Literature.

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
VERSION = CONFIG.get('settings', 'version')
CORPUS = CONFIG.get('settings', 'corpus')
ONTOLGOY = CONFIG.get('search', 'umls')
QUERY = CONFIG.get('search', 'typeahead_query')
TYPE = CONFIG.get('search', 'typeahead_type')

IML_TEST = wh.InsightsForMedicalLiteratureServiceV1(BASE_URL, APIKEY, IAMURL, VERSION, LEVEL, DISABLE_SSL)

# test can only be successful against a custom plan intance
def test_search_typeahead():
    types = [TYPE]
    ontologies = [ONTOLGOY]
    concept_list = IML_TEST.typeahead(corpus=CORPUS, query=QUERY, types=types, category='disorders', verbose=False,
                                  limit=10, max_hit_count=1000, no_duplicates=True, ontologies=ontologies)
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None

def test_search_typeahead_verbose():
    types = [TYPE]
    ontologies = [ONTOLGOY]
    concept_list = IML_TEST.typeahead(corpus=CORPUS, query=QUERY, types=types, category='disorders', verbose=True,
                                  limit=10, max_hit_count=1000, no_duplicates=True, ontologies=ontologies)
    assert concept_list is not None
    concepts = concept_list.concepts
    for concept in concepts:
        assert concept.cui is not None
        assert concept.ontology is not None

def test_search_typeahead_no_corpus():
    types = [TYPE]
    ontologies = [ONTOLGOY]
    try:
        concept_list = IML_TEST.typeahead(corpus=None, query=QUERY, types=types, category='disorders', verbose=True,
                                  limit=10, max_hit_count=1000, no_duplicates=True, ontologies=ontologies)
    except ValueError as imle:
        assert imle is not None

def test_search_typeahead_verbose_no_query():
    types = [TYPE]
    ontologies = [ONTOLGOY]
    try:
        concept_list = IML_TEST.typeahead(corpus=CORPUS, query=None, types=types, category='disorders', verbose=True,
                                  limit=10, max_hit_count=1000, no_duplicates=True, ontologies=ontologies)
    except ValueError as imle:
        assert imle is not None
