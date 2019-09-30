from neuraxle.base import BaseStep, NonFittableMixin
from neuraxle.pipeline import Pipeline
from testing.test_pipeline import SomeStep


class SomeSplitStep(NonFittableMixin, BaseStep):
    def fit(self, data_inputs, expected_outputs=None) -> 'NonFittableMixin':
        pass

    def fit_transform(self, data_inputs, expected_outputs=None):
        pass

    def transform(self, data_inputs):
        pass


def test_truncable_steps_should_split_by_type():
    pipeline = Pipeline([
        SomeStep(),
        SomeStep(),
        SomeSplitStep(),
        SomeStep(),
        SomeStep(),
        SomeSplitStep(),
        SomeStep(),
    ])

    sub_pipelines = pipeline.split('SomeSplitStep')

    assert 'SomeStep' in sub_pipelines[0]
    assert 'SomeStep1' in sub_pipelines[0]
    assert 'SomeSplitStep' in sub_pipelines[0]
    assert 'SomeStep2' in sub_pipelines[1]
    assert 'SomeStep3' in sub_pipelines[1]
    assert 'SomeSplitStep1' in sub_pipelines[1]
    assert 'SomeStep4' in sub_pipelines[2]
