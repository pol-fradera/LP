import Data.List (unfoldr)

myUnfoldr :: (b -> Maybe (a, b)) -> b -> [a]
myUnfoldr f x = case f x of
  Nothing -> []
  Just (y, z) -> y : myUnfoldr f z

myReplicate :: a -> Int -> [a]
myReplicate x n = myUnfoldr (\y -> if y == 0 then Nothing else Just(x,y-1)) n

myIterate :: (a -> a) -> a -> [a] 
myIterate f x = myUnfoldr (\y -> Just(y,(f y))) x

myMap :: (a -> b) -> [a] -> [b]
myMap f xs = myUnfoldr generar xs
  where
    generar [] = Nothing
    generar (x:xs) = Just (f x, xs)


data Bst a = Empty | Node a (Bst a) (Bst a) 
 
add :: Ord a => a -> (Bst a) -> (Bst a)
add x Empty = Node x Empty Empty
add x (Node y l r)
    | x < y          = Node y (add x l) r
    | x > y          = Node y l (add x r)
    | otherwise = Node y l r

instance Show a => Show (Bst a) where
    show Empty = "."
    show (Node x l r) = "(" ++ show x ++ " " ++ show l ++ " " ++ show r ++ ")"


adder :: Ord a => (Bst a, [a]) -> Maybe (Bst a, (Bst a, [a]))
adder (a, []) = Nothing
adder (a, x:xs) = Just ((add x a),((add x a), xs))

