UPDATE t_product_information i
	LEFT JOIN (
		SELECT cpid, SUM(sl) AS slhj
		FROM (
			SELECT d.fProductID AS cpid, -1 * d.fQuant AS sl
			FROM t_product_outbound_order_detail d
				RIGHT JOIN t_product_outbound_order o ON d.fOrderID = o.fOrderID
			WHERE o.fSubmited = 1
				AND o.fConfirmed = 1
				AND o.fCanceled = 0
			UNION ALL
			SELECT d.fProductID AS cpid, d.fQuant AS sl
			FROM t_product_warehousereceipt_order_detail d
				RIGHT JOIN t_product_warehousereceipt_order o ON d.fOrderID = o.fOrderID
			WHERE o.fSubmited = 1
				AND o.fCanceled = 0
		) q
		GROUP BY q.cpid
	) q1
	ON i.fID = q1.cpid
SET fCurrentQuantity = ifnull(q1.slhj, 0)