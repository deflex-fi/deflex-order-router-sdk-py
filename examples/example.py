from algosdk.v2client import algod
import algosdk
import msgpack

from deflex.v1.deflex_client import DeflexOrderRouterTestnetClient

senderAddress = 'DWQXOZMGDA6QZRSPER6O4AMTO3BQ6CEJMFO25EWRRBK72RJO54GLDCGK4E'
senderPk = algosdk.mnemonic.to_private_key('bottom stone elegant just symbol bunker review curve laugh burden jewel pepper replace north tornado alert relief wrist better property spider picture insect abandon tuna')

algodUri = '<INSERT_ALGOD_URI>'
algodToken = {
	'X-API-Key': '<INSERT_ALGOD_TOKEN>'
}
algodPort = ''
apiKey = '' # reach out to phil@deflex.com to get custom API key with higher rate limit
algod = algod.AlgodClient(algodToken['X-API-Key'], algodUri, algodToken)
params = algod.suggested_params()
inputAssetId = 0
outputAssetId = 10458941
amount = 1000000

client = DeflexOrderRouterTestnetClient(algodUri, algodToken, algodPort)
quote = client.get_fixed_input_swap_quote(inputAssetId, outputAssetId, amount)
requiredAppOptIns = quote.requiredAppOptIns

accountInfo = algod.account_info(senderAddress)
appsLocalState = accountInfo['apps-local-state']

# opt into required apps for swap
for requiredAppOptIn in requiredAppOptIns:
	requiredAppLocalState = [appLocalState['id'] == requiredAppOptIn for appLocalState in appsLocalState]
	if len(requiredAppLocalState) == 0:
		appOptIn = algosdk.future.transaction.ApplicationOptInTxn(senderAddress, params, requiredAppOptIn)
		signedAppOptIn = appOptIn.sign(senderPk)
		algod.send_transaction(signedAppOptIn)

slippage = 5

txnGroup = client.get_swap_quote_transactions(
	senderAddress,
	quote.txnPayload,
	slippage
)

signedTxns = []
for txn in txnGroup.txns:
	if txn.logicSigBlob:
		signedTxns.append(msgpack.unpackb(txn.logicSigBlob))
	else:
		txnObj = algosdk.encoding.future_msgpack_decode(txn.data)
		signedTxns.append(txnObj.sign(senderPk))

txId = algod.send_transactions(signedTxns)

print(txId)