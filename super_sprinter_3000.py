from flask import Flask, render_template, request, redirect, url_for
import data_manager

app = Flask(__name__, static_url_path="/static")


@app.route('/list')
@app.route('/')
def render_list():
    user_stories = data_manager.get_data_from_file('stories.csv')

    return render_template('list.html', user_stories=user_stories)


@app.route('/story')
def render_form():
    return render_template('form.html', title="Add New Story", user_story={})


@app.route('/story', methods=['POST'])
def save_post_data():

    form_data_list = ["{}:{}".format(key, request.form[key]) for key in request.form]
    data_manager.add_to_file(form_data_list)

    return render_template('form.html', title="Add New Story", user_story={})


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def render_filled_form(story_id):

    user_stories = data_manager.get_data_from_file('stories.csv')

    if request.method == 'GET':
        return render_template('form.html', title="Edit Story", user_story=user_stories[int(story_id) - 1])

    if request.method == 'POST':
        user_stories[int(story_id) - 1] = request.form
        data_manager.write_to_file(user_stories)

        return redirect(url_for('render_list'))


@app.route('/delete/<story_id>')
def delete_story(story_id):
    user_stories = data_manager.get_data_from_file('stories.csv')
    del user_stories[int(story_id) - 1]
    data_manager.write_to_file(user_stories)

    return redirect(url_for('render_list'))


if __name__ == '__main__':
    app.run()
