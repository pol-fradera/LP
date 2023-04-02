countIf :: (Int -> Bool) -> [Int] -> Int
countIf f [] = 0
countIf f (x:xs) 
        | f x = 1 + countIf f xs
        | otherwise = countIf f xs

pam :: [Int] -> [Int -> Int] -> [[Int]]
pam xs [] = []
pam xs (y:ys) = [map y xs] ++ pam xs ys 

pam2 :: [Int] -> [Int -> Int] -> [[Int]]
pam2 xs fs = map (\x -> map ($ x) fs) xs              

filterFoldl :: (Int -> Bool) -> (Int -> Int -> Int) -> Int -> [Int] -> Int
filterFoldl _ _ xo [] = xo
filterFoldl f op xo (x:xs) 
        | f x = filterFoldl f op (op xo x) xs
        | otherwise = filterFoldl f op xo xs

insert :: (Int -> Int -> Bool) -> [Int] -> Int -> [Int]
insert f [] y = [y]
insert f (x:xs) y
        | f y x = y : x : xs
        | otherwise = x : insert f xs y

insertionSort :: (Int -> Int -> Bool) -> [Int] -> [Int]
insertionSort f [] = []
insertionSort f (x:xs) = insert f (insertionSort f xs) x 