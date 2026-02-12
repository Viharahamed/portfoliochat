"""
Script to check existing Supabase tables and create missing ones
"""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import get_supabase


def check_and_create_tables():
    """Check what tables exist and create missing ones"""
    supabase = get_supabase()
    
    print("🔍 Checking existing tables...")
    
    # Try to query each table to see if it exists
    tables_status = {}
    
    tables_to_check = ['profiles', 'experiences', 'projects', 'skills', 'chat_history']
    
    for table in tables_to_check:
        try:
            response = supabase.table(table).select('*').limit(1).execute()
            tables_status[table] = 'EXISTS'
            print(f"✅ Table '{table}' exists")
        except Exception as e:
            tables_status[table] = 'MISSING'
            print(f"❌ Table '{table}' does not exist or has errors: {str(e)[:100]}")
    
    print("\n" + "=" * 60)
    print("SUMMARY:")
    for table, status in tables_status.items():
        print(f"  {table}: {status}")
    print("=" * 60)
    
    # Check if we need to create tables
    missing_tables = [t for t, s in tables_status.items() if s == 'MISSING']
    
    if missing_tables:
        print(f"\n⚠️ Missing tables: {', '.join(missing_tables)}")
        print("\nYou need to create these tables in Supabase.")
        print("Please run the SQL migrations in the Supabase dashboard.")
    else:
        print("\n✅ All required tables exist!")


if __name__ == "__main__":
    check_and_create_tables()
