myLength :: [Int] -> Int
myLength [] = 0
myLength (_:xs) = 1 + myLength xs

myMaximum :: [Int] -> Int
myMaximum (x:xs) = myMaximum2 xs x 

myMaximum2 :: [Int] -> Int -> Int
myMaximum2 [] x = x
myMaximum2 (y:xs) x = if (y >= x) then myMaximum2 xs y 
                                  else myMaximum2 xs x

average :: [Int] -> Float
average xs = fromIntegral (sum xs) / fromIntegral (myLength xs)

buildPalindrome :: [Int] -> [Int]
buildPalindrome xs = reverse xs ++ xs

{-
remove :: [Int] -> [Int] -> [Int]
remove xs [] = xs
remove xs ys = remove (eliminar_element xs [] (head ys)) (tail ys)

eliminar_element :: [Int] -> [Int] -> Int -> [Int]
--el segon paràmetre inicialment és una llista buida
eliminar_element xs res x
        | myLength xs == 0 = res
        | x == y = eliminar_element (init xs) res x  
        | otherwise = eliminar_element (init xs) (y:res) x
        where y = last xs
-}

remove :: [Int] -> [Int] -> [Int]
remove [] _ = []
remove (x:xs) ys
    | elem x ys = remove xs ys
    | otherwise = x : (remove xs ys)

flatten :: [[Int]] -> [Int]
flatten xs = concat xs

oddsNevens :: [Int] -> ([Int],[Int])
oddsNevens xs = oddsNevens2 xs ([],[])

oddsNevens2 :: [Int] -> ([Int],[Int]) -> ([Int],[Int])
oddsNevens2 xs (ys, zs)
        | myLength xs == 0 = (ys, zs)
        | odd x = oddsNevens2 (init xs) (x:ys, zs)
        | otherwise = oddsNevens2 (init xs) (ys, x:zs)
        where x = last xs


isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime x =  not (hasDivisor (x-1))
  where
    hasDivisor :: Int -> Bool
    hasDivisor 1 = False
    hasDivisor n = mod x n == 0 || hasDivisor (n-1)


primeDivisors :: Int -> [Int] 
primeDivisors x
    | isPrime x = [x]
    | otherwise = primeDivs x 2
    where
        primeDivs :: Int -> Int -> [Int]
        primeDivs x y 
          | y > (div x 2) = []
          | ((mod x y) == 0) && (isPrime y) = y : primeDivs x (y+1)
          | otherwise = primeDivs x (y+1)

{-
primeDivisors :: Int -> [Int]
primeDivisors n = primeDivisors2 n n []

primeDivisors2 :: Int -> Int -> [Int] -> [Int]
primeDivisors2 n x xs 
        | primer == False = xs
        | otherwise = primeDivisors2 n (segon-1) (segon:xs)
        where tupla = hasDivisors2 n x
              primer = fst(tupla)
              segon = snd(tupla)


hasDivisors2 :: Int -> Int -> (Bool,Int)
hasDivisors2 n divisor
    | divisor <= 2 = (False,-1)
    | (mod n divisor == 0) && (isPrime divisor) = (True,divisor)
    | otherwise = hasDivisors2 n (divisor - 1)


isPrime :: Int -> Bool
isPrime 0 = False
isPrime 1 = False
isPrime n = not (hasDivisors n 2)

hasDivisors :: Int -> Int -> Bool
hasDivisors n divisor
    | divisor * divisor > n = False
    | mod n divisor == 0 = True
    | otherwise = hasDivisors n (divisor + 1)
-}