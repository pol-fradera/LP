data Tree a = Empty | Node a (Tree a) (Tree a)

instance Show a => Show (Tree a) where
    show Empty = "()"
    show (Node x l r) = "(" ++ show l ++ "," ++ show x ++ "," ++ show r ++ ")"

instance Num a => Functor (Tree a) where
    fmap f Empty = Empty
    fmap f (Node x l r) = (Node (f x) (fmap f l) (fmap f r))
    

doubleT :: Num a ⇒ Tree a → Tree a
doubleT t = fmap (*2) t