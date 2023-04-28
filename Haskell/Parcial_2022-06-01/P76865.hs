data Tree a = Empty | Node a (Tree a) (Tree a)
        deriving (Show)

instance Foldable Tree where
    foldr f x Empty = x
    foldr f x (Node a l r) = foldr f (foldr f (f a x) l) r

avg :: Tree Int -> Double
avg t = s/l
    where 
        s = fromIntegral(sum t)
        l = fromIntegral(length t)

cat :: Tree String -> String
cat t = foldr (\x y -> if y == [] then x else y ++ " " ++ x) [] t