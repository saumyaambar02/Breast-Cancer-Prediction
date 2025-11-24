from data_loader import load_data
from eda import generate_pairplot, plot_target_distribution, scatter_plot, correlation_heatmap
from preprocessing import split_features, create_train_test_split
from model import build_model
from train import train_model
from evaluate import evaluate_model
from visualize import show_plots

def main():
    df, cancer = load_data()
    print(df.head())
    print(df.tail())

    # EDA
    generate_pairplot(df)
    plot_target_distribution(df)
    scatter_plot(df)
    correlation_heatmap(df)

    # Preprocessing
    X, y = split_features(df)
    X_train, X_test, y_train, y_test = create_train_test_split(X, y)

    # Model
    model = build_model()

    # Training
    trained_model = train_model(model, X_train, y_train)

    # Evaluation
    evaluate_model(trained_model, X_test, y_test)

    # Show all plots
    show_plots()

if __name__ == "__main__":
    main()
