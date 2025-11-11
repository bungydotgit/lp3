// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/// @title Student Data Management Contract
/// @notice Demonstrates use of Structs, Arrays, and Fallback function in Solidity
contract StudentData {
    // Structure to store student details
    struct Student {
        uint256 rollNo;
        string name;
        uint256 marks;
    }

    // Dynamic array to hold all student records
    Student[] public students;

    // Event to log when a student is added
    event StudentAdded(uint256 rollNo, string name, uint256 marks);

    // Function to add a new student
    function addStudent(uint256 _rollNo, string memory _name, uint256 _marks) public {
        students.push(Student(_rollNo, _name, _marks));
        emit StudentAdded(_rollNo, _name, _marks);
    }

    // Function to get student details by index
    function getStudent(uint256 index) public view returns (uint256, string memory, uint256) {
        require(index < students.length, "Invalid index");
        Student memory s = students[index];
        return (s.rollNo, s.name, s.marks);
    }

    // Function to get total number of students
    function getTotalStudents() public view returns (uint256) {
        return students.length;
    }

    // Fallback function to handle any unexpected Ether transfers or calls
    fallback() external payable {
        // If Ether is sent directly, accept it silently
    }

    // Receive function to handle direct Ether transfers
    receive() external payable {}
}
