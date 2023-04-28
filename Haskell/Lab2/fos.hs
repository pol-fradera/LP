eql :: [Int] -> [Int] -> Bool 
eql xs ys 
    | length xs /= length ys = False
    | otherwise = all (== 0) zs
    where zs = zipWith (-) xs ys

prod :: [Int] -> Int
prod xs = foldl (*) 1 xs

prodOfEvens :: [Int] -> Int
prodOfEvens xs = foldl (*) 1 ys
    where ys = filter even xs

powersOf2 :: [Int]
powersOf2 = iterate (*2) 1

scalarProduct :: [Float] -> [Float] -> Float
scalarProduct xs ys = foldl (+) 0 zs
    where zs = zipWith (*) xs ys
