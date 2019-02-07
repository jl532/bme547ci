# bme547ci

## Specifications  
The function is_tachycardic within tachycardic.py does the following:
* It should take a string argument as input.
* This string will only contain a single word, but there is no guarantee whether the word will be upper case, lower case, mixed case, or have leading / trailing spaces or punctuation.
* If the string contains the word "tachycardic," regardless of capitalization, the function should return a value of True
* Otherwise, the function should return a value of False.
* Function must follow the PEP-8 style guide.

## As a whole, the full repository has the following:  
* Implementation of Travis CI
* Presence of comprehensive unit testing to ensure that the appropriate range of possible string inputs are successfully identified or rejected
* The use of @pytest.mark.parametrize for at least one unit test
* Appropriate naming and syntax for unit tests
* Appropriate use of virutal environments  
**Additionally, is_tachycardic is tolerant to close representations of the word tachycardic. For example, it should be able to tolerate 1 to 2 missing letters (ex. tachycrdic) and/or 1 to 2 misspelled letters (ex. tachycard1c)**