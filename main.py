from web3 import Web3
from datetime import datetime

w3 = Web3(Web3.HTTPProvider('https://eth-sepolia.g.alchemy.com/v2/i0wKTERLjBoAFlhdiXLhiphs5kIwvfNe' ))

block_number = 'latest'

block = w3.eth.get_block(block_number, full_transactions=True)

timestamp = block['timestamp']
dt = datetime.utcfromtimestamp(timestamp).strftime('%Y-%m-%d %H:%M:%S UTC')

print(f"\n�� Bloco: {block['number']}")
print(f"⛏️ Minerador: {block['miner']}")
print(f"📅 Data e hora do bloco: {dt}")
print(f"💼 Total de transações: {len(block['transactions'])}\n")

for idx, tx in enumerate(block['transactions']):
    from_addr = tx['from']
    to_addr = tx['to']
    value_wei = tx['value']
    value_eth = w3.from_wei(value_wei, 'ether')

    print(f"🔸 Transação {idx + 1}:")
    print(f"🕒 Data e hora: {dt}")
    print(f"🔹 De: {from_addr}")
    print(f"🔸 Para: {to_addr}")
    print(f"💰 Valor: {value_eth} ETH\n")
