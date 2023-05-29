var alertFunc = function () {
	alert("Hello world!"); //アラートで出力される文字をHello world!に変更してください
};

var outputFunc = function () {
	var output = document.getElementById("OutTextBox");
	output.innerText = document.forms.FontForm.InTextBox.value;
};

// ステップex-4：
var inputFunc = function () {
	var output = document.getElementById("outputCheck");
	flag = document.forms.inputForm.textBox.value
	if (flag === "") {
		output.innerText = "error!";
	} else {
		output.innerText = document.forms.inputForm.textBox.value;
	}

	var length = document.getElementById("len");
	length.innerText = document.forms.inputForm.textBox.value.length;


	var blankCheck = document.getElementById("error");
	var flag = document.forms.inputForm.textBox.value;
	if (flag === "") {
		blankCheck.innerText = "文字が入力されていません";
	} else {
		blankCheck.innerText = "OK!";
	}
};

// ステップex-5：
var inputCalc = function () {
	var outputPlus = document.getElementById("outputPlus");
	var outputMinus = document.getElementById("outputMinus");
	var outputMulti = document.getElementById("outputMulti");
	var outputDiv = document.getElementById("outputDiv");
	var outputLog = document.getElementById("outputLog");
	var calcNum1 = document.forms.calc.calcNum1.value;
	var calcNum2 = document.forms.calc.calcNum2.value;

	if (Number.isInteger(parseInt(calcNum1)) && Number.isInteger(parseInt(calcNum2))) {
		outputPlus.innerText = parseInt(calcNum1) + parseInt(calcNum2)
		outputMinus.innerText = parseInt(calcNum1) - parseInt(calcNum2)
		outputMulti.innerText = parseInt(calcNum1) * parseInt(calcNum2)
		outputDiv.innerText = parseInt(calcNum1) / parseInt(calcNum2)
		outputLog.innerText = "OK";
	} else {
		outputPlus.innerText = ""
		outputMinus.innerText = ""
		outputMulti.innerText = ""
		outputDiv.innerText = ""
		outputLog.innerText = "正常に入力されていません";
	}
};

// おまけ：テーブル出力
var tableOutput = function () {

	var tableOutput = document.getElementById("tableOutput");
	var table
		= "<td>id</td><td>name</td><tr><td>1</td><td>田中</td></tr><tr><td>2</td><td>遠藤</td></tr><td>3</td><td>山田</td></tr>"
	tableOutput.innerHTML = table;
};

// おまけ：アニメーション
var shapeChange = function () { //図形チェンジ
	var target = document.getElementById("target");
	target.classList.toggle("circle");
};