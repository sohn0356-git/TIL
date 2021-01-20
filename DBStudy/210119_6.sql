#JSON (JAVASCRIPT OBJECT NOTATION)
SELECT * FROM items;
SELECT JSON_OBJECT('id',id,'name',name,'price',price,'redgate',YEAR(regdate)) FROM items;