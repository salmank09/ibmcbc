import json
import os.path
import __builtin__
import errno
import os

# Lesson using pytest
def simple_tdd_function(a,b):
    """Computes the sum of two integers

    Parameters
    ----------
    a : {int} a first number
    b : {int} a second number

    Returns
    -------
    int : the sum of those numbers
    """
    return a + b


# Exercise 1
def read_json_file(file_path):
    """Reads and parse a json file.

    Parameters
    ----------
    file_path : {str} the path to the json file.

    Returns
    -------
    dict : a dictionary containing the json structure read from the file.
    """
    if file_path.endswith('.json'):
        try:
            with open(file_path) as f:
                data = json.load(f)
            return data
        except:
            raise FileNotFoundError("File not found")
    else:
        raise ValueError('Please submit a .json file.')


# Exercise 2
def course_weeks_count(json_data):
    """Counts how many weeks there are in a course described in a JSON structure.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    int : the number of weeks in the course (0 if there is no weeks list)

    Notes
    -----
    look at data/course_1_full.json for an example of the structure of a course,
    here is a description of the schema of that structure:

    root (dict)
    |- key "course_id" => (str)
    |- key "weeks" => (list) of str
    |- key "content_units" => (dict) in which keys is a subset of the list found in "weeks"
                              and each entry of that dict is a list of strings
                              giving the names of the lessons.

    error cases: if the key 'weeks' doesn't exist, should return 0
    """

    if 'weeks' in json_data:
        if type(json_data['weeks']) != list:
            return 0
        else:
            return len(json_data['weeks'])
    else:
        return 0


# Exercise 3
def course_content_count(json_data):
    """Counts how many lessons there are in each week of a course.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    dict : a dictionary giving for each week of the course the number of lessons.

    Notes
    -----
    look at data/course_1_full.json for an example of the structure of a course,
    here is a description of the schema of that structure:

    root (dict)
    |- key "course_id" => (str)
    |- key "weeks" => (list) of str
    |- key "content_units" => (dict) in which keys is a subset of the list found in "weeks"
                              and each entry of that dict is a list of strings
                              giving the names of the lessons.

    error cases: weeks in 'content_units' that are not found in 'weeks' should not be counted
    error cases: if there is no 'weeks' in the course, return an empty dict
    """
    d = {}
    if 'weeks' in json_data:
        for week in json_data['weeks']:
            if week in json_data['content_units']:
                d[week] = len(json_data['content_units'][week])
        return d
    else:
        return d



# Exercise 4
def tones_parse_anger(json_data):
    """Returns the probability of detection of Anger in a ToneAnalyzer json response.

    Parameters
    ----------
    json_data : {dict} a JSON structure as read from a file using read_json_file().

    Returns
    -------
    float : the probability of the detection of Anger.

    Notes
    -----
    - if no Anger is found in the json structure, should return 0.0
    - within the list given by "tone_categories", emotion is not necessarily the first
    - within the list of tones that have "category_id": "emotion_tone", Anger is not necessarily the first
    """
    for tone_category in json_data['document_tone']['tone_categories']:
        if tone_category['category_name']=='Emotion Tone':
            for tone in tone_category['tones']:
                if tone["tone_name"]=="Anger":
                    return tone["score"]
    return 0.0
