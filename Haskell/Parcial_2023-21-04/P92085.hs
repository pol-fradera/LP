data Nat = Z | S Nat
    deriving Show

rec :: a -> (Nat -> a -> a) -> Nat -> a
rec base step Z = base 
rec base step (S n) = step n (rec base step n)

isEven :: Nat -> Bool 
isEven = rec base step
    where 
        base = True 
        step = \n pn -> not pn      -- pn diu si n és parell

add :: Nat -> (Nat -> Nat)
add = rec base step 
    where 
        base = id 
        step = \n sn m -> S (sn m)      -- sn és la funció que suma n

mul :: Nat -> (Nat -> Nat)
mul = rec base step 
    where 
        base = const Z
        step = \n pn m -> (add m) (pn m)        -- pn és la funció que multiplica per n

fact :: Nat -> Nat 
fact = rec base step 
    where 
        base = S Z 
        step = \n fn -> mul (S n) fn           -- fn és el factorial de n
