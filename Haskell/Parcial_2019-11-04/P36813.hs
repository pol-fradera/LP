import Data.List

degree :: Eq a => [(a, a)] -> a -> Int
degree [] _ = 0
degree ((a,b):xs) x = if (x == a || x == b) then 1 + (degree xs x) else (degree xs x)

degree' :: Eq a => [(a, a)] -> a -> Int
degree' l x = foldl (\ant (a,b) -> if (a == x || b == x) then ant+1 else ant) 0 l

neighbors :: Ord a => [(a, a)] -> a -> [a]
neighbors l x = sort $ foldl (\ant (a,b) -> if (a == x) then b:ant else if (b == x) then a:ant else ant) [] l

arestesneighbors :: Ord a => [(a, a)] -> a -> [(a,a)]
arestesneighbors l x = sort $ filter (\(a,b) -> if (a == x || b == x) then True else False) l 
