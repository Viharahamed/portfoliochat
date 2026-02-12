"""
Script to inspect table schemas in Supabase
"""

import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent.parent))

from app.database import get_supabase


def inspect_table_schema(table_name):
    """Try to get a sample record to see the schema"""
    supabase = get_supabase()
    
    try:
        response = supabase.table(table_name).select('*').limit(1).execute()
        if response.data:
            print(f"\n✅ Table '{table_name}' columns:")
            if len(response.data) > 0:
                for key in response.data[0].keys():
                    print(f"  - {key}")
            else:
                print("  (No data to infer schema)")
        else:
            print(f"\n✅ Table '{table_name}' exists but is empty")
    except Exception as e:
        print(f"\n❌ Error with table '{table_name}': {e}")


if __name__ == "__main__":
    tables = ['profiles', 'experiences', 'projects', 'skills']
    
    print("🔍 Inspecting table schemas...")
    print("=" * 60)
    
    for table in tables:
        inspect_table_schema(table)
    
    print("\n" + "=" * 60)
