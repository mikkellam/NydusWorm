class RequirementRepository:
    """Class containing all requirements for units and upgrades. including
       producers and tech requirements"""
    unit_producers = {}
    unit_required_buildings = {}
    research_producers = {}
    research_required_buildings = {}
    research_required_research = {}

    def __init__(self, unit_producers, unit_required_buildings, reasearch_producers, research_required_buildings, reasearch_required_research):
        for multi_pair in unit_producers:
            self.unit_producers.update({multi_pair.key: multi_pair.values})

        for multi_pair in unit_required_buildings:
            self.unit_required_buildings.update({multi_pair.key: multi_pair.values})

        for value_pair in reasearch_producers:
            self.research_producers.update({value_pair.key: value_pair.value})

        for value_pair in research_required_buildings:
            self.research_required_buildings.update({value_pair.key: value_pair.value})

        for value_pair in reasearch_required_research:
            self.research_required_research.update({value_pair.key: value_pair.value})
