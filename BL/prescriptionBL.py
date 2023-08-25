import httpx
from models.prescription import Prescription
from models.interactions import Interactions

RXNAV_API = 'https://rxnav.nlm.nih.gov/REST'


def build_interactions_object(given_interactions) -> Interactions:
    """
    builds an object with the following format:

    interactions: {
        [drug_code1 + drug_code2]:  warnings[]
    }
    """
    interactions = Interactions()

    for interaction_pair in given_interactions:
        drug_code1, drug_code2 = [drug['rxcui'] for drug in interaction_pair['minConcept']]
        warnings = {interaction['description'] for interaction in interaction_pair['interactionPair']}
        interaction_key = f'{drug_code1} + {drug_code2}'

        interactions.interaction_pairs[interaction_key] = list(warnings)

    return interactions


async def get_prescription_interaction_warnings(prescription: Prescription):
    """check for any warnings of interactions between the prescription's medications"""
    medication_codes = {medication.code for medication in prescription.medications}
    medication_codes_parameter = '+'.join(map(str, medication_codes))

    url = f'{RXNAV_API}/interaction/list.json?rxcuis={medication_codes_parameter}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()

            try:
                given_interactions = data['fullInteractionTypeGroup'][0]['fullInteractionType']
                return build_interactions_object(given_interactions)
            except (NameError, AttributeError, ValueError) as e:
                print(e)

        return None
