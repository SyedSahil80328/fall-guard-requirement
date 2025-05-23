import json

task_dict = {
    "01": "Stand for 30 seconds",
    "02": "Stand, slowly bend the back with or without bending at knees, tie shoe lace, and get up",
    "03": "Pick up an object from the floor",
    "04": "Gently jump (try to reach an object)",
    "05": "Stand, sit to the ground, wait a moment, and get up with normal speed",
    "06": "Walk normally with turn (4m)",
    "07": "Walk quickly with turn (4m)",
    "08": "Jog normally with turn (4m)",
    "09": "Jog quickly with turn (4m)",
    "10": "Stumble while walking",
    "11": "Sit on a chair for 30 seconds",
    "12": "Sit on the sofa (back is inclined to the support) for 30 seconds",
    "13": "Sit down to a chair normally, and get up from a chair normally",
    "14": "Sit down to a chair quickly, and get up from a chair quickly",
    "15": "Sit a moment, trying to get up, and collapse into a chair",
    "16": "Stand, sit on the sofa (back is inclined to the support), and get up normally",
    "17": "Lie on the bed for 30 seconds",
    "18": "Sit a moment, lie down to the bed normally, and get up normally",
    "19": "Sit a moment, lie down to the bed quickly, and get up quickly",
    "35": "Walk upstairs and downstairs normally (5 steps)",
    "36": "Walk upstairs and downstairs quickly (5 steps)",
    "20": "Forward fall when trying to sit down",
    "21": "Backward fall when trying to sit down",
    "22": "lateral fall when trying to sit down",
    "23": "Forward fall when trying to get up",
    "24": "lateral fall when trying to get up",
    "25": "Forward fall while sitting, caused by fainting",
    "26": "lateral fall while sitting, caused by fainting",
    "27": "Backward fall while sitting, caused by fainting",
    "28": "Vertical(forward) fall while walking caused by fainting",
    "29": "Fall while walking, use of hands to dampen fall, caused by fainting",
    "30": "Forward fall while walking caused by a trip",
    "31": "Forward fall while jogging caused by a trip",
    "32": "Forward fall while walking caused by a slip",
    "33": "Lateral fall while walking caused by a slip",
    "34": "Backward fall while walking caused by a slip"
}

with open('task_dict.json', 'w') as f:
    json.dump(task_dict, f, indent=4)
