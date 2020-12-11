# first round recommend query
select UserId, recommended_item, category_code, brand, frequency from
(select UserId, recommended_item, frequency from recommended_item_single
where UserId = '113868975'
order by frequency
DESC LIMIT 5) as recommend_round1
inner join original_data o
on recommend_round1.recommended_item = o.product_id

sample_output:
UserId, recommended_item, category_code, brand, frequency
113868975,1004856,furniture.kitchen.pot,robam,415
113868975,1005115,apparel.shoes,respect,542
113868975,100068488,furniture.kitchen.table,febest,340
113868975,5100855,apparel.shoes.keds,rosenberg,93
113868975,1003316,computers.peripherals.printer,sokolov,80


-- select  recommended_item_1, recommended_item_2, rp.frequency from
--     (select UserId, recommended_item, category_code, brand, frequency from
--         (select UserId, recommended_item, frequency from recommended_item_single
--         where UserId = '113868975'
--         order by frequency
--         DESC LIMIT 5) as pre_process
--     inner join original_data o
--     on pre_process.recommended_item = o.product_id) as recommend_round1
-- inner join recommended_item_pairs rp
-- on rp.recommended_item_1 = recommend_round1.recommended_item
-- or rp.recommended_item_2 = recommend_round1.recommended_item
-- order by frequency
-- DESC LIMIT 5

# second round recommend query
set session sql_mode='TRADITIONAL';
select recommended_item_1 reference_item, recommended_item_2 recommended_item, category_code, brand from
(select recommended_item_1, recommended_item_2, frequency from recommended_item_pairs
where recommended_item_1 = '1005115'
group by recommended_item_2
order by frequency DESC LIMIT 5) as recommend_round2
inner join original_data o
on recommended_item_2 = o.product_id
group by recommended_item_2
order by frequency
DESC LIMIT 5


sample_output:
reference_item, recommended_item, category_code, brand
1005115,1005105,apparel.shoes,respect
1005115,1004226,furniture.living_room.chair,lego
1005115,100068488,furniture.kitchen.table,febest
1005115,1005100,computers.components.cooler,yamaha
1005115,1004659,computers.desktop,florentina

# third round recommend query
set session sql_mode='TRADITIONAL';
select reference_item1, reference_item2, recommended_item, category_code, brand from
(select recommended_item_1 reference_item1, recommended_item_2 reference_item2, recommended_item_3 recommended_item, frequency
from recommended_item_triple rt
where rt.recommended_item_1 = '1005115'
and rt.recommended_item_2 = '1004226'
group by recommended_item
order by frequency
DESC LIMIT 5) as recommend_round3
inner join original_data o
on o.product_id = recommend_round3.recommended_item

sample_output:
reference_item1, reference_item2, recommended_item, category_code, brand
1005115,1004226,1005105,apparel.shoes,respect
1005115,1004226,1004227,kids.dolls,bestway
1005115,1004226,1004249,appliances.kitchen.hob,electrolux
1005115,1004226,1005116,apparel.pajamas,yusufhali
1005115,1004226,4804056,computers.desktop,comforser

# fourth round recommend query
set session sql_mode='TRADITIONAL';
select reference_item1, reference_item2, reference_item3, recommended_item, category_code, brand from
(select recommended_item_1 reference_item1, recommended_item_2 reference_item2, recommended_item_3 reference_item3,
       recommended_item_4 recommended_item, frequency from recommended_item_four rf
where rf.recommended_item_1 = '1005115'
and rf.recommended_item_2 = '1004226'
and rf.recommended_item_3 = '1004249'
group by recommended_item
order by frequency
DESC LIMIT 5) as recommend_round4
inner join original_data o
on o.product_id = recommend_round4.recommended_item

sample_output:
reference_item1, reference_item2, reference_item3, recommended_item, category_code, brand
1005115,1004226,1004249,5100855,apparel.shoes.keds,rosenberg
1005115,1004226,1004249,4804056,electronics.audio.microphone,hayali
1005115,1004226,1004249,1003312,furniture.living_room.chair,
1005115,1004226,1004249,1004870,computers.peripherals.printer,sokolov
1005115,1004226,1004249,5100855,appliances.kitchen.kettle,tramontina
