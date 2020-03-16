import data_manager
from flask import Flask, render_template,request,redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mentors-with-best-first-name')
def mentor_names():
    # We get back dictionaries here (for details check 'database_common.py')
    mentor_names = data_manager.get_mentor_names_by_first_name('László')

    return render_template('mentor_names.html', mentor_names=mentor_names)

@app.route('/mentors-nick-names')
def mentor_nick_names():
    nick_names = data_manager.get_mentor_nick_name('Miskolc')
    return render_template('mentor_nicknames.html', mentor_nick_names=nick_names)

@app.route('/carol-full-name')
def get_carol_full_name():
    details = data_manager.get_carol_name('Carol')
    return render_template('carol.html', details=details)

@app.route('/mistery-name')
def get_misterious_full_details():
    details = data_manager.get_mistery_name()
    return render_template('misterygirl.html', details=details)


@app.route('/add-applicant', methods =['GET', 'POST'])
def add_applicant():
    if request.method == "GET":
        return render_template('add_aplicant.html')
    else:
        user_input = request.form.to_dict()
        data_manager.append_to_database('applicants' ,user_input)
        return redirect(url_for('index', application_code=user_input['application_code']))

@app.route('/show-all')
def show_all_applicants():
    applicants = data_manager.show_all()
    return render_template('all_aplicants.html', details = applicants)

@app.route('/show-applicant/<id>')
def show_info(id):
    applicant = data_manager.show_applicant(id)
    return render_template('applicant_info.html', applicant_info=applicant, display_all=True)

@app.route('/update-jamina')
def update_jamina():
    details = data_manager.update_applicant('Jemima', 'Foreman', '003670/223-7459')
    return render_template('update_jamina.html', details=details)
    
@app.route('/delete-applicants')
def delete_mariseu():
    applicant_id = data_manager.get_applicant_id('@mauriseu.net')
    applicant_id_list = []
    for id in applicant_id:
        applicant_id_list.append(str (id['id']))
    details = data_manager.delete_after_emai('@mauriseu.net', applicant_id_list)
    return render_template('delete_mariseu.html', details=details)

@app.route('/mentors')
def show_mentor_school():
    mentors = data_manager.get_mentor_schools()
    return render_template('mentors_and_schools.html', mentors=mentors)

@app.route('/all_school')
def show_schools():
    schools = data_manager.get_all_schools()
    return render_template('all_schools.html', schools=schools)


@app.route('/mentors_by_country')
def mentors_by_country():
    details = data_manager.get_no_of_mentors()
    return render_template('mentors_by_country.html', details=details)

@app.route('/contacts')
def contact():
    details = data_manager.get_contact_name()
    return render_template('contact.html', details=details)

@app.route('/applicants')
def get_applicants():
    details = data_manager.get_applicants()
    return render_template('applicants.html', details=details)


@app.route('/applicants_and_mentors')
def get_them_all():
    details = data_manager.get_applicants_and_mentors()
    return render_template('mentors_and_applicants.html', details=details)

if __name__ == '__main__':
    app.run(debug=True)
