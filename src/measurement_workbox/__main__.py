import measurement_workbox as mw


def main():
    """Measurement Workbox Information"""
    print("Measurement Workbox Examples")
    array = mw.Matrix()
    print(array.vals[0])
    auto = mw.Automate()
    print(auto.root)
    fig = mw.Figure()
    print(fig.type)

if __name__ == "__main__":
    main()