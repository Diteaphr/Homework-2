# 2024-Spring-HW2

Please complete the report problem below:

## Problem 1
Provide your profitable path, the amountIn, amountOut value for each swap, and your final reward (your tokenB balance).

> Solution

Transaction: Convert 5.00 tokenB to 5.66 tokenA
Transaction: Convert 5.66 tokenA to 2.46 tokenD
Transaction: Convert 2.46 tokenD to 5.09 tokenC
Transaction: Convert 5.09 tokenC to 20.13 tokenB
Path: tokenB->tokenA->tokenD->tokenC->tokenB , 
TokenB balance = 20.129888944077447

## Problem 2
What is slippage in AMM, and how does Uniswap V2 address this issue? Please illustrate with a function as an example.

> Solution

Slippage in AMM means that there's a discrepancy between expected quoted price and the actual price which the trade is actually executed because of the price movements caused by the constant rebalancing of liquidity pools.

Uniswap V2 addresses this issue by introducing a feature called "constant product with fees." This version of Uniswap includes a fee on every trade, which is collected and distributed to liquidity providers. 

The formula goes :
$( x + ∆x \times 0.997) \times (y - ∆y)  = k = x \times y$

Where:

∆x is the change in the amount of token x due to the trade
∆y is the change in the amount of token y due to the trade
0.997 is the fee multiplier (1 minus the fee percentage)

The transaction fee could incentivizing liquidity providers, and also encouraging arbitrage.


## Problem 3
Please examine the mint function in the UniswapV2Pair contract. Upon initial liquidity minting, a minimum liquidity is subtracted. What is the rationale behind this design?

> Solution

The rationale behind this design is primarily to prevent the liquidity pool from being dominated by very small liquidity providers, ensuring the pool's efficiency, stability, and integrity. It helps facilitate smoother trading and reduces the impact of slippage, and also prevent from being manipulated by malicious actors adding negligible amounts of liquidity to control the price of assets in the pool.


## Problem 4
Investigate the minting function in the UniswapV2Pair contract. When depositing tokens (not for the first time), liquidity can only be obtained using a specific formula. What is the intention behind this?

> Solution

The intention behind using this formula when depositing tokens is to ensure that the liquidity pool remains balanced and that liquidity providers are appropriately compensated for their contributions.It also helps maintain the integrity and efficiency of the Uniswap liquidity pools, as it prevents liquidity providers from disproportionately benefiting from their contributions or diluting the pool with excessive amounts of liquidity tokens.



## Problem 5
What is a sandwich attack, and how might it impact you when initiating a swap?

> Solution
In a sandwich attack, a malicious actor strategically places buy and sell orders around a target transaction to manipulate the price in their favor and profit from the price movement caused by the target transaction.

In a sandwich attack, a malicious actor strategically places buy and sell orders around a target transaction to manipulate the price in their favor and profit from the price movement caused by the target transaction. As a result, the trader may experience losses on their trade. If they are buying assets, they may receive fewer assets than expected for the same amount of input currency. Conversely, if they are selling assets, they may receive less currency than expected for the assets they're selling.

