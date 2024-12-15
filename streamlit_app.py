import streamlit as st
import warnings
from crewai import Agent, Task, Crew, Process
from crewai_tools import ScrapeWebsiteTool, SerperDevTool
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

# Warning control
warnings.filterwarnings('ignore')

# Load environment variables
load_dotenv()


def initialize_tools():
    return SerperDevTool(), ScrapeWebsiteTool()

def create_agents(search_tool, scrape_tool):
    data_analyst_agent = Agent(
        role="Data Analyst",
        goal="Monitor and analyze market data in real-time to identify trends and predict market movements.",
        backstory="Specializing in financial markets, this agent uses statistical modeling and machine learning to provide crucial insights.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )
    
    trading_strategy_agent = Agent(
        role="Trading Strategy Developer",
        goal="Develop and test various trading strategies based on insights from the Data Analyst Agent.",
        backstory="Equipped with a deep understanding of financial markets and quantitative analysis, this agent devises and refines trading strategies.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )
    
    execution_agent = Agent(
        role="Trade Advisor",
        goal="Suggest optimal trade execution strategies based on approved trading strategies.",
        backstory="This agent specializes in analyzing the timing, price, and logistical details of potential trades.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )
    
    risk_management_agent = Agent(
        role="Risk Advisor",
        goal="Evaluate and provide risks associated with potential trading activities.",
        backstory="Armed with a deep understanding of risk assessment models and market dynamics, this agent scrutinizes potential risks.",
        verbose=True,
        allow_delegation=True,
        tools=[scrape_tool, search_tool]
    )
    
    return [data_analyst_agent, trading_strategy_agent, execution_agent, risk_management_agent]

def create_tasks(agents, inputs):
    tasks = [
        Task(
            description=f"Continuously monitor and analyze market data for the selected stock ({inputs['stock_selection']}). Use statistical modeling and machine learning to identify trends and predict market movements.",
            expected_output=f"Insights and alerts about significant market opportunities or threats for {inputs['stock_selection']}.",
            agent=agents[0]
        ),
        Task(
            description=f"Develop and refine trading strategies based on the insights from the Data Analyst and user-defined risk tolerance ({inputs['risk_tolerance']}). Consider trading preferences ({inputs['trading_strategy_preference']}).",
            expected_output=f"A set of potential trading strategies for {inputs['stock_selection']} that align with the user's risk tolerance.",
            agent=agents[1]
        ),
        Task(
            description=f"Analyze approved trading strategies to determine the best execution methods for {inputs['stock_selection']}, considering current market conditions and optimal pricing.",
            expected_output=f"Detailed execution plans suggesting how and when to execute trades for {inputs['stock_selection']}.",
            agent=agents[2]
        ),
        Task(
            description=f"Evaluate the risks associated with the proposed trading strategies and execution plans for {inputs['stock_selection']}. Provide a detailed analysis of potential risks and suggest mitigation strategies.",
            expected_output=f"A comprehensive risk analysis report detailing potential risks and mitigation recommendations for {inputs['stock_selection']}.",
            agent=agents[3]
        )
    ]
    return tasks

def main():
    st.set_page_config(page_title="Financial Analysis Crew", layout="wide")
    
    st.title("🤖 Financial Analysis Crew")
    st.markdown("---")
    
    with st.sidebar:
        st.header("Input Parameters")
        stock_selection = st.text_input("Stock Symbol", value="AAPL")
        initial_capital = st.number_input("Initial Capital", value=100000, step=1000)
        risk_tolerance = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
        trading_strategy = st.selectbox("Trading Strategy", ["Day Trading", "Swing Trading", "Position Trading"])
        news_impact = st.checkbox("Consider News Impact", value=True)
        
        run_analysis = st.button("Run Analysis")
    
    if run_analysis:
        inputs = {
            'stock_selection': stock_selection,
            'initial_capital': str(initial_capital),
            'risk_tolerance': risk_tolerance,
            'trading_strategy_preference': trading_strategy,
            'news_impact_consideration': news_impact
        }
        
        with st.spinner("Initializing agents and tools..."):
            search_tool, scrape_tool = initialize_tools()
            agents = create_agents(search_tool, scrape_tool)
            tasks = create_tasks(agents, inputs)
            
            crew = Crew(
                agents=agents,
                tasks=tasks,
                manager_llm=ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7),
                process=Process.hierarchical,
                verbose=True
            )
        
        with st.spinner("Analyzing... This may take a few minutes..."):
            result = crew.kickoff(inputs=inputs)
        
        st.markdown("## 📊 Analysis Results")
        st.markdown("---")
        st.markdown(result)

if __name__ == "__main__":
    main()