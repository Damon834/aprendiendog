#include <iostream> // Required for input and output operations

int main()
{
    double num1, num2; // Declare variables to store the two numbers
    char operation;    // Declare a variable to store the operation (+, -, *, /)

    // Prompt the user to enter the first number
    std::cout << "Enter the first number: ";
    std::cin >> num1; // Read the first number from the user

    // Prompt the user to enter the operation
    std::cout << "Enter an operation (+, -, *, /): ";
    std::cin >> operation; // Read the operation from the user

    // Prompt the user to enter the second number
    std::cout << "Enter the second number: ";
    std::cin >> num2; // Read the second number from the user

    double result; // Declare a variable to store the result

    // Use a switch statement to perform the calculation based on the operation
    switch (operation)
    {
    case '+':
        result = num1 + num2;
        std::cout << "Result: " << num1 << " + " << num2 << " = " << result << std::endl;
        break; // Exit the switch statement

    case '-':
        result = num1 - num2;
        std::cout << "Result: " << num1 << " - " << num2 << " = " << result << std::endl;
        break;

    case '*':
        result = num1 * num2;
        std::cout << "Result: " << num1 << " * " << num2 << " = " << result << std::endl;
        break;

    case '/':
        // Check for division by zero
        if (num2 != 0)
        {
            result = num1 / num2;
            std::cout << "Result: " << num1 << " / " << num2 << " = " << result << std::endl;
        }
        else
        {
            std::cout << "Error: Division by zero is not allowed." << std::endl;
        }
        break;

    default:
        // Handle invalid operations
        std::cout << "Error: Invalid operation. Please use +, -, *, or /." << std::endl;
        break;
    }

    return 0; // Indicate successful program execution
}