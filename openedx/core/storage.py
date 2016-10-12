"""
Django storage backends for Open edX.
"""
from django_pipeline_forgiving.storages import PipelineForgivingStorage
from django.contrib.staticfiles.storage import StaticFilesStorage, CachedFilesMixin
from pipeline.storage import PipelineMixin, NonPackagingMixin
from require.storage import OptimizedFilesMixin
from openedx.core.djangoapps.theming.storage import ComprehensiveThemingAwareMixin


class ProductionStorage(
        PipelineForgivingStorage,
        ComprehensiveThemingAwareMixin,
#	OptimizedFilesMixin,
#	Replaced by the below. Probably a performance hit, but works...
	NonPackagingMixin,
        PipelineMixin,
        CachedFilesMixin,
        StaticFilesStorage
):
    """
    This class combines Django's StaticFilesStorage class with several mixins
    that provide additional functionality. We use this version on production.
    """
    pass


class DevelopmentStorage(
        ComprehensiveThemingAwareMixin,
        NonPackagingMixin,
        PipelineMixin,
        StaticFilesStorage
):
    """
    This class combines Django's StaticFilesStorage class with several mixins
    that provide additional functionality. We use this version for development,
    so that we can skip packaging and optimization.
    """
    pass
