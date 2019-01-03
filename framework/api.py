import requests

class Postmethod:

    @staticmethod
    def addintegers(test_input, expected_respons):

        body = {
            "numbers": test_input
        }

        full_url = f'http://localhost:12345/add'

        fixed_reponse_text = '"sum":'

        res = requests.post(full_url,
                            json=body)

        exprespons = ("{" + fixed_reponse_text + expected_respons + "}")

        assert res.text == exprespons

        if res.status_code == 200:
            return res.json()

        else:
            raise RuntimeError(f'Failed to process request, server returned {res.status_code}: {res.content}')

class Hellogreeting:

    @staticmethod
    def getgreeting(test_input, expected_respons):

        base_url = f'http://localhost:12345/hello/'
        full_url = base_url + test_input

        print (full_url)

        fixed_reponse_text = '"greeting":"Hello, '

        res = requests.get(full_url)

        print (res)
        print (res.text)
        print (res.json)

        exprespons = ("{" + fixed_reponse_text + test_input + " " + expected_respons + '"' + "}")

        print (exprespons)

        assert res.text == exprespons
