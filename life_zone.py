# def medium_radius(L_star):
#     if L_star<0:
#         print("Ошибка,болометрический показатель звезды не может быть отрицательным")
#     return (L_star/(3,86*(10**33)))**0,5


medium_radius = lambda L_star:((L_star/(3.86*(10**33)))**0.5)/149_597_870_700 
print(f"{medium_radius(2*10**60):.2f}")