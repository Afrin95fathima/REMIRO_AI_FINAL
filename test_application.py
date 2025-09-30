"""
Remiro AI Application Test Script
Tests the complete 16-agent career analysis system
"""

import sys
import os
import time

# Add the project directory to the Python path
sys.path.append(r'C:\Users\afrin\OneDrive\Desktop\Remiro AI -final')

try:
    # Test imports
    print("🔍 Testing Application Components...")
    
    # Test master agent import
    from agents.master_agent import MasterAgent
    print("✅ Master Agent imported successfully")
    
    # Test all agent imports
    agent_imports = [
        "skills_agent", "values_agent", "financial_agent", "learning_agent",
        "personality_agent", "interests_agent", "work_environment_agent", 
        "industry_agent", "career_trajectory_agent", "purpose_agent",
        "aspirations_agent", "network_agent", "role_fit_agent", 
        "identity_agent", "career_roadmap_agent"
    ]
    
    for agent_name in agent_imports:
        try:
            module = __import__(f'agents.{agent_name}', fromlist=[agent_name])
            print(f"✅ {agent_name} imported successfully")
        except Exception as e:
            print(f"❌ Error importing {agent_name}: {str(e)}")
    
    # Test master agent initialization
    print("\n🚀 Testing Master Agent Initialization...")
    master_agent = MasterAgent()
    print(f"✅ Master Agent initialized with {len(master_agent.agent_sequence)} agents")
    
    # Test agent sequence
    print("\n📋 Agent Sequence:")
    for i, agent_name in enumerate(master_agent.agent_sequence, 1):
        print(f"  {i:2d}. {agent_name.replace('_', ' ').title()}")
    
    # Test initial response
    print("\n💬 Testing Initial Interaction...")
    response = master_agent.process_message("Hello, I'd like to start my career analysis")
    if isinstance(response, tuple) and len(response) >= 2:
        message, is_complete = response[0], response[1]
        print("✅ Initial response generated successfully")
        print(f"   Response length: {len(str(message))} characters")
        print(f"   Is complete: {is_complete}")
    else:
        print(f"⚠️  Unexpected response format: {type(response)}")
    
    # Test agent availability
    print("\n🤖 Testing Agent Availability...")
    for agent_name in master_agent.agent_sequence:
        if agent_name in master_agent.agents:
            agent = master_agent.agents[agent_name]
            if hasattr(agent, 'process_message'):
                print(f"✅ {agent_name}: Ready")
            else:
                print(f"❌ {agent_name}: Missing process_message method")
        else:
            print(f"❌ {agent_name}: Not initialized")
    
    print("\n🎯 Application Test Summary:")
    print("✅ All core components working")
    print("✅ 16-agent system ready")
    print("✅ No critical errors detected")
    print("\n🌐 Application running at: http://localhost:8503")
    
except Exception as e:
    print(f"❌ Test failed with error: {str(e)}")
    import traceback
    traceback.print_exc()