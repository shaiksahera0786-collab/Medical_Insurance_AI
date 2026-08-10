import matplotlib.pyplot as plt


def plot_age_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(df["age"], bins=15)

    ax.set_title("Age Distribution")
    ax.set_xlabel("Age")
    ax.set_ylabel("Count")

    return fig


def plot_bmi_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(df["bmi"], bins=15)

    ax.set_title("BMI Distribution")
    ax.set_xlabel("BMI")
    ax.set_ylabel("Count")

    return fig


def plot_charges_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    ax.hist(df["charges"], bins=20)

    ax.set_title("Insurance Charges Distribution")
    ax.set_xlabel("Charges")
    ax.set_ylabel("Count")

    return fig


def plot_smoker_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    df["smoker"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Smoker Distribution")
    ax.set_xlabel("Smoker")
    ax.set_ylabel("Count")

    return fig


def plot_region_distribution(df):

    fig, ax = plt.subplots(figsize=(6,4))

    df["region"].value_counts().plot(
        kind="bar",
        ax=ax
    )

    ax.set_title("Region Distribution")
    ax.set_xlabel("Region")
    ax.set_ylabel("Count")

    return fig