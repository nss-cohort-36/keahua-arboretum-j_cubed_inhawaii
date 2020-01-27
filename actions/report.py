def build_facility_report(arboretum):
    for river in arboretum.rivers:
        print(river)
    for coastline in arboretum.coastlines:
        print(coastline)

    input("\n\nPress any key to continue...")