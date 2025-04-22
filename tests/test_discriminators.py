#  Copyright 2024 Palantir Technologies, Inc.
#
#  Licensed under the Apache License, Version 2.0 (the "License");
#  you may not use this file except in compliance with the License.
#  You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
#  Unless required by applicable law or agreed to in writing, software
#  distributed under the License is distributed on an "AS IS" BASIS,
#  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#  See the License for the specific language governing permissions and
#  limitations under the License.


import pydantic
import pytest

from gotham.v1.federated_sources import models as models_federated_sources_v1
from gotham.v1.foundry import models as models_foundry_v1
from gotham.v1.gaia import models as models_gaia_v1
from gotham.v1.geotime import models as models_geotime_v1
from gotham.v1.gotham import models as models_gotham_v1
from gotham.v1.inbox import models as models_inbox_v1
from gotham.v1.map_rendering import models as models_map_rendering_v1
from gotham.v1.media import models as models_media_v1
from gotham.v1.target_workbench import models as models_target_workbench_v1


def test_can_validate_types():
    """
    The discriminators types are difficult to construct. This test ensures
    that all discriminators are importable without raising any issues.
    """

    for models, model_name in [
        *[
            (models_federated_sources_v1, model_name)
            for model_name in dir(models_federated_sources_v1)
        ],
        *[(models_foundry_v1, model_name) for model_name in dir(models_foundry_v1)],
        *[(models_gaia_v1, model_name) for model_name in dir(models_gaia_v1)],
        *[(models_geotime_v1, model_name) for model_name in dir(models_geotime_v1)],
        *[(models_gotham_v1, model_name) for model_name in dir(models_gotham_v1)],
        *[(models_inbox_v1, model_name) for model_name in dir(models_inbox_v1)],
        *[(models_map_rendering_v1, model_name) for model_name in dir(models_map_rendering_v1)],
        *[(models_media_v1, model_name) for model_name in dir(models_media_v1)],
        *[
            (models_target_workbench_v1, model_name)
            for model_name in dir(models_target_workbench_v1)
        ],
    ]:
        klass = getattr(models, model_name)

        if "Annotated[Union[" not in str(klass):
            continue

        try:
            ta = pydantic.TypeAdapter(klass)
        except pydantic.PydanticUndefinedAnnotation as e:
            print(model_name, str(klass))
            raise e

        with pytest.raises(pydantic.ValidationError) as error:
            ta.validate_python({})

        assert error.value.errors(include_url=False) == [
            {
                "type": "union_tag_not_found",
                "loc": (),
                "msg": "Unable to extract tag using discriminator 'type'",
                "input": {},
                "ctx": {"discriminator": "'type'"},
            }
        ]
