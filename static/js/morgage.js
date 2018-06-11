function morgage() {
	a = Number($("#sale_price").val()) * 10000;
	b = Number($("#down_percent").val()) / 100.0;
	c = Number($("#year_term").val());
	d = Number($("#annual_interest_percent").val()) / 100.0;

	repay = (a*b*d)/12 + ((a*b)/c/12);
	$("#monthlyrepay").val(repay);
	$("#total_loan").val(a * b);

}




