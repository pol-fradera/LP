insert :: [Int] -> Int -> [Int]
insert [] x = [x]
insert (x:xs) y
    | y >= x = x : insert xs y
    | otherwise = y : x : xs

isort :: [Int] -> [Int] 
isort [] = []
isort (x:xs) = insert (isort xs) x


remove :: [Int] -> Int -> [Int]
remove (x:xs) y 
    | x == y = xs
    | otherwise = x : remove xs y

ssort :: [Int] -> [Int] 
ssort [] = []
ssort xs = min : ssort (remove xs min)
    where min = minimum xs

merge :: [Int] -> [Int] -> [Int] 
merge [] xs = xs
merge xs [] = xs
merge (x:xs) (y:ys) 
    | x <= y = x : merge xs (y:ys)
    | otherwise = y : merge (x:xs) ys

msort :: [Int] -> [Int] 
msort [] = []
msort [x] = [x]
msort xs = merge (msort esq) (msort dre)
    where
        esq = take mida_e xs
        dre = drop mida_e xs
        mida_e = (div (length xs) 2)
       

qsort :: [Int] -> [Int]
qsort []     = []
qsort (p:xs) = (qsort menors) ++ [p] ++ (qsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]

genQsort :: Ord a => [a] -> [a]
genQsort []     = []
genQsort (p:xs) = (genQsort menors) ++ [p] ++ (genQsort majors)
    where
        menors = [x | x <- xs, x <  p]
        majors = [x | x <- xs, x >= p]