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
        
        # Calculate amountIn and amountOut
        amount_in = token_amount
        amount_out = calculate_balance(token_amount, input_reserve, output_reserve)
#        print(f"Transaction: Convert {amount_in:.2f} {input_token} to {amount_out:.2f} {output_token}")
        
        token_amount = amount_out
    return token_amount

# Define the conversion path and initial amount
conversion_path = ["tokenB", "tokenA", "tokenD", "tokenB"]
initial_amount = 5

# Perform token conversion and calculate final tokenB balance
final_balance = convert_tokens(conversion_path, initial_amount)

# Print the result
print("Path:", "->".join(conversion_path), ", TokenB balance =", final_balance)

#conversion_path_most = ["tokenB", "tokenE", "tokenB", "tokenD", "tokenC", "tokenE", "tokenD", "tokenC", "tokenE", "tokenD", "tokenC", "tokenB"]
conversion_path_most = ["tokenB", "tokenA", "tokenD", "tokenC", "tokenB"]
#tokenB->tokenA->tokenC->tokenB->tokenD->tokenC->tokenB
final_balance_most = convert_tokens(conversion_path_most, initial_amount)
# print("Path:", "->".join(conversion_path_most), ", TokenB balance most =", final_balance_most)



