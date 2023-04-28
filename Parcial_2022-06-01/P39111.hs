import Data.List (sort)
type Pos = (Int, Int)

dins :: Pos -> Bool
dins (f, c) = if (f < 1 || f > 8 || c < 1 || c > 8) then False else True

moviments :: Pos -> [Pos]
moviments (f,c) = filter dins xs
    where
        xs = [(f+2,c+1),(f+2, c-1),(f-2,c+1),(f-2,c-1),(f+1,c+2),(f-1,c+2),(f+1,c-2),(f-1,c-2)]

potAnar3 :: Pos -> Pos -> Bool
potAnar3 (ox,oy) (dx,dy) = potAnar3_2 (ox,oy) (dx,dy) 3

potAnar3_2 :: Pos -> Pos -> Int -> Bool
potAnar3_2 (ox,oy) (dx,dy) 1 = elem (dx,dy) $ moviments (ox,oy)
potAnar3_2 (ox,oy) (dx,dy) n = if (any (\(x,y) -> potAnar3_2 (x,y) (dx,dy) (n-1)) $ moviments (ox,oy)) then True else False

potAnar3' :: Pos -> Pos -> Bool
potAnar3' p q = q `elem` destins
    where destins = (moviments p >>= moviments >>= moviments)
