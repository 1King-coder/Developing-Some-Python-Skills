from Calculador_de_IPV4 import CalculadorIPV4

calc_ipv4 = CalculadorIPV4('127.0.0.1', mask='255.0.0.0')

print(f'\033[1;33mIP: \033[1;34m{calc_ipv4.ip}\033[m')
print(f'\033[1;33mMáscara: \033[1;34m{calc_ipv4.mask}\033[m')
print(f'\033[1;33mPrefixo: \033[1;34m{calc_ipv4.prefix}\033[m')
print(f'\033[1;33mRede: \033[1;34m{calc_ipv4.network}\033[m')
print(f'\033[1;33mBroadcast: \033[1;34m{calc_ipv4.broadcast}\033[m')
print(
    f'\033[1;33mNúmero de IPs da rede: \033[1;34m{calc_ipv4.number_ips}\033[m')
