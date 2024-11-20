from flask import Flask,render_template,request

app = Flask(__name__)

@app.route('/')
def index():
    # データ入力ページの表示
    return render_template('index.html')

@app.route('/bmi', methods=["POST"])
def bmi_post():
    # 身長・体重データを取得
    weight = float(request.form["in_weight"])
    height = float(request.form["in_height"]) / 100

    # BMI値を計算，結果の判定
    bmi = round(weight / (height ** 2),1)
    if bmi < 18.5:
        result = "痩せ型"
    elif (bmi >= 18.5) and (bmi < 25):
        result = "標準体型"
    elif (bmi >= 25) and (bmi < 30):
        result = "肥満(軽)"
    else:
        result = "肥満(重)"
        print("BMI: " + str(bmi))
        print("判定: " + result)

    # 結果ページの表示
    return render_template('bmi.html', out_bmi = bmi, out_result = result)

if __name__ == '__main__':
    app.debug = True
    app.run(host='localhost')
