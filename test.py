import pyupbit

access = "V1nSuhOfXgElKshr78xnMxcTInVferEgjmxLh0R4"          # 본인 값으로 변경
secret = "KfTdO8eMcy6hbJZtBuopZEEnBJVAxk6XaxFzo4BN"          # 본인 값으로 변경
upbit = pyupbit.Upbit(access, secret)

print(upbit.get_balance("KRW-BTC"))     # KRW-XRP 조회
print(upbit.get_balance("KRW"))         # 보유 현금 조회