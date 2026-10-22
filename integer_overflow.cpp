#include <iostream>
#include <limits>

int main() {
    short smallInt = 32767; // Maximum value for a short
    std:: cout << "Original Value: " << smallInt << std::endl;
    smallInt++;
    std::cout << "After Overflow: " << smallInt <<std::endl; // This will show the overflowed value

    unsigned int positiveOnly = 0;
    std::cout << "Unsigned Integer Start: " << positiveOnly << std::endl;
    positiveOnly--;
    std::cout << " Unsigned Integer Wrap-around: " << positiveOnly << std::endl; // This will show the wrap-around value
    
    std::cout << "\nInteger Type Limits: " << std::endl;
    std::cout << "Short Max: " << std::numeric_limits::max() << std::endl;
    std::cout << "Short Min: " << std::numeric_limits::min() << std::endl;

    try {
        if (smallInt < std::numeric_limits::max()) {
            smallInt++; std::cout << "Safe Increment: " << smallInt << std::endl;
        } else {
            std::cout << "Cannot increment further" << std::endl; }
    }catch (const std::overflow_error& e) {
        std::cout << "Overflow Error: " << e.what() << std::endl;

    return 0;
    }
}