# Octofit Tracker Frontend

This is the frontend for the Octofit Tracker application, a fitness tracking app that allows users to log activities, manage teams, and view leaderboards.

## Project Structure

- **public/index.html**: The main HTML file for the React application. It serves as the entry point for the web app and includes a root div where the React components will be rendered.
  
- **src/App.js**: Contains the main application component, including routing setup and the main layout of the application.
  
- **src/index.js**: The entry point for the React application that renders the `App` component into the root div of the `index.html` file. It also imports Bootstrap CSS for styling.
  
- **src/components**: A directory for various React components that can be used throughout the application.

- **package.json**: Contains metadata about the project, including dependencies, scripts, and other configurations necessary for npm.

## Setup Instructions

1. **Clone the repository**:
   ```
   git clone https://github.com/mayurbhat2000/skills-build-applications-w-copilot-agent-mode.git
   cd octofit-tracker/frontend
   ```

2. **Install dependencies**:
   ```
   npm install
   ```

3. **Run the application**:
   ```
   npm start
   ```

The application will be available at `http://localhost:3000`.

## Usage

- Users can create profiles, log activities, and manage teams.
- The app provides a competitive leaderboard and personalized workout suggestions.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or features.