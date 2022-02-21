
class LitercartDB:

    def find_order_id_by_email(self, email):
        self.execute(f"SELECT * FROM lc_orders WHERE customer_email = '{email}' AND date_created >= SUBTIME(NOW(), "
                     f"'0:2:0.000000')")
        return self.fetchall()

    def delete_order_by_email(self, email):
        self.execute(f"DELETE FROM lc_orders WHERE customer_email = '{email}' AND date_created >= SUBTIME(NOW(), "
                     f"'0:2:0.000000')")
