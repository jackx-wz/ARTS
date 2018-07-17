pragma solidity ^0.4.21;

contract token {
    mapping (address => uint) public coinBalanceOf;
    function constrction() public pure{}

    function sendCoin(address receiver, uint amount) public returns(bool sufficient) { 
    } 
}

contract Crowdsale {
    
    address public beneficiary;
    address owner;
    uint public fundingGoal;
    uint public amountRaised;
    uint public deadline;
    uint public price;
    token public tokenReward;   
    Funder[] public funders;
    event FundTransfer(address backer, uint amount, bool isContribution);
    
    /* data structure to hold information about campaign contributors */
    struct Funder {
        address addr;
        uint amount;
    }
    
    /*  at initialization, setup the owner */
    function constrction(address _beneficiary, uint _fundingGoal, uint _duration, uint _price, token _reward) public {
        beneficiary = _beneficiary;
        fundingGoal = _fundingGoal;
        deadline = now + _duration * 1 minutes;
        price = _price;
        owner = msg.sender;
        tokenReward = token(_reward);
    }   
    
    /* The function without name is the default function that is called whenever anyone sends funds to a contract */
    function () public payable {
        uint amount = msg.value;
        funders[funders.length++] = Funder({addr: msg.sender, amount: amount});
        amountRaised += amount;
        tokenReward.sendCoin(msg.sender, amount / price);
        emit FundTransfer(msg.sender, amount, true);
    }
        
    modifier afterDeadline() {
        if (now >= deadline) _;
    }

    /* checks if the goal or time limit has been reached and ends the campaign */
    function checkGoalReached() public afterDeadline {
        if (amountRaised >= fundingGoal){
            beneficiary.transfer(amountRaised);
            emit FundTransfer(beneficiary, amountRaised, false);
        } else {
            emit FundTransfer(0, 11, false);
            for (uint i = 0; i < funders.length; ++i) {
                funders[i].addr.transfer(funders[i].amount);  
                emit FundTransfer(funders[i].addr, funders[i].amount, false);
            }               
        }
        selfdestruct(beneficiary);
    }

    function kill() public {
        if(owner == msg.sender){
            selfdestruct(owner);
        }
    }
}