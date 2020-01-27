from utilities import Banner
def build_facility_report(arboretum):
    Banner.display_banner()

    for river in arboretum.rivers:
        print(river)
    for coastline in arboretum.coastlines:
        print(coastline)

    input("\n\nPress any key to continue...")
