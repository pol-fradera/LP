fizzBuzz :: [Either Int String]
fizzBuzz = map evaluate (iterate (+1) 0)
    where evaluate x 
            | mod x 15 == 0 = Right "FizzBuzz"
            | x `mod` 3 == 0 = Right "Fizz"
            | x `mod` 5 == 0 = Right "Buzz"
            | otherwise = Left x 
