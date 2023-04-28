data Tree a = Node a (Tree a) (Tree a) | Empty deriving (Show)

t7 = Node 7 Empty Empty
t6 = Node 6 Empty Empty
t5 = Node 5 Empty Empty
t4 = Node 4 Empty Empty
t3 = Node 3 t6 t7
t2 = Node 2 t4 t5
t1 = Node 1 t2 t3
t1' = Node 1 t3 t2

size :: Tree a -> Int
size Empty = 0
size (Node _ fe fd) = 1 + size(fe) + size(fd)

height :: Tree a -> Int
height Empty = 0
height (Node _ fe fd) = 1 + max (height(fe)) (height(fd))

equal :: Eq a => Tree a -> Tree a -> Bool
equal Empty Empty = True
equal Empty _ = False
equal _ Empty = False
equal (Node a fea fda) (Node b feb fdb) 
    | a == b = (equal fea feb) && (equal fda fdb)
    | otherwise = False

isomorphic :: Eq a => Tree a -> Tree a -> Bool
isomorphic Empty Empty = True
isomorphic Empty _ = False
isomorphic _ Empty = False
isomorphic (Node a fea fda) (Node b feb fdb) 
    | a == b = (equal fea feb && equal fda fdb) || (equal fea fdb && equal fda feb)
    | otherwise = False

preOrder :: Tree a -> [a]
preOrder Empty = []
preOrder (Node a fe fd) = a : preOrder fe ++ preOrder fd

postOrder :: Tree a -> [a]
postOrder Empty = []
postOrder (Node a fe fd) = postOrder fe ++ postOrder fd ++ [a]

inOrder :: Tree a -> [a]
inOrder Empty = []
inOrder (Node a fe fd) = inOrder fe ++ [a] ++ inOrder fd

breadthFirst :: Tree a -> [a]
breadthFirst t = bf [t]
    where  
        bf :: [Tree a] -> [a]
        bf [] = []
        bf (Empty:ts) = bf ts
        bf ((Node x t1 t2):ts) = [x] ++ bf (ts++[t1,t2]) 


build :: Eq a => [a] -> [a] -> Tree a
build [] [] = Empty
build (x:xs) (ys) = Node x l r
    where   
        l = build x1s y1s
        r = build x2s y2s
        (y1s,y2s) = split x ys  --separo la llista in-ordre en fill esquerra i fill dret
        (x1s,x2s) = splitAt (length y1s) xs -- separo la llista preordre en el fill esquerra i fill dret

split :: Eq a => a -> [a] -> ([a],[a])
split _ [] = ([],[])
split x l = (takeWhile (/= x) l, tail (dropWhile (/= x) l))

overlap :: (a -> a -> a) -> Tree a -> Tree a -> Tree a
overlap _ Empty Empty = Empty
overlap _ esq Empty = esq
overlap _ Empty dre = dre
overlap f (Node a fea fda) (Node b feb fdb) = Node (f a b) (overlap f fea feb) (overlap f fda fdb)