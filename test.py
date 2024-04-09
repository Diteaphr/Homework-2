from itertools import product

# Define the liquidity pool reserve data
liquidity = {
    ("tokenA", "tokenB"): (17, 10),
    ("tokenA", "tokenC"): (11, 7),
    ("tokenA", "tokenD"): (15, 9),
    ("tokenA", "tokenE"): (21, 5),
    ("tokenB", "tokenC"): (36, 4),
    ("tokenB", "tokenD"): (13, 6),
    ("tokenB", "tokenE"): (25, 3),
    ("tokenC", "tokenD"): (30, 12),
    ("tokenC", "tokenE"): (10, 8),
    ("tokenD", "tokenE"): (60, 25),
}

# Function to calculate token balance after conversion with fee
def calculate_balance(input_amount, input_reserve, output_reserve, fee=0.003):
    input_amount_with_fee = input_amount * (1 - fee)
    return (input_amount_with_fee * output_reserve) / (input_reserve + input_amount_with_fee)

# Function to perform token conversion along a path
def convert_tokens(path, amount):
    token_amount = amount
    for i in range(len(path) - 1):
        input_token, output_token = path[i], path[i + 1]
        # Check if the liquidity pair exists in the dictionary
        if (input_token, output_token) in liquidity:
            input_reserve, output_reserve = liquidity[(input_token, output_token)]
        elif (output_token, input_token) in liquidity:
            output_reserve, input_reserve = liquidity[(output_token, input_token)]
        else:
            raise ValueError(f"No liquidity pair found for {input_token} to {output_token}")
        token_amount = calculate_balance(token_amount, input_reserve, output_reserve)
    return token_amount

# Define the function to generate valid permutations
def generate_valid_permutations():
    tokens = ['tokenA', 'tokenB', 'tokenC', 'tokenD', 'tokenE']
    valid_permutations = {}

    for length in range(3, 8):  # 从3个元素到7个元素
        valid_permutations[length] = []
        for perm in product(tokens, repeat=length):
            if perm[0] == 'tokenB' and perm[-1] == 'tokenB':
                valid = True
                for i in range(len(perm) - 1):
                    if perm[i] == perm[i + 1]:
                        valid = False
                        break
                if valid:
                    valid_permutations[length].append(perm)

    return valid_permutations

# Generate valid permutations
valid_permutations = generate_valid_permutations()

# Test each permutation for profitability
profitable_permutations = {}
for length, permutations in valid_permutations.items():
    profitable_permutations[length] = []
    for perm in permutations:
        final_balance = convert_tokens(perm, 5)  # Initial tokenB amount is 5
        if final_balance > 20:
            profitable_permutations[length].append((perm, final_balance))

# Print the profitable permutations
print("Profitable permutations with final TokenB balance > 20:")
for length, permutations in profitable_permutations.items():
    print(f"长度为 {length} 的套利路径有以下 {len(permutations)} 种：")
    for perm, balance in permutations:
        print("Path:", "->".join(perm), ", Final TokenB balance:", balance)
