# 智能合约教程
[智能合约教程](https://github.com/ethereum/go-ethereum/wiki/Contract-Tutorial)

比较长，感觉需要分几次进行学习

## Your first citizen
主要是通过这个例子，来认识智能合约是什么。智能合约就是在区块链上运行的一段程序，一个智能合约可以看成是一个类或者多个类的集合。

智能合约可以做很多事情，就像普通的程序语言一样。

这个例子是输入一个值，所有人都可以调用相应的方法得到这个值。

code:
[greeter.sol](code/blockchain/greeter.sol)

## 调用智能合约
智能合约的部署官方说已经从 geth 客户端移除了，于是我们直接用了官方钱包 Ethereum Wallet

调用智能合约关键是两点：
> 智能合约的ABI(Application Binary Interface)

> 智能合约的地址

```
> var abi=[ { "constant": false, "inputs": [], "name": "kill", "outputs": [], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": false, "inputs": [ { "name": "receiver", "type": "address" }, { "name": "amount", "type": "uint256" } ], "name": "sendCoin", "outputs": [ { "name": "sufficient", "type": "bool" } ], "payable": false, "stateMutability": "nonpayable", "type": "function" }, { "constant": true, "inputs": [ { "name": "", "type": "address" } ], "name": "coinBalanceOf", "outputs": [ { "name": "", "type": "uint256", "value": "0" } ], "payable": false, "stateMutability": "view", "type": "function" }, { "inputs": [ { "name": "supply", "type": "uint256", "index": 0, "typeShort": "uint", "bits": "256", "displayName": "supply", "template": "elements_input_uint", "value": "10000" } ], "payable": false, "stateMutability": "nonpayable", "type": "constructor" }, { "anonymous": false, "inputs": [ { "indexed": false, "name": "sender", "type": "address" }, { "indexed": false, "name": "receiver", "type": "address" }, { "indexed": false, "name": "amount", "type": "uint256" } ], "name": "CoinTransfer", "type": "event" } ]
undefined
> var addr = "0x26aF69471eb541Ed660E38D5F87f819950045613"
undefined
> my_contract = eth.contract(abi).at(addr)
```

这样使用 my_contract 就可以操作合约了。


## The Coin
代币发行，这里的代币并没有遵守 ERC20 协议内容。只是一个记账的协议。不过已经能够达到目的了。

[Coin.sol](code/blockchain/Coin.sol)

## Crowdfound Your Idea
众筹是发币的关键，现在很多空气币就靠这个圈钱。这里就要使用众筹的方式，让别人来买上面发的代币。所以众筹协议要做到自动根据买家发的货币进行发币活动。由于要进行自动发币，所以众筹智能合约的账户必须拥有上面发的币。

要让智能合约自动发币，就必须使用一个匿名函数，在每次交易的时候都会调用到。
[Crowdsale.sol](code/blockchain/Crowdsale.sol)