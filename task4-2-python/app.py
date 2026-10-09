from datetime import datetime
import platform

print("=" * 55)
print("SWE40006 Task 4.2 - Python Docker Application")
print("=" * 55)

print("Application status: Running successfully")
print(f"Python version: {platform.python_version()}")
print(f"Platform: {platform.system()}")
print(f"Execution time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

print("=" * 55)
print("Task 4.2 Python container completed successfully.")
print("=" * 55)