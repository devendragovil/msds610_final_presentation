from crypt import methods
from flask import Flask, render_template, url_for, flash, redirect, request
# from hash import *
import time,os
from IPython.display import display
import random, string
import pandas as pd
from lolviz import *

app = Flask(__name__,template_folder='template')
app.config['UPLOAD_FOLDER'] = 'static'
app.config['SEND_FILE_MAX_AGE_DEFAULT'] = 0
n=20
prefs.max_list_elems = 50
prefs.max_str_le= 20

write_file_random = random.randint(1,1_000_000_000)

def save_img(tbl_viz):
    if os.path.exists('static/chain_table.png'):
        os.remove('static/chain_table.png')
        os.remove('static/chain_table')
    tbl_viz.render('static/chain_table',format='png', view=False)
    bkt_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'chain_table.png')
    return bkt_img_path

def save_img2(tbl_viz):
    if os.path.exists('static/chain_table2.png'):
        os.remove('static/chain_table2.png')
        os.remove('static/chain_table2')
    tbl_viz.render('static/chain_table2',format='png', view=False)
    bkt_img_path = os.path.join(app.config['UPLOAD_FOLDER'], 'chain_table2.png')
    return bkt_img_path

def parse_data_from_random_files():
    all_files = os.listdir('./write_folder/')
    all_fav_num = []
    all_first_names = []
    for file in all_files:
        with open('./write_folder/'+file, 'r') as f:
            all_lines= f.readlines()
        for line in all_lines:
            line_cl= line.strip().split(',')
            all_fav_num.append(int(line_cl[0]))
            all_first_names.append(line_cl[1])
    return all_fav_num, all_first_names



@app.route("/")
def home():
    return render_template("main_page.html")

@app.route("/submit", methods=['POST'])
def fetch_data():
    fav_num = request.form.get("fav")
    fname = request.form.get("fname")
    for a in string.punctuation:
        if a in fname:
            return "Invalid Response! Go back and try again!"
    for a in "0123456789":
        if a in fname:
            return "Invalid Response! Go back and try again!"
    with open(f'./write_folder/random_{write_file_random}.txt','a') as f:
        f.write(f"{fav_num},{fname}")
        f.write('\n')
    return "Successful Entry! Hurray!"

@app.route("/cleanfiles")
def clean_files():
    all_files = os.listdir('./write_folder/')
    for file in all_files:
        os.remove('./write_folder/'+file)
    return "Successfully Cleared all files in write_folder"

@app.route("/linear")
def linear():
    all_fav_num, all_first_names= parse_data_from_random_files()
    df = pd.DataFrame()
    indices = list(range(50))
    df['index']= list(range(50))
    df['Favorite Number'] = [None]*50
    df['First Names']= [None]*50
    for i, num in enumerate(all_fav_num):
        num_new = num*4
        prepared_list = list(range(num_new,50)) + list(range(0, num_new))
        for trial in prepared_list:
            if df.loc[trial,'Favorite Number'] is None:
                df.loc[trial,'Favorite Number'] = num
                df.loc[trial,'First Names'] = all_first_names[i]
                break
    final_list = list(zip(df['Favorite Number'].values,df['First Names'].values))
    tbl_viz=listviz(final_list, showassoc=False)
    bkt_img=save_img2(tbl_viz)
    return render_template("table.html", user_image=bkt_img)
# def linear():
#     all_fav_num, all_first_names= parse_data_from_random_files()
#     df = pd.DataFrame()
#     indices = list(range(50))
#     df['index']= list(range(50))
#     df['Favorite Number'] = [None]*50
#     df['First Names']= [None]*50
#     for i, num in enumerate(all_fav_num):
#         num_new = num*4
#         prepared_list = list(range(num_new,50)) + list(range(0, num_new))
#         for trial in prepared_list:
#             if df.loc[trial,'Favorite Number'] is None:
#                 df.loc[trial,'Favorite Number'] = num
#                 df.loc[trial,'First Names'] = all_first_names[i]
#                 break
#     return df.to_html()


@app.route("/chain")
def chain():
    all_fav_num, all_first_names= parse_data_from_random_files()
    chain_ht= [[] for x in range(10)]
    for i, num in enumerate(all_fav_num):
        chain_ht[num].append((num, all_first_names[i], "Ptr"))
    tbl_viz=lolviz(chain_ht)
    bkt_img=save_img(tbl_viz)
    return render_template("table.html", user_image=bkt_img)

@app.route("/display")
def display():
    pass



if __name__=='__main__':
    app.run()