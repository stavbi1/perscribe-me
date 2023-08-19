import httpx


async def validate_medication(name):
    drug_codes = 'RXCUIS'
    url = f'https://clinicaltables.nlm.nih.gov/api/rxterms/v3/search?terms={name}&ef={drug_codes}'

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

        if response.status_code == 200:
            data = response.json()
            result_amount = data[0]

            if result_amount == 1:
                try:
                    return data[2][drug_codes][0]
                except (NameError, AttributeError) as e:
                    pass

        return None
