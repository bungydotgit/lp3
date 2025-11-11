// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Simple Bank Contract
/// @author GPT-5
/// @notice This contract allows deposits, withdrawals, and balance checks.

contract SimpleBank {
    // Mapping to store balances of each customer (address)
    mapping(address => uint256) private balances;

    /// @notice Deposit ether into your bank account
    function deposit() public payable {
        require(msg.value > 0, "Deposit must be greater than zero");
        balances[msg.sender] += msg.value;
    }

    /// @notice Withdraw ether from your bank account
    /// @param amount The amount (in wei) to withdraw
    function withdraw(uint256 amount) public {
        require(amount > 0, "Amount must be greater than zero");
        require(balances[msg.sender] >= amount, "Insufficient balance");

        balances[msg.sender] -= amount;

        // Transfer ether back to the sender
        payable(msg.sender).transfer(amount);
    }

    /// @notice Returns the current balance of the caller
    /// @return balance The balance of the caller in wei
    function getBalance() public view returns (uint256 balance) {
        return balances[msg.sender];
    }
}
