from __future__ import unicode_literals

from django.db import models

# region ODM2 Core models


class AffiliationManager(models.Manager):
    use_for_related_fields = True

    def get_queryset(self):
        queryset = super(AffiliationManager, self).get_queryset()
        return queryset.prefetch_related('person', 'organization')


class ActionManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActionManager, self).get_queryset()
        return queryset.prefetch_related('feature_action__sampling_feature', 'method')


class ActionByManager(models.Manager):
    def get_queryset(self):
        queryset = super(ActionByManager, self).get_queryset()
        return queryset.prefetch_related('action', 'affiliation__organization', 'affiliation__person')


class FeatureActionManager(models.Manager):
    def get_queryset(self):
        queryset = super(FeatureActionManager, self).get_queryset()
        return queryset.prefetch_related('sampling_feature', 'action')


class RelatedActionManager(models.Manager):
    def get_queryset(self):
        queryset = super(RelatedActionManager, self).get_queryset()
        return queryset.prefetch_related('related_action', 'action')


class ResultManager(models.Manager):
    def get_queryset(self):
        queryset = super(ResultManager, self).get_queryset()
        return queryset.prefetch_related(
            'variable', 'unit', 'taxonomic_classifier', 'processing_level'
        )


class DataLoggerFileManager(models.Manager):
    def get_queryset(self):
        queryset = super(DataLoggerFileManager, self).get_queryset()
        return queryset.prefetch_related('program')


class DataLoggerFileColumnManager(models.Manager):
    def get_queryset(self):
        queryset = super(DataLoggerFileColumnManager, self).get_queryset()
        return queryset.DataLoggerFileColumnManager('result')

# endregion

# region ODM2 Equipment Extension


class EquipmentModelManager(models.Manager):
    def get_queryset(self):
        queryset = super(EquipmentModelManager, self).get_queryset()
        return queryset.prefetch_related('model_manufacturer')


class InstrumentOutputVariableManager(models.Manager):
    def get_queryset(self):
        queryset = super(InstrumentOutputVariableManager, self).get_queryset()
        return queryset.prefetch_related('model', 'variable', 'instrument_method', 'instrument_raw_output_unit')


class EquipmentManager(models.Manager):
    def get_queryset(self):
        queryset = super(EquipmentManager, self).get_queryset()
        return queryset.prefetch_related('equipment_model', 'equipment_owner', 'equipment_vendor')


class CalibrationReferenceEquipmentManager(models.Manager):
    def get_queryset(self):
        queryset = super(CalibrationReferenceEquipmentManager, self).get_queryset()
        return queryset.prefetch_related('action', 'equipment')


class EquipmentUsedManager(models.Manager):
    def get_queryset(self):
        queryset = super(EquipmentUsedManager, self).get_queryset()
        return queryset.prefetch_related('action', 'equipment')


class MaintenanceActionManager(models.Manager):
    def get_queryset(self):
        queryset = super(MaintenanceActionManager, self).get_queryset()
        return queryset.prefetch_related('action')


class RelatedEquipmentManager(models.Manager):
    def get_queryset(self):
        queryset = super(RelatedEquipmentManager, self).get_queryset()
        return queryset.prefetch_related('equipment', 'related_equipment')


class CalibrationActionManager(models.Manager):
    def get_queryset(self):
        queryset = super(CalibrationActionManager, self).get_queryset()
        return queryset.prefetch_related('instrument_output_variable')

# endregion

