invited_guest = ["Alice", "Bob", "Charlie"] # This is a list of invited guests

#sending the message each one
print(f"Hi {invited_guest[0]}, do you want to have a dinner with me tonight?")
print(f"Hi {invited_guest[1]}, do you want to have a dinner with me tonight?")
print(f"Hi {invited_guest[2]}, do you want to have a dinner with me tonight?")

#list of guest who can't come
guest_not_coming = "Charlie" # This guest is not coming
print(f"\nUnfortunately, {guest_not_coming} can't make it to the dinner.\n")

#sending new invitation to new people 
invited_guest[2] = "james"
print(f"Hi {invited_guest[2]}, do you want to have a dinner with me?\n")  

print(f"Hi guys {invited_guest} I just found a bigger dinner table online\n")

invited_guest.insert(0, "ice")
invited_guest.insert(2, "tristan")
invited_guest.append("gene")

#new set of sending dinner invitation
print(f"Hi {invited_guest[0]}, do you want to have a dinner with me tonight")
print(f"Hi {invited_guest[2]}, do you want to have a dinner with me tonight")
print(f"Hi {invited_guest[-1]}, do you want to have a dinner with me tonight")
