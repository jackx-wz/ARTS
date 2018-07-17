pragma solidity ^0.4.17;

contract mortal {
    /* Define variable owner of the type address*/
    address owner;

    /* this function is executed at initialization and sets the owner of the contract */
    function construct() public { owner = msg.sender; }

    /* Function to recover the funds on the contract */
    function kill() public { if (msg.sender == owner) selfdestruct(owner); }
}

contract greeter is mortal {
    /* define variable greeting of the type string */
    string greeting;
    
    /* this runs when the contract is executed */
    function construct(string _greeting) public {
        greeting = _greeting;
    }

    /* main function */
    function greet() public view returns (string) {
        return greeting;
    }
}