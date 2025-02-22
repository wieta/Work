from faker.providers import BaseProvider
import itertools

class ClientRegisterProvider(BaseProvider):
	
	def client(self, fields=None):

		cardNumber = self.generator.cardNumberAuthorization()
		
		if fields is None:
			fields = []

		d = {
		"Identity":
		{
		"PosId": self.generator.uuid4(),
		"PosNumber": self.generator.random_number(2),
		"PosOperatorId": self.generator.uuid4(),
		"PosOperatorNumber": self.generator.random_number(2),
		"SiteId": self.generator.random_number(4)
		},
		"ResponseLanguage":
		{		
		"ClientLanguage": self.generator.locale(),
		"CashierLanguage": self.generator.locale()
		},
		"LoyaltyCard":
		{
		"CardNumber": cardNumber,
		"PhoneNumber": "",#self.generator.numerify('48#########'),
		"Gender": self.generator.random_element(["F", "M", "U"]),
		"CardPinHMac": "",#self.generator.cardPinHmacAuthorization(cardNumber),
		"Wallets":[],
		}
		}

		if len(fields) > 0:
			d = dict((k, v) for (k, v) in d.items() if k in fields)

		return d
