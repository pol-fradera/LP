ones :: [Integer]
ones = 1 : ones

nats :: [Integer]
nats = 0 : map (+1) nats

ints :: [Integer]
ints = iterate (\x -> if x > 0 then -x else -x+1) 0

triangulars :: [Integer]
triangulars = 0 : scanl (+) 1 (tail $ tail nats)

factorials :: [Integer]
factorials = scanl (*) 1 (tail nats)

fibs :: [Integer]
fibs = 0 : 1 : zipWith (+) fibs (tail fibs)

primes :: [Integer]
primes = garbell (tail $ tail nats)
    where
        garbell (p : xs) = p : garbell (filter (\x -> x `mod` p /= 0) xs)

hammings :: [Integer]
hammings = 1 : map (2*) hammings `merge` map (3*) hammings `merge` map (5*) hammings
  where merge (x:xs) (y:ys)
          | x < y = x : xs `merge` (y:ys)
          | x > y = y : (x:xs) `merge` ys
          | otherwise = x : xs `merge` ys

look :: [Char] -> Integer
look [] = 0
look [_] = 1
look (c1:c2:s)
    | c1 == c2 = 1 + (look (c2:s))
    | otherwise = 1

say :: [Char] -> [Char]
say [] = []
say s = (show count) ++ (head s) : (say (drop (fromIntegral count) s)) where count = look s

lookNsay :: [Integer]
lookNsay = iterate (read . say . show) 1
        
tartaglia :: [[Integer]]
tartaglia = iterate next [1]
    where next xs = zipWith (+) ([0] ++ xs) (xs ++ [0])