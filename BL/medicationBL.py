import httpx

CLINICAL_TABLES_API = 'https://clinicaltables.nlm.nih.gov/api'
DRUG_CODES = 'RXCUIS'
DOSAGES = 'STRENGTHS_AND_FORMS'


async def validate_medication(name, dosage):
    """validates that the medication's name and dosage matches exactly an existing medication,
    if so, return the medication codes"""

    url = f'{CLINICAL_TABLES_API}/rxterms/v3/search?terms={name}&ef={DRUG_CODES},{DOSAGES}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            result_amount = data[0]

            if result_amount == 1:
                try:
                    dosage_index = list(map(str.strip, data[2][DOSAGES][0])).index(dosage)
                    medication_code = data[2][DRUG_CODES][0][dosage_index]

                    return medication_code
                except (NameError, AttributeError, ValueError) as e:
                    print(e)

        return None