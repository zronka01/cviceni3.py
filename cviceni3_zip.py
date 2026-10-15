def my_zip(*iterables):
    """
    Nase vlastni implementace zip()

    iterables = [
        ["Alice", "Bob", "Karel", "Eva", "Martin"], -> len() -> 5
        [   30,     20,     24,     18,     27   ],
        [   50,     80,     90,     55,     67   ]
    ]

    results = [
        ()
        
        
        
        
    ]
    """
    pass


if __name__ == "__main__"":

    jmena = ["Alice", "Bob", "Karel", "Eva", "Martin"]
    vek =   [   30,     20,     24,     18,     27   ]
    vaha =  [   50,     80,     90,     55,     67   ]

    vysledek = list( zip(jmena, vek, vaha) )
    print(vysledek)
    # for jmeno, vek, vaha in vysledek:
    #     print(f{jmeno} jd {vek})