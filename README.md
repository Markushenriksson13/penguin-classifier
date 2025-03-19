# Penguin Species Classifier

This project implements a machine learning classifier to identify penguin species based on their physical measurements. The system is designed to help identify Adelie penguins in New York City using daily data updates.

## Project Structure

```
├── data/
│   ├── raw/         # Original penguin dataset
│   └── processed/    # Processed and transformed data
├── models/           # Trained model files
├── src/
│   ├── data/        # Data processing scripts
│   ├── models/      # Model training scripts
│   └── api/         # API interaction scripts
└── database/        # SQLite database files
```

## Technical Details

### Data Pipeline
- Data source: Seaborn penguins dataset
- Database: SQLite
- Features: bill_length_mm, bill_depth_mm, flipper_length_mm, body_mass_g

### Model
- Type: Classification model for penguin species identification
- Target: Identifying Adelie penguins
- Features: Selected based on correlation and importance analysis

### Automation
- GitHub Actions workflow for daily data fetching
- Automated predictions posted to GitHub Pages
- Schedule: Daily at 7:30 AM

### Dependencies
- Python 3.x
- Required packages (will be listed in requirements.txt)

## Setup and Usage

1. Clone the repository
2. Install dependencies
3. Run data processing pipeline
4. Train the model
5. Set up GitHub Actions

## License
MIT