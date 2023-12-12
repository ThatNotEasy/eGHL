import hashlib
import uuid
import requests
import urllib.parse

SERVICE_ID = 'OnlyGodKnowThis'
MERCHANT_PW = 'OnlyGodKnowThis'

PAYMENT_ID = str(uuid.uuid4())
CURRENCY_CODE = 'MYR'
AMOUNT = '10.00'
TIMEOUT = '600'

MERCHANT_RETURN = 'http://localhost/eGHL/return'
MERCHANT_APPROVAL = 'http://localhost/eGHL/approval'
MERCHANT_UNAPPROVAL = 'http://localhost/eGHL/unapproval'

DEV = "https://pay.e-ghl.com/IPGSG/Payment.aspx"
PROD = "https://securepay.e-ghl.com/IPG/Payment.aspx"

REFUND = 'REFUND'
SALE = 'SALE'
SETTLEMENT = 'SETTLEMENT'
QUERY = 'QUERY'
CAPTURE = 'CAPTURE'
REVERSAL = 'REVERSAL'

def ini_ip():
    response = requests.get('https://httpbin.org/ip')
    data = response.json()
    origin = data.get('origin')
    return origin

def tukang_hash():
    meow = (
        MERCHANT_PW
        + SERVICE_ID
        + PAYMENT_ID
        + MERCHANT_RETURN
        + AMOUNT
        + CURRENCY_CODE
        + ini_ip()
        + TIMEOUT
    )
    generated = hashlib.sha256(meow.encode('utf-8')).hexdigest()

    params = {
        'TransactionType': 'SALE',
        'PymtMethod': 'ANY',
        'ServiceID': SERVICE_ID,
        'PaymentID': PAYMENT_ID,
        'OrderNumber': PAYMENT_ID,
        'PaymentDesc': 'EXAMPLE',
        'MerchantReturnURL': MERCHANT_RETURN,
        'Amount': AMOUNT,
        'CurrencyCode': CURRENCY_CODE,
        'CustIP': ini_ip(),
        'CustName': 'EXAMPLE',
        'CustEmail': 'EXAMPLE',
        'CustPhone': '60123456789',
        'PageTimeout': TIMEOUT,
        'HashValue': generated
    }
    encoded_params = urllib.parse.urlencode(params)
    donde = f'{DEV}?{encoded_params}'
    return donde
