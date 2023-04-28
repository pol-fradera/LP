absValue :: Int -> Int
absValue n = if (n >= 0) then n else -n

power :: Int -> Int -> Int
power _ 0 = 1
power x p = x * power x (p-1)

isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime n = not (hasDivisors n 2)

hasDivisors :: Int -> Int -> Bool
hasDivisors n divisor
    | divisor * divisor > n = False
    | mod n divisor == 0 = True
    | otherwise = hasDivisors n (divisor + 1)

slowFib :: Int -> Int
slowFib 0 = 0
slowFib 1 = 1
slowFib n = slowFib (n-1) + slowFib (n-2)

quickFib :: Int -> Int
quickFib n = quickFib' 0 1 n

quickFib' :: Int -> Int -> Int -> Int
quickFib' a b 0 = a
quickFib' a b iteration = quickFib' b (a + b) (iteration - 1)

{-
esDivisible :: Int -> Int -> Bool
esDivisible x y
        | y == 1 = False
        | mod x y == 0 = True
        | otherwise = esDivisible x (y-1)


comprovarArrel :: Int -> Bool
comprovarArrel x
        | fromIntegral(floor z) == z = False
        | otherwise = not (esDivisible x (floor z))
        where 
            y = fromIntegral x
            z = sqrt y

isPrime :: Int -> Bool 
isPrime 0 = False
isPrime 1 = False
isPrime x = comprovarArrel x
-}