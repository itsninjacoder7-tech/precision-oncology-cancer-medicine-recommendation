def extract_entities(query):

    entities = []

    biomarkers = [
        "EGFR",
        "HER2",
        "ALK",
        "BRAF",
        "KRAS"
    ]

    for b in biomarkers:

        if b.lower() in query.lower():
            entities.append(b)

    return entities