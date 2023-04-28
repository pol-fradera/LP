myFoldl :: (a -> b -> a) -> a -> [b] -> a
myFoldl f y [] = y
myFoldl f y (x:xs) = myFoldl f (f y x) xs

myFoldr :: (a -> b -> b) -> b -> [a] -> b
myFoldr f y [] = y
myFoldr f y (x:xs) = f x (myFoldr f y xs)

myIterate :: (a -> a) -> a -> [a]
myIterate f x = x : myIterate f (f x) 

myUntil :: (a -> Bool) -> (a -> a) -> a -> a
myUntil p f x 
    | p x = x
    | otherwise = myUntil p f (f x)

myMap :: (a -> b) -> [a] -> [b]
myMap f xs = foldr (\x y -> (f x):y ) [] xs

myFilter :: (a -> Bool) -> [a] -> [a]
myFilter f xs = foldr (\x y -> if (f x) then x:y else y) [] xs

myAll :: (a -> Bool) -> [a] -> Bool
myAll f xs = and (map f xs)

myAny :: (a -> Bool) -> [a] -> Bool
myAny f xs = or (map f xs)

myZip :: [a] -> [b] -> [(a, b)]
myZip [] _ = []
myZip _ [] = []
myZip (x:xs) (y:ys) = (x,y) : myZip xs ys

myZipWith :: (a -> b -> c) -> [a] -> [b] -> [c]
myZipWith f xs ys = myFoldr (\(x, y) a -> (f x y):a) [] (myZip xs ys)
