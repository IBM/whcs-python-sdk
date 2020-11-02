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

import ibm_whcs_sdk.annotator_for_clinical_data as wh

def test_MedicationAnnotation_model():
    drug_list = []
    temporal_list = []
    model = wh.MedicationAnnotation(id="name", type="type", uid=123, begin=1, end=2,
                                    covered_text="We got you covered", negated=False, hypothetical=False, cui=234,
                                    drug=drug_list, section_normalized_name="snn", section_surface_form="ssf",
                                    temporal=temporal_list, extra="more")
    assert model.__str__() is not None
