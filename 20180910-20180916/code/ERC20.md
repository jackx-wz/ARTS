# ERC20 代币标准

## Method
```
optional function name() constant returns (string name)

optional function symbol() constant returns (string symbol)

optional function decimals() constant returns (uint8 decimals)

required function totalSupply() constant returns (uint256 totalSupply)

required function balanceOf(address _owner) constant returns (uint256 balance)

required function transfer(address _to, uint256 _value) returns (bool success)
必须触发事件 Transfer

required function transferFrom(address _from, address _to, uint256 _value) returns (bool success)
必须触发事件 Transfer

required function approve(address _spender, uint256 _value) returns (bool success)

required function allowance(address _owner, address _spender) constant returns (uint256 remaining)
```

## Event

```
event Transfer(address indexed _from, address indexed _to, uint256 _value)

event Approval(address indexed _owner, address indexed _spender, uint256 _value)
在每次成功调用方法 approve 之后会触发
```