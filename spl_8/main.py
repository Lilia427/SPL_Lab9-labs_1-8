from visualizer.csv_loader import CSVLoader
from visualizer.data_analyzer import DataAnalyzer
from visualizer.basic_visuals import BasicVisuals
from visualizer.advanced_visuals import AdvancedVisuals
from visualizer.multi_subplots import MultiSubplots
from visualizer.exporter import Exporter
from visualizer.config import Config

def main():
    print("=== Data Visualizer Application ===")
    
    # Step 1: Load CSV data
    csv_path = input("Enter the path to your CSV file (e.g., datasets/example.csv): ")
    loader = CSVLoader(csv_path)
    data = loader.load_data()
    
    if data is None:
        print("Failed to load data. Exiting.")
        return
    
    # Step 2: Analyze data
    analyzer = DataAnalyzer(data)
    print("\n=== Data Summary ===")
    print(analyzer.get_summary_statistics())
    
    print("\n=== Column Extremes ===")
    extremes = analyzer.get_column_extremes()
    for column, values in extremes.items():
        print(f"{column}: Min={values['min']}, Max={values['max']}")

    # Step 3: Choose visualization type
    print("\n=== Visualization Options ===")
    print("1. Line Chart")
    print("2. Bar Chart")
    print("3. Scatter Plot")
    print("4. Histogram")
    print("5. Multiple Subplots")
    
    choice = input("Select a visualization type (1-5): ")

    # Step 4: Visualize data
    visuals = None
    if choice in ["1", "2"]:
        visuals = BasicVisuals(data)
    elif choice in ["3", "4"]:
        visuals = AdvancedVisuals(data)
    elif choice == "5":
        visuals = MultiSubplots(data)
    else:
        print("Invalid choice. Exiting.")
        return

    if choice == "1":
        x_col = input("Enter the column for X-axis: ")
        y_col = input("Enter the column for Y-axis: ")
        visuals.line_chart(x_col, y_col)
    elif choice == "2":
        x_col = input("Enter the column for X-axis: ")
        y_col = input("Enter the column for Y-axis: ")
        visuals.bar_chart(x_col, y_col)
    elif choice == "3":
        x_col = input("Enter the column for X-axis: ")
        y_col = input("Enter the column for Y-axis: ")
        visuals.scatter_plot(x_col, y_col)
    elif choice == "4":
        col = input("Enter the column for the histogram: ")
        bins = int(input("Enter the number of bins (default 10): ") or 10)
        visuals.histogram(col, bins)
    elif choice == "5":
        x_col = input("Enter the column for X-axis: ")
        y_cols = input("Enter the columns for Y-axis (comma-separated): ").split(',')
        y_cols = [col.strip() for col in y_cols]
        visuals.multiple_charts(x_col, y_cols)

    # Step 5: Export visualization
    export_choice = input("\nDo you want to export the visualization? (yes/no): ").strip().lower()
    if export_choice == "yes":
        exporter = Exporter(Config.OUTPUT_DIR)
        filename = input("Enter the filename for export (without extension): ")
        format_choice = input("Enter the format (png/svg, default png): ").strip().lower() or "png"
        exporter.save_plot(filename, format_choice)
    else:
        print("Visualization not exported.")

    print("\n=== Done ===")
    print("Thank you for using the Data Visualizer!")

if __name__ == "__main__":
    main()
