import re

notes = ["C", "C#", "D", "D#", "E", "F", "F#", "G", "G#", "A", "A#", "B"]

pattern = r"[A-G][#B]?"


def mirror_inversion(axis, notes_in):

    inversion_axis_idx = notes.index(axis)

    rotated_notes = notes[inversion_axis_idx:] + notes[:inversion_axis_idx]

    mirrored_notes = []

    for note in notes_in:
        note_idx = rotated_notes.index(note)
        mirrored_notes.append(rotated_notes[0 - note_idx])

    return mirrored_notes


def validate_input(pattern):
    # Keep using the regular standard pattern: r"[A-G](?:[#b])?"
    invalid_notes = ["CB", "B#", "DB", "EB", "E#", "FB", "GB", "AB", "BB"]

    while True:
        axis_raw = input("Axis: ").strip()
        # Validate using original mixed-case regex first
        if not re.fullmatch(r"[A-G](?:[#b])?", axis_raw):
            print("ValueError: Invalid note format. Please enter exactly one valid note.")
            continue
            
        inversion_axis = axis_raw.upper()
        if inversion_axis in invalid_notes:
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break

    while True:
        notes_raw = input("Chord/notes: ").strip()
        # Find raw notes like 'Ab', 'B', 'C' before capitalizing them
        matches = re.findall(r"[A-G](?:[#b])?", notes_raw)
        
        # Verify the user didn't type junk letters (e.g. 'AbXT')
        if not matches or "".join(matches) != notes_raw.replace(" ", ""):
            print("ValueError: Invalid note(s).")
            continue
            
        notes_in = [x.upper() for x in matches]
        if any(x in invalid_notes for x in notes_in):
            print("ValueError: Only sharps (i.e. nice sharps...) for now.")
            continue
        else:
            break
            
    return inversion_axis, notes_in


print(f"{", ".join(map(str, mirror_inversion(*validate_input(pattern))))}")

# sort notes (in relation to axis)
# print(f"{", ".join(map(str, sorted(mirror_inversion(inversion_axis, notes_in))))}")
