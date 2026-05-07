# Q1. You receive this list of tags from a form submission — clean it
#     submitted = ["django", "python", "api", "django", "rest", "python"]
#     Convert to a set, then back to a list and print it

submitted = ["django", "python", "api", "django", "rest", "python"]
tags = list(set(submitted))
print()
print(f"Unique tags: {tags}")

# Q2. Create two sets:
#     user_permissions = {"read", "write", "delete"}
#     required_permissions = {"read", "delete", "publish"}
#     Find and print:
#       a) All permissions combined (union)
#       b) Permissions the user and requirement share (intersection)
#       c) What the user has that isn't required (difference)
#       d) What the user is missing (difference the other way)

user_permissions = {"read", "write", "delete"}
required_permissions = {"read", "delete", "publish"}

#       a) All permissions combined (union)

all_permissions = user_permissions | required_permissions
print()
print(f"Union: {all_permissions}")

#       b) Permissions the user and requirement share (intersection)

shared_permissions = user_permissions & required_permissions
print()
print(f"Intersection: {shared_permissions}")


#       c) What the user has that isn't required (difference)

only_in_user_permission = user_permissions - required_permissions
print()
print(f"Only in User Permissions: {only_in_user_permission}")

#       d) What the user is missing (difference the other way)

only_in_required_permissions = required_permissions - user_permissions
print()
print(f"Only in Required Permissions: {only_in_required_permissions}")

# Q3. Check if "write" is in user_permissions — print a clear message
#     e.g. "Permission granted" or "Access denied"

if "write" in user_permissions:
    print("Permission granted")
else:
    print("Access denied")

# Q4. Add "publish" to user_permissions, then safely remove "execute"
#     (which doesn't exist) without crashing the program

user_permissions.add("publish")

print()
print(f"After adding 'publish': {user_permissions}")

# Removing using discard:

user_permissions.discard("execute")
print(f"Removed 'execute': {user_permissions}")