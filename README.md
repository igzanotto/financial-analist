# Financial Analysis Crew 📊

A sophisticated AI-powered financial analysis tool that leverages multiple AI agents to provide comprehensive market analysis, trading strategies, execution plans, and risk assessments.

## 🌟 Features

- Real-time market data monitoring and analysis
- Custom trading strategy development
- Trade execution recommendations
- Risk assessment and mitigation strategies
- User-configurable parameters for personalized analysis
- Web-based interface built with Streamlit

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- OpenAI API key
- Serper Dev API key

### Installation

1. Clone the repository:
```bash
git clone <repository-url>
cd financial-analysis-crew
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the root directory with your API keys:
```plaintext
OPENAI_API_KEY=your_openai_api_key
SERPER_API_KEY=your_serper_api_key
```

### Running the Application

Launch the Streamlit app:
```bash
streamlit run streamlit_app.py
```

## 💻 Usage

1. Access the web interface through your browser (typically at `http://localhost:8501`)

2. Configure your analysis parameters in the sidebar:
   - **Stock Symbol**: Enter the ticker symbol (e.g., AAPL, GOOGL)
   - **Initial Capital**: Set your investment amount
   - **Risk Tolerance**: Choose between Low, Medium, or High
   - **Trading Strategy**: Select Day Trading, Swing Trading, or Position Trading
   - **News Impact**: Toggle whether to consider news impact in analysis

3. Click "Run Analysis" to start the AI agents

4. Review the comprehensive analysis results, including:
   - Market trends and predictions
   - Recommended trading strategies
   - Execution suggestions
   - Risk assessment and mitigation recommendations

## 🤖 AI Agents

The system employs four specialized AI agents:

1. **Data Analyst**: Monitors and analyzes market data in real-time
2. **Trading Strategy Developer**: Develops and tests trading strategies
3. **Trade Advisor**: Suggests optimal trade execution strategies
4. **Risk Advisor**: Evaluates and provides risk assessments

## 🛠️ Technologies Used

- Streamlit: Web interface
- CrewAI: Multi-agent orchestration
- LangChain: LLM integration
- OpenAI: Language model
- Serper Dev: Web search capabilities

## ⚠️ Disclaimer

This tool is for educational and research purposes only. Always conduct your own research and consult with financial professionals before making investment decisions. The creators and contributors of this tool are not responsible for any financial losses or decisions made based on its outputs.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📧 Support

If you encounter any problems or have questions, please open an issue in the repository.

## 🙏 Acknowledgments

- OpenAI for providing the language model capabilities
- CrewAI for the multi-agent framework
- The Streamlit team for their amazing web framework