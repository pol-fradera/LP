eval1 :: String -> Int
eval1 l = eval1' (words l) []

eval1' :: [String] -> [Int] -> Int
eval1' [] (y:p) = y
eval1' l p
    | x ==  "+" = eval1' (tail l) ((e2+e1):(tail $ tail p))
    | x ==  "-" = eval1' (tail l) ((e2-e1):(tail $ tail p))
    | x ==  "*" = eval1' (tail l) ((e2*e1):(tail $ tail p))
    | x ==  "/" = eval1' (tail l) ((div e2 e1):(tail $ tail p))
    | otherwise = eval1' (tail l) (z:p)
        where 
            x = head l
            z = read (x):: Int
            e1 = head p
            e2 = head $ tail p


fsmap :: a -> [a -> a] -> a
fsmap x [] = x
fsmap x (f:fs) = fsmap (f x) fs