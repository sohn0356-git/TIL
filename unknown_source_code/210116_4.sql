SELECT plus.PF, plus.PL, plus.puv, plus.psum-minus.msum, IF(minus.msum<plus.credit, "YES", "NO") FROM (
(SELECT user.vpa AS muv, SUM(trans.amount) AS msum FROM user_financial_detail as user JOIN transaction_log as trans ON user.vpa = trans.paid_by GROUP BY trans.paid_by) AS minus JOIN

(SELECT user.first_name AS PF, user.last_name AS PL, user.vpa AS puv, SUM(trans.amount) AS psum, user.credit_limit AS credit FROM user_financial_detail AS user JOIN transaction_log as trans ON user.vpa = trans.paid_to GROUP BY trans.paid_to) AS plus ON minus.muv = plus.puv
)