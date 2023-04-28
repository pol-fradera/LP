flatten :: [[Int]] -> [Int]
flatten xs = concatMap (id) xs

myLength :: String -> Int
myLength xs = foldl (+) 0 ys
    where ys = map (const 1) xs

myReverse :: [Int] -> [Int]
myReverse xs = scanl (-) 0 ys
    where ys = scanr (+) 0 xs

countIn :: [[Int]] -> Int -> [Int]
countIn xs y = map length ys
    where ys = map (filter (== y)) xs

firstWord :: String -> String
firstWord xs = takeWhile (/= ' ') ys
    where ys = dropWhile (== ' ') xs