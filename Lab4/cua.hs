data Queue a = Queue [a] [a]
    deriving (Show)

c = push 3 (push 2 (push 1 create))
c1 = push 4 (pop (push 3 (push 2 (push 1 create))))
c2 = push 4 (push 3 (push 2 create))

create :: Queue a
create = Queue [] []

push :: a -> Queue a -> Queue a
push a (Queue xs ys) = Queue xs (a:ys)

pop' :: Queue a -> Queue a
pop' (Queue (x:xs) []) = Queue xs []
pop' (Queue xs (y:ys)) = pop' (Queue (y:xs) ys)

pop :: Queue a -> Queue a
pop (Queue [] []) = Queue [] []
pop (Queue [] (y:ys)) = pop' (Queue [y] ys)
pop (Queue (x:xs) ys) = Queue xs ys

top' :: Queue a -> a
top' (Queue (x:xs) []) = x
top' (Queue xs (y:ys)) = top' (Queue (y:xs) ys)

top :: Queue a -> a
top (Queue [] (y:ys)) = top' (Queue [y] ys)
top (Queue (x:xs) _) = x

empty :: Queue a -> Bool
empty (Queue [] []) = True
empty _ = False 

-- igual :: Eq a => [a] -> [a] -> Bool
-- igual [] [] = True
-- igual [] _ = False
-- igual _ [] = False
-- igual (x:xs) (y:ys) = (x==y) && (igual xs ys)

instance Eq a => Eq (Queue a)
    where
        (Queue x1s y1s) == (Queue x2s y2s) = (x1s ++ reverse y1s) == (x2s ++ reverse y2s)   