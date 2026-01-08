from enum import Enum

class SearchCriteria(str, Enum):
    CONDITIONS = 'conditions'
    PROCEDURES = 'procedures'
    MEDICATIONS = 'medications'