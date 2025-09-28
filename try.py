import numpy as np
import matplotlib.pyplot as plt
import sys


def load_csv(path):
    data = np.genfromtxt(path, delimiter=",", names=True, dtype=None, encoding="utf-8")
    years = data["Year"]
    area = data["Area_harvested"].astype(float)
    yld = data["Yield"].astype(float)
    return years, area, yld


def plot_scatter(years, yld, country):
    plt.figure(figsize=(8, 5))
    plt.scatter(years, yld, c="blue")
    plt.title(f"{country}: Yield by Year")
    plt.xlabel("Year")
    plt.ylabel("Yield (hg/ha)")
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.show()


def plot_bar(years, area, country):
    plt.figure(figsize=(8, 5))
    plt.bar(years, area, color="green")
    plt.title(f"{country}: Area Harvested by Year")
    plt.xlabel("Year")
    plt.ylabel("Area harvested (ha)")
    plt.grid(True, axis="y", linestyle="--", alpha=0.6)
    plt.show()


def plot_combined(ghana_data, ivory_data, output="combined_cocoa_plots.pdf"):
    ghana_years, ghana_area, ghana_yield = ghana_data
    ivory_years, ivory_area, ivory_yield = ivory_data

    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    fig.suptitle("Cocoa Production in Ghana and Ivory Coast", fontsize=16, fontweight="bold")
    #scatter ghana yield
    axs[0, 0].scatter(ghana_years, ghana_yield, color="blue")
    axs[0, 0].set_title("Ghana: Yield by Year")
    axs[0, 0].set_xlabel("Year")
    axs[0, 0].set_ylabel("Yield (hg/ha)")
    axs[0, 0].grid(True, linestyle="--", alpha=0.6)

    # scatter ivory coast yield
    axs[0, 1].scatter(ivory_years, ivory_yield, color="red")
    axs[0, 1].set_title("Ivory Coast: Yield by Year")
    axs[0, 1].set_xlabel("Year")
    axs[0, 1].set_ylabel("Yield (hg/ha)")
    axs[0, 1].grid(True, linestyle="--", alpha=0.6)

    # bar ghana harvest yield
    axs[1, 0].bar(ghana_years, ghana_area, color="green")
    axs[1, 0].set_title("Ghana: Area Harvested by Year")
    axs[1, 0].set_xlabel("Year")
    axs[1, 0].set_ylabel("Area harvested (ha)")
    axs[1, 0].grid(True, axis="y", linestyle="--", alpha=0.6)

    # bar ivory coast yield
    axs[1, 1].bar(ivory_years, ivory_area, color="orange")
    axs[1, 1].set_title("Ivory Coast: Area Harvested by Year")
    axs[1, 1].set_xlabel("Year")
    axs[1, 1].set_ylabel("Area harvested (ha)")
    axs[1, 1].grid(True, axis="y", linestyle="--", alpha=0.6)

    plt.tight_layout()
    plt.savefig(output)
    plt.show()


def main():
    ghana_file = r"C:\Users\hp\Downloads\ghana_cocoa.csv"
    ivory_file = r"C:\Users\hp\Downloads\ivory_coast_cocoa.csv"

    ghana_years, ghana_area, ghana_yield = load_csv(ghana_file)
    ivory_years, ivory_area, ivory_yield = load_csv(ivory_file)

    # Individual plot
    #plot_scatter(ghana_years, ghana_yield, "Ghana")
    #plot_bar(ghana_years, ghana_area, "Ghana")
    #plot_scatter(ivory_years, ivory_yield, "Ivory Coast")
    #plot_bar(ivory_years, ivory_area, "Ivory Coast")

    # Combined plot
    plot_combined(
        (ghana_years, ghana_area, ghana_yield),
        (ivory_years, ivory_area, ivory_yield)
    )

    return 0


if __name__ == "__main__":
    sys.exit(main())
