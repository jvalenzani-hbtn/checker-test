def generate_invitations(template, attendees):
    # Check if template is a string
    if not isinstance(template, str):
        print(f"Error: Template should be a string, got {type(template)} instead.")
        return
    
    # Check if attendees is a list
    if not isinstance(attendees, list):
        print(f"Error: Attendees should be a list, got {type(attendees)} instead.")
        return

    # Check for empty template
    if template == "":
        print("Template is empty, no output files generated.")
        return
    
    # Check for empty attendees list
    if not attendees:
        print("No data provided, no output files generated.")
        return

    # Process each attendee
    for index, attendee in enumerate(attendees, start=1):
        if not isinstance(attendee, dict):
            print(f"Error: Each attendee should be a dictionary, got {type(attendee)} instead.")
            return

        # Replace placeholders with actual values or "N/A" if missing
        output = template
        output = output.replace("{name}", attendee.get("name", "N/A"))
        output = output.replace("{event_title}", attendee.get("event_title", "N/A"))
        output = output.replace("{event_date}", attendee.get("event_date", "N/A"))
        output = output.replace("{event_location}", attendee.get("event_location", "N/A"))

        # Write the output to a file
        with open(f'output_{index}.txt', 'w') as file:
            file.write(output)
    
    print(f"{index} output files generated.")
