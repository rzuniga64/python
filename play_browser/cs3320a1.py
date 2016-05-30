#   Raul Zuniga
#   CS3320 Internet Software Development
#   Assignment 1

import flask
import json
import glob
from flask import Flask

plays = dict()

for file in glob.glob('data/*.json'):
    with open(file, 'r') as yf:
        play = json.load(yf)
        plays[play["id"]] = play

app = Flask(__name__)

#   The root page (/) should have a heading that says something useful (e.g. ‘Plays of Shakespeare’), followed by a list
#   of plays.
#
#   The list should be a ul (bulleted list)
#   List the plays in order of year published (earliest first)
#   The play should be listed by its title
#   The title should be a hyperlink to the play, /play/<id>/ where <id> is the play's ID
#   After the title, list the play's date in parentheses


@app.route('/')
def index():
    title = "Plays of Shakespeare"
    return flask.render_template('index.html', plays=plays.values(), title=title)

#   When the user browses to /plays/12night/, or the corresponding URL for any other play, they should see a page that
#   has the following:
#
#   The play's full title as a level-1 heading
#   The play's date
#   A list of characters
#   A list of acts, each of which has a sub-list of scenes. Each scene should be a link to a page for that scene, of
#   the form: /play/<id>/acts/<act>/scenes/<scene>, so a link to Act 2 Scene 3 of Twelfth Night will be
#   /play/12night/acts/2/scenes/3.
#
#   Use Level 2 headings to introduce the list of characters and the list of acts (table of contents).


@app.route('/plays/<play_id>')
def show_play(play_id):
    title = "Plays"
    for current_play in plays.values():
        if current_play["id"] == play_id:
            play = current_play["id"]
            full_title = current_play["full_title"]
            date = current_play["date"]
            characters = current_play["characters"]
            acts = current_play["acts"]
            break
    return flask.render_template('play.html', title=title, play=play, full_title=full_title, date=date, characters=characters,
                                 acts=acts)


#   The scene page should have the following:
#
#   A level-1 heading of the play's title
#   A level-2 heading with the act and scene number
#   The scene's setting (right after the L2 act & scene number)
#   The blocks/speeches in the play
#   Hyperlinks to the previous and next scenes, if relevant (the first scene should not have a previous link, and the
#   last scene should not have a next link). These links should have the act and scene number as the text
#   (e.g. ‘Act 2 Scene 3’).

@app.route('/plays/<play_id>/act/<int:act_no>/scene/<int:scene_no>')
def show_scene(play_id, act_no, scene_no):
    title = "Scenese"
    scenes = []
    for current_play in plays.values():
        if current_play["id"] == play_id:
            play = current_play["id"]
            full_title = current_play["full_title"]
            for act in current_play["acts"]:
                for scene in act['scenes']:
                    scenes.append(scene)
            break
    for count, item in enumerate(scenes):
        if item['act'] == act_no and item['scene'] == scene_no:
            scene_pos = count
            setting = item['title']
            blocks = item['blocks']
            break
    return flask.render_template('scenes.html', title=title, play=play, full_title=full_title, setting=setting, blocks=blocks,
                                 scenes=scenes, scene_pos=scene_pos)


#   For this part, we will implement a cross-referencing system for characters.
#   Create a new URL handler for URLs of the form /characters/<character> that take a character ID.
#   This page should display the character's name as a level 1 heading, and a list of all plays in which that character
#   appears (looked up by ID — character IDs are globally unique across all plays). The plays should be listed by date,
#   exactly as they appear in the main plays list (part 1).
#
#   Modify the play info page (part 2) and the scene displays (part 3) so that the character names are hyperlinks to the
#   character pages.

@app.route('/characters/<character>')
def show_characters(character):
    title = "Characters"
    playlist = dict()
    for current_play in plays.values():
        full_title = current_play["full_title"]
        date = current_play["date"]
        chars = current_play["characters"]
        for char in chars:
            if char == character:
                play = dict()
                play["full_title"] = full_title
                play["date"] = date
                playlist[current_play['id']] = play
                break
    return flask.render_template('characters.html', title=title, character=character.capitalize(), playlist=playlist)

if __name__ == '__main__':
    app.run(debug=True)
