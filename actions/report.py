from utilities import display_banner

def build_facility_report(arboretum):
    display_banner()

    for river in arboretum.rivers:
        print(river)
    for coastline in arboretum.coastlines:
        print(coastline)
    for grassland in arboretum.grasslands:
        print(grassland)

    input("\n\nPress any key to continue...")
