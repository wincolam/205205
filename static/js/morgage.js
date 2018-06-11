function morgage() {
	p = Number($("#sale_price").val()) * 10000;
	down = Number($("#down_percent").val()) / 100.0;
	year = Number($("#year_term").val());
	r = Number($("#annual_interest_percent").val()) / 100.0;

	$("#monthlyrepay").val(p * down / ((year * r) / 12));
	$("#total_loan").val((p * down * year * r) - p);

}




